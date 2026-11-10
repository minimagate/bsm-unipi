(function () {
  function renderMath() {
    if (typeof katex === "undefined") return;
    document.querySelectorAll(".math[data-tex]").forEach(function (el) {
      try {
        katex.render(el.dataset.tex, el, {
          displayMode: el.classList.contains("display"),
          throwOnError: false
        });
      } catch (e) {
        /* leave the raw TeX visible if KaTeX fails */
      }
    });
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", renderMath);
  } else {
    renderMath();
  }
})();
