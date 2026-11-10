(function () {
  "use strict";
  var input = document.getElementById("site-search");
  var list = document.getElementById("search-results");
  if (!input || !list) return;

  var MAX = 10;
  var items = null;      // loaded lazily from the search index
  var loading = null;
  var results = [];
  var active = -1;

  function norm(s) {
    return String(s || "").normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase();
  }

  function load() {
    if (!loading) {
      loading = fetch(input.dataset.index, { credentials: "same-origin" })
        .then(function (r) { if (!r.ok) throw new Error(String(r.status)); return r.json(); })
        .then(function (data) {
          items = data.map(function (it) {
            return { item: it, title: norm(it.title), alias: norm(it.alias) };
          });
          return items;
        });
      loading.catch(function () { loading = null; });
    }
    return loading;
  }

  function kindLabel(kind) { return kind === "voce" ? "Voce" : "Lezione"; }

  function search(q) {
    var needle = norm(q).trim();
    if (!needle || !items) return [];
    var starts = [], inside = [];
    items.forEach(function (x) {
      var hitTitle = x.title.indexOf(needle) !== -1;
      var hitAlias = x.alias.indexOf(needle) !== -1;
      if (!hitTitle && !hitAlias) return;
      (x.title.indexOf(needle) === 0 ? starts : inside).push(x.item);
    });
    return starts.concat(inside).slice(0, MAX);
  }

  function close() {
    list.hidden = true;
    list.innerHTML = "";
    input.setAttribute("aria-expanded", "false");
    input.removeAttribute("aria-activedescendant");
    active = -1;
    results = [];
  }

  function highlight(i) {
    var lis = list.querySelectorAll("[role='option']");
    lis.forEach(function (li, j) { li.setAttribute("aria-selected", j === i ? "true" : "false"); });
    active = i;
    if (lis[i]) {
      input.setAttribute("aria-activedescendant", lis[i].id);
      lis[i].scrollIntoView({ block: "nearest" });
    }
  }

  function go(item) {
    window.location.href = new URL(item.url, input.dataset.index).href;
  }

  function render(q) {
    results = search(q);
    list.innerHTML = "";
    if (!q.trim()) return close();
    if (!items) {
      var wait = document.createElement("li");
      wait.className = "sr-empty";
      wait.textContent = "Caricamento…";
      list.appendChild(wait);
    } else if (!results.length) {
      var none = document.createElement("li");
      none.className = "sr-empty";
      none.textContent = "Nessun risultato per “" + q.trim() + "”";
      list.appendChild(none);
    }
    results.forEach(function (it, i) {
      var li = document.createElement("li");
      li.id = "sr-" + i;
      li.setAttribute("role", "option");
      li.setAttribute("aria-selected", "false");
      var a = document.createElement("a");
      a.href = new URL(it.url, input.dataset.index).href;
      var t = document.createElement("span");
      t.textContent = it.title;
      var m = document.createElement("span");
      m.className = "sr-meta";
      m.textContent = kindLabel(it.kind) + (it.corso ? " · " + it.corso : "");
      a.appendChild(t);
      a.appendChild(m);
      a.addEventListener("mousedown", function (e) { e.preventDefault(); go(it); });
      li.appendChild(a);
      list.appendChild(li);
    });
    list.hidden = false;
    input.setAttribute("aria-expanded", "true");
    active = -1;
  }

  input.addEventListener("focus", function () { load(); });
  input.addEventListener("input", function () {
    load().then(function () { render(input.value); }, function () {
      list.hidden = false;
      list.innerHTML = "<li class='sr-empty'>Ricerca non disponibile</li>";
    });
    if (!input.value.trim()) close();
  });

  input.addEventListener("keydown", function (e) {
    var open = !list.hidden && results.length > 0;
    if (e.key === "ArrowDown" && open) {
      e.preventDefault();
      highlight((active + 1) % results.length);
    } else if (e.key === "ArrowUp" && open) {
      e.preventDefault();
      highlight(active <= 0 ? results.length - 1 : active - 1);
    } else if (e.key === "Enter") {
      if (open) {
        e.preventDefault();
        go(results[active >= 0 ? active : 0]);
      }
    } else if (e.key === "Escape") {
      if (input.value) input.value = "";
      close();
    }
  });

  input.addEventListener("blur", function () { setTimeout(close, 120); });

  document.addEventListener("keydown", function (e) {
    if (e.key !== "/" || e.ctrlKey || e.metaKey || e.altKey) return;
    var t = e.target;
    if (t && (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName))) return;
    e.preventDefault();
    input.focus();
    input.select();
  });
})();
