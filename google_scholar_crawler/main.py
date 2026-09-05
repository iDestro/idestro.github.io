from scholarly import scholarly
import json
from datetime import datetime, timezone
import os
import sys
import time


def require_scholar_id() -> str:
    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", "").strip()
    if not scholar_id:
        raise SystemExit("GOOGLE_SCHOLAR_ID is missing or empty")
    return scholar_id


def fetch_author(scholar_id: str, retries: int = 3, delay_seconds: float = 8.0) -> dict:
    last_error = None
    for attempt in range(1, retries + 1):
        try:
            author = scholarly.search_author_id(scholar_id)
            scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
            if not author.get("name"):
                raise RuntimeError("Google Scholar returned no author name")
            publications = author.get("publications") or []
            author["publications"] = {
                item["author_pub_id"]: item
                for item in publications
                if item.get("author_pub_id")
            }
            author["citedby"] = author.get("citedby", 0)
            author["updated"] = datetime.now(timezone.utc).isoformat()
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
