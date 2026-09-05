(function () {
  function currentLang() {
    return document.documentElement.lang === "zh" ? "zh" : "en";
  }

  function syncButtons(lang) {
    var buttons = document.querySelectorAll(".lang-switch [data-lang]");
    for (var i = 0; i < buttons.length; i++) {
      var on = buttons[i].getAttribute("data-lang") === lang;
      buttons[i].setAttribute("aria-pressed", on ? "true" : "false");
    }
  }

  function setLang(lang) {
    if (lang !== "zh" && lang !== "en") {
      lang = "en";
    }
    document.documentElement.lang = lang;
    try {
      window.localStorage.setItem("site-lang", lang);
    } catch (e) {}
    try {
      var url = new URL(window.location.href);
      url.searchParams.set("lang", lang);
      window.history.replaceState(null, "", url);
    } catch (e) {}
    syncButtons(lang);
  }

  document.addEventListener("DOMContentLoaded", function () {
    syncButtons(currentLang());
    var root = document.querySelector(".lang-switch");
    if (!root) {
      return;
    }
    root.addEventListener("click", function (event) {
      var target = event.target;
      while (target && target !== root) {
        if (target.getAttribute && target.getAttribute("data-lang")) {
          setLang(target.getAttribute("data-lang"));
          return;
        }
        target = target.parentNode;
      }
    });
  });
})();
