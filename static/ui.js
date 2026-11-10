(function () {
  "use strict";
  var root = document.documentElement;
  var STORAGE_KEY = "bsm-theme";

  function systemTheme() {
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function currentTheme() {
    var explicit = root.getAttribute("data-theme");
    return explicit === "light" || explicit === "dark" ? explicit : systemTheme();
  }

  function setTheme(theme) {
    root.setAttribute("data-theme", theme);
    try { localStorage.setItem(STORAGE_KEY, theme); } catch (e) { /* private mode: the choice lasts for this page only */ }
  }

  function initTheme() {
    var btn = document.querySelector(".theme-toggle");
    if (!btn) return;
    btn.addEventListener("click", function () {
      setTheme(currentTheme() === "dark" ? "light" : "dark");
    });
  }

  function initNav() {
    var toggle = document.querySelector(".nav-toggle");
    var sidebar = document.getElementById("sidebar");
    var backdrop = document.querySelector(".nav-backdrop");
    if (!toggle || !sidebar) return;

    function setOpen(open) {
      root.classList.toggle("nav-open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Chiudi la navigazione" : "Apri la navigazione");
    }

    toggle.addEventListener("click", function () {
      setOpen(!root.classList.contains("nav-open"));
    });
    if (backdrop) backdrop.addEventListener("click", function () { setOpen(false); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && root.classList.contains("nav-open")) {
        setOpen(false);
        toggle.focus();
      }
    });
    sidebar.addEventListener("click", function (e) {
      if (e.target.closest && e.target.closest("a")) setOpen(false);
    });
    var wide = window.matchMedia("(min-width: 1000px)");
    var onWide = function (e) { if (e.matches) setOpen(false); };
    if (wide.addEventListener) wide.addEventListener("change", onWide);
  }

  // Highlights the heading the reader is in, in the desktop table of contents.
  function initToc() {
    var links = document.querySelectorAll(".toc-desktop a[href^='#']");
    if (!links.length || !("IntersectionObserver" in window)) return;

    var linkById = {};
    var headings = [];
    links.forEach(function (a) {
      var id = decodeURIComponent(a.getAttribute("href").slice(1));
      var el = document.getElementById(id);
      if (el) {
        linkById[id] = a;
        headings.push(el);
      }
    });
    if (!headings.length) return;

    var inBand = {};
    var active = null;

    function setActive(id) {
      if (id === active) return;
      if (active && linkById[active]) {
        linkById[active].classList.remove("is-active");
        linkById[active].removeAttribute("aria-current");
      }
      active = id;
      if (linkById[id]) {
        linkById[id].classList.add("is-active");
        linkById[id].setAttribute("aria-current", "location");
      }
    }

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) { inBand[entry.target.id] = entry.isIntersecting; });
      // The topmost heading inside the reading band wins.
      for (var i = 0; i < headings.length; i++) {
        if (inBand[headings[i].id]) { setActive(headings[i].id); return; }
      }
    }, { rootMargin: "0px 0px -70% 0px", threshold: 0 });

    headings.forEach(function (h) { observer.observe(h); });
    if (headings.length) setActive(headings[0].id);
  }

  function ready(fn) {
    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", fn);
    else fn();
  }

  ready(function () {
    initTheme();
    initNav();
    initToc();
  });
})();
