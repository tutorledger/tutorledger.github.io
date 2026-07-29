/* TutorLedger — EN/PT toggle.
 *
 * English stays in the HTML and remains what Google indexes: no duplicate URLs,
 * no hreflang, no extra page weight for the ~99% of visitors who never touch
 * the button. Portuguese lives in pt.json and is fetched only on demand.
 *
 * Translation works by walking text nodes and looking up the exact trimmed
 * string, so no markup changes are needed anywhere. Anything missing from the
 * dictionary simply stays in English rather than breaking.
 */
(function () {
  "use strict";

  var KEY = "tl-lang";
  var dict = null;
  var original = new WeakMap();   // node -> its English text, so EN is restorable
  var originalAttr = new WeakMap();

  var ATTRS = ["placeholder", "aria-label", "title", "content", "alt"];

  function walk(fn) {
    var w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        var p = n.parentNode;
        if (!p) return NodeFilter.FILTER_REJECT;
        var tag = p.nodeName;
        if (tag === "SCRIPT" || tag === "STYLE" || tag === "NOSCRIPT")
          return NodeFilter.FILTER_REJECT;
        return n.nodeValue.trim() ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
      }
    });
    var n;
    while ((n = w.nextNode())) fn(n);
  }

  function toPT() {
    walk(function (n) {
      var t = n.nodeValue.trim();
      var hit = dict.text[t];
      if (!hit) return;
      if (!original.has(n)) original.set(n, n.nodeValue);
      n.nodeValue = n.nodeValue.replace(t, hit);
    });
    document.querySelectorAll("[" + ATTRS.join("],[") + "]").forEach(function (el) {
      ATTRS.forEach(function (a) {
        var v = el.getAttribute(a);
        if (!v) return;
        var hit = dict.text[v.trim()];
        if (!hit) return;
        var store = originalAttr.get(el) || {};
        if (!(a in store)) { store[a] = v; originalAttr.set(el, store); }
        el.setAttribute(a, hit);
      });
    });
    banner(true);
    document.documentElement.lang = "pt-BR";
  }

  function toEN() {
    walk(function (n) {
      if (original.has(n)) n.nodeValue = original.get(n);
    });
    document.querySelectorAll("[" + ATTRS.join("],[") + "]").forEach(function (el) {
      var store = originalAttr.get(el);
      if (!store) return;
      Object.keys(store).forEach(function (a) { el.setAttribute(a, store[a]); });
    });
    banner(false);
    document.documentElement.lang = "en";
  }

  /* An honest notice. The product itself — spreadsheet, guide, bonuses — is
     English only, and someone reading a Portuguese sales page has no way of
     knowing that until after they have paid. */
  function banner(show) {
    var el = document.getElementById("tl-lang-note");
    if (!show) { if (el) el.remove(); return; }
    if (el) return;
    var head = document.querySelector(".site-head");
    if (!head) return;
    el = document.createElement("div");
    el.id = "tl-lang-note";
    el.setAttribute("role", "note");
    el.innerHTML = '<div class="wrap">' + (dict.notice || "") + "</div>";
    head.insertAdjacentElement("afterend", el);
  }

  function setLang(lang) {
    if (lang === "pt") {
      if (!dict) {
        var base = document.querySelector('link[href*="tl.css"]').getAttribute("href")
                     .replace(/assets\/tl\.css.*$/, "assets/pt.json");
        fetch(base).then(function (r) { return r.json(); }).then(function (j) {
          dict = j; toPT(); paint("pt");
        }).catch(function () { paint("en"); });
        return;
      }
      toPT();
    } else {
      toEN();
    }
    paint(lang);
  }

  function paint(lang) {
    localStorage.setItem(KEY, lang);
    var b = document.getElementById("tl-lang-btn");
    if (!b) return;
    b.querySelectorAll("span").forEach(function (s) {
      s.classList.toggle("on", s.dataset.lang === lang);
    });
    b.setAttribute("aria-label", lang === "pt" ? "Mudar para inglês" : "Switch to Portuguese");
  }

  // ---- build the control ------------------------------------------------
  var nav = document.querySelector(".site-head .nav");
  if (!nav) return;
  var btn = document.createElement("button");
  btn.id = "tl-lang-btn";
  btn.type = "button";
  btn.className = "langtoggle";
  btn.innerHTML = '<span data-lang="en" class="on">EN</span><span data-lang="pt">PT</span>';
  var spacer = nav.querySelector(".nav-spacer");
  if (spacer) spacer.insertAdjacentElement("afterend", btn);
  else nav.appendChild(btn);

  btn.addEventListener("click", function () {
    setLang(localStorage.getItem(KEY) === "pt" ? "en" : "pt");
  });

  if (localStorage.getItem(KEY) === "pt") setLang("pt");
})();
