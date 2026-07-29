/* TutorLedger — EN/PT toggle.
 *
 * English stays in the HTML and remains what Google indexes: no second set of
 * URLs, no hreflang, no extra page weight for visitors who never touch the
 * button. Portuguese lives in pt.json and is fetched only on demand.
 *
 * Two substitution modes, because one is not enough:
 *
 *   text   — exact match on a whole text node. Fine for labels and buttons.
 *   blocks — replaces an element's innerHTML wholesale, keyed by data-t.
 *            Prose needs this: a paragraph containing <strong> is several text
 *            nodes, so matching the sentence as one string never fires.
 *
 * Anything absent from the dictionary stays in English rather than breaking.
 */
(function () {
  "use strict";

  var KEY = "tl-lang";
  var DISMISS = "tl-lang-note-dismissed";
  var dict = null;
  var textBackup = new WeakMap();
  var attrBackup = new WeakMap();
  var blockBackup = new WeakMap();

  var ATTRS = ["placeholder", "aria-label", "title", "alt"];

  function walk(fn) {
    var w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        var p = n.parentNode;
        if (!p) return NodeFilter.FILTER_REJECT;
        var tag = p.nodeName;
        if (tag === "SCRIPT" || tag === "STYLE" || tag === "NOSCRIPT")
          return NodeFilter.FILTER_REJECT;
        if (p.closest && p.closest("[data-t]")) return NodeFilter.FILTER_REJECT;
        return n.nodeValue.trim() ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
      }
    });
    var n;
    while ((n = w.nextNode())) fn(n);
  }

  function toPT() {
    // blocks first — they remove whole subtrees from the text walker's reach
    document.querySelectorAll("[data-t]").forEach(function (el) {
      var html = dict.blocks && dict.blocks[el.dataset.t];
      if (!html) return;
      if (!blockBackup.has(el)) blockBackup.set(el, el.innerHTML);
      el.innerHTML = html;
      restoreMotion(el);
    });
    walk(function (n) {
      var t = n.nodeValue.trim();
      var hit = dict.text[t];
      if (!hit) return;
      if (!textBackup.has(n)) textBackup.set(n, n.nodeValue);
      n.nodeValue = n.nodeValue.replace(t, hit);
    });
    document.querySelectorAll("[" + ATTRS.join("],[") + "]").forEach(function (el) {
      ATTRS.forEach(function (a) {
        var v = el.getAttribute(a);
        if (!v || !dict.text[v.trim()]) return;
        var store = attrBackup.get(el) || {};
        if (!(a in store)) { store[a] = v; attrBackup.set(el, store); }
        el.setAttribute(a, dict.text[v.trim()]);
      });
    });
    if (window.tlCalcSetLang) window.tlCalcSetLang("pt", dict);
    notice(true);
    document.documentElement.lang = "pt-BR";
  }

  /* Freshly inserted markup carries .reveal / .rise, which start at opacity:0
     and depend on an IntersectionObserver to become visible. Re-observing them
     was not enough — content that is merely translated must never be able to
     end up invisible, and correctness should not hinge on an observer firing.
     So it is forced visible outright, with the inline style as a belt-and-braces
     guard in case the class is ever outranked in the cascade. Nothing is lost:
     re-animating a section the reader is already looking at adds nothing. */
  function restoreMotion(el) {
    var anim = el.querySelectorAll(".reveal, .rise");
    for (var i = 0; i < anim.length; i++) {
      anim[i].classList.add("in");
      anim[i].style.opacity = "1";
      anim[i].style.transform = "none";
      anim[i].style.transitionDelay = "0s";
    }
  }

  function toEN() {
    document.querySelectorAll("[data-t]").forEach(function (el) {
      if (!blockBackup.has(el)) return;
      el.innerHTML = blockBackup.get(el);
      restoreMotion(el);
    });
    walk(function (n) { if (textBackup.has(n)) n.nodeValue = textBackup.get(n); });
    document.querySelectorAll("[" + ATTRS.join("],[") + "]").forEach(function (el) {
      var store = attrBackup.get(el);
      if (store) Object.keys(store).forEach(function (a) { el.setAttribute(a, store[a]); });
    });
    if (window.tlCalcSetLang) window.tlCalcSetLang("en", dict);
    notice(false);
    document.documentElement.lang = "en";
  }

  /* An honest heads-up: the product itself — spreadsheet, guide, bonuses — is
     English only and the checkout is in dollars. Someone reading a Portuguese
     sales page has no way of knowing that until after they have paid.
     Dismissible, and it stays dismissed for the rest of the session. */
  function notice(show) {
    var el = document.getElementById("tl-lang-note");
    if (!show) { if (el) el.remove(); return; }
    if (el || sessionStorage.getItem(DISMISS) === "1") return;
    var head = document.querySelector(".site-head");
    if (!head) return;
    el = document.createElement("div");
    el.id = "tl-lang-note";
    el.setAttribute("role", "note");
    el.innerHTML =
      '<div class="wrap"><p>' + (dict.notice || "") + "</p>" +
      '<button type="button" class="close" aria-label="Fechar aviso">' +
      '<svg viewBox="0 0 20 20" width="15" height="15" aria-hidden="true">' +
      '<path d="M5 5l10 10M15 5L5 15" stroke="currentColor" stroke-width="2" ' +
      'stroke-linecap="round" fill="none"/></svg></button></div>';
    head.insertAdjacentElement("afterend", el);
    el.querySelector(".close").addEventListener("click", function () {
      sessionStorage.setItem(DISMISS, "1");
      el.style.height = el.offsetHeight + "px";
      requestAnimationFrame(function () { el.classList.add("gone"); });
      setTimeout(function () { el.remove(); }, 260);
    });
  }

  function setLang(lang) {
    if (lang === "pt" && !dict) {
      var href = document.querySelector('link[href*="tl.css"]').getAttribute("href");
      var base = href.replace(/assets\/tl\.css.*$/, "assets/");
      var page = document.body.dataset.ptPack;      // per-page pack, e.g. articles
      var jobs = [fetch(base + "pt.json").then(function (r) { return r.json(); })];
      if (page) jobs.push(fetch(page).then(function (r) { return r.json(); })
                               .catch(function () { return {}; }));
      Promise.all(jobs).then(function (parts) {
        dict = parts[0];
        dict.text = dict.text || {};
        dict.blocks = dict.blocks || {};
        if (parts[1]) {
          Object.assign(dict.text, parts[1].text || {});
          Object.assign(dict.blocks, parts[1].blocks || {});
          if (parts[1].notice) dict.notice = parts[1].notice;
        }
        toPT(); paint("pt");
      }).catch(function () { paint("en"); });
      return;
    }
    if (lang === "pt") toPT(); else toEN();
    paint(lang);
  }

  function paint(lang) {
    localStorage.setItem(KEY, lang);
    var b = document.getElementById("tl-lang-btn");
    if (!b) return;
    b.querySelectorAll("span").forEach(function (s) {
      s.classList.toggle("on", s.dataset.lang === lang);
    });
    b.setAttribute("aria-label", lang === "pt" ? "Switch to English" : "Mudar para português");
  }

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
