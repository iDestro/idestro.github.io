import json
import os
import sys
import time
from datetime import datetime, timezone
from urllib.parse import parse_qs, urlparse

import requests
from bs4 import BeautifulSoup

PROFILE_URL = "https://scholar.google.com/citations?user={scholar_id}&hl=en&pagesize=100"
REQUEST_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/128.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}


def require_scholar_id() -> str:
    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", "").strip()
    if not scholar_id:
        raise SystemExit("GOOGLE_SCHOLAR_ID is missing or empty")
    return scholar_id


def parse_profile(html: str, scholar_id: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    name_el = soup.select_one("#gsc_prf_in")
    if name_el is None:
        raise RuntimeError("Google Scholar returned no author profile (blocked or captcha)")

    index_cells = soup.select("#gsc_rsb_st td.gsc_rsb_std")
    citedby = 0
    if index_cells:
        citedby = int(index_cells[0].get_text(strip=True) or "0")

    publications = {}
    for row in soup.select("#gsc_a_b tr.gsc_a_tr"):
        title_el = row.select_one("a.gsc_a_at")
        if title_el is None:
            continue
        href = title_el.get("href") or ""
        pub_id = parse_qs(urlparse(href).query).get("citation_for_view", [None])[0]
        if not pub_id:
            continue
        cite_el = row.select_one("a.gsc_a_ac")
        cite_text = cite_el.get_text(strip=True) if cite_el else ""
        publications[pub_id] = {
            "author_pub_id": pub_id,
            "num_citations": int(cite_text) if cite_text.isdigit() else 0,
            "bib": {"title": title_el.get_text(strip=True)},
        }

    return {
        "name": name_el.get_text(strip=True),
        "scholar_id": scholar_id,
        "citedby": citedby,
        "publications": publications,
        "updated": datetime.now(timezone.utc).isoformat(),
    }


def fetch_author(scholar_id: str, retries: int = 3, delay_seconds: float = 8.0) -> dict:
    url = PROFILE_URL.format(scholar_id=scholar_id)
    last_error = None
    for attempt in range(1, retries + 1):
        try:
            print(f"Fetching Google Scholar profile (attempt {attempt}/{retries})", file=sys.stderr)
            response = requests.get(url, headers=REQUEST_HEADERS, timeout=20)
            response.raise_for_status()
            lowered = response.text.lower()
            if "sorry/index" in response.url or "not a robot" in lowered:
                raise RuntimeError("Google Scholar served a captcha page")
            author = parse_profile(response.text, scholar_id)
            if not author.get("name"):
                raise RuntimeError("Google Scholar returned no author name")
            return author
        except Exception as error:
            last_error = error
            print(f"Attempt {attempt}/{retries} failed: {error}", file=sys.stderr)
            if attempt < retries:
                time.sleep(delay_seconds * attempt)
    raise RuntimeError(
        f"Failed to fetch Google Scholar data after {retries} attempts: {last_error}"
    ) from last_error


def write_results(author: dict) -> None:
    os.makedirs("results", exist_ok=True)
    with open("results/gs_data.json", "w", encoding="utf-8") as outfile:
        json.dump(author, outfile, ensure_ascii=False, indent=2)
    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(author.get("citedby", 0)),
    }
    with open("results/gs_data_shieldsio.json", "w", encoding="utf-8") as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False)


def main() -> None:
    scholar_id = require_scholar_id()
    author = fetch_author(scholar_id)
    write_results(author)
    print(json.dumps({"name": author.get("name"), "citedby": author.get("citedby")}, indent=2))


if __name__ == "__main__":
    main()
