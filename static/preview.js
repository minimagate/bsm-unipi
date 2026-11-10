(function () {
  "use strict";
  // Hover previews for links to voci: a small card with the categoria and the lead sentence.
  var fine = window.matchMedia && window.matchMedia("(hover: hover) and (pointer: fine)").matches;
  if (!fine || !window.fetch || !window.DOMParser) return;

  var VOCE_RE = /\/voci\/[^\/]+\/?$/;
  var DELAY = 300;
  var cache = {};
  var card = null;
  var timer = null;
  var current = null;

  function isVoceLink(a) {
    if (!a || !a.href || a.origin !== window.location.origin) return false;
    if (a.closest(".preview-card")) return false;
    return VOCE_RE.test(a.pathname);
  }

  function load(url) {
    if (!cache[url]) {
      cache[url] = fetch(url, { credentials: "same-origin" })
        .then(function (r) { if (!r.ok) throw new Error(String(r.status)); return r.text(); })
        .then(function (html) {
          var doc = new DOMParser().parseFromString(html, "text/html");
          var title = doc.querySelector("h1");
          var cat = doc.querySelector(".ib-categoria");
          var lead = doc.querySelector(".voce-body > p");
          return {
            title: title ? title.textContent : "",
            categoria: cat ? cat.textContent.trim() : "",
            leadHtml: lead ? lead.innerHTML : ""
          };
        });
      cache[url].catch(function () { delete cache[url]; });
    }
    return cache[url];
  }

  function ensureCard() {
    if (!card) {
      card = document.createElement("div");
      card.className = "preview-card";
      card.setAttribute("role", "tooltip");
      card.setAttribute("aria-hidden", "true");
      document.body.appendChild(card);
    }
    return card;
  }

  function renderMath(el) {
    if (typeof katex === "undefined") return;
    el.querySelectorAll(".math[data-tex]").forEach(function (m) {
      try {
        katex.render(m.dataset.tex, m, { displayMode: m.classList.contains("display"), throwOnError: false });
      } catch (e) { /* keep the raw TeX */ }
    });
  }

  function position(a) {
    var c = ensureCard();
    var r = a.getBoundingClientRect();
    var w = c.offsetWidth;
    var h = c.offsetHeight;
    var left = Math.min(Math.max(8, r.left), window.innerWidth - w - 8);
    var top = r.bottom + 8;
    if (top + h > window.innerHeight - 8) top = Math.max(8, r.top - h - 8);
    c.style.left = left + "px";
    c.style.top = top + "px";
  }

  function show(a) {
    var url = a.href;
    load(url).then(function (data) {
      if (current !== a) return;
      var c = ensureCard();
      c.innerHTML = "";
      var t = document.createElement("p");
      t.className = "pv-title";
      t.textContent = data.title || a.textContent;
      c.appendChild(t);
      if (data.categoria) {
        var k = document.createElement("p");
        k.className = "pv-cat";
        k.textContent = data.categoria;
        c.appendChild(k);
      }
      if (data.leadHtml) {
        var p = document.createElement("p");
        p.innerHTML = data.leadHtml;
        c.appendChild(p);
        renderMath(p);
      }
      c.setAttribute("aria-hidden", "false");
      position(a);
      c.classList.add("is-visible");
    }).catch(function () { /* no preview: the link still works */ });
  }

  function hide() {
    clearTimeout(timer);
    current = null;
    if (card) {
      card.classList.remove("is-visible");
      card.setAttribute("aria-hidden", "true");
    }
  }

  document.addEventListener("mouseover", function (e) {
    var a = e.target.closest && e.target.closest("a[href]");
    if (!isVoceLink(a) || a === current) return;
    hide();
    current = a;
    timer = setTimeout(function () { show(a); }, DELAY);
  });

  document.addEventListener("mouseout", function (e) {
    var a = e.target.closest && e.target.closest("a[href]");
    if (a && a === current && !a.contains(e.relatedTarget)) hide();
  });

  window.addEventListener("scroll", hide, { passive: true });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") hide(); });
})();
