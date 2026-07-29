/* TutorLedger blog — reading progress, table-of-contents highlighting, reveal.
   No dependencies. Every effect is either functional or a short fade; nothing
   here moves for the sake of moving. */
(function () {
  "use strict";
  var reduced = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // ---- reading progress -----------------------------------------------
  var bar = document.querySelector(".progress");
  var article = document.querySelector("article.post");
  if (bar && article) {
    var tick = function () {
      var box = article.getBoundingClientRect();
      var total = box.height - window.innerHeight;
      var done = total > 0 ? Math.min(1, Math.max(0, -box.top / total)) : 0;
      bar.style.width = (done * 100).toFixed(2) + "%";
    };
    addEventListener("scroll", tick, { passive: true });
    addEventListener("resize", tick);
    tick();
  }

  // ---- table of contents ----------------------------------------------
  var links = [].slice.call(document.querySelectorAll(".toc a[href^='#']"));
  if (links.length) {
    var heads = links.map(function (a) { return document.getElementById(a.hash.slice(1)); })
                     .filter(Boolean);
    var mark = function () {
      // the heading whose top has most recently passed a quarter of the viewport
      var cut = window.innerHeight * 0.25, current = heads[0];
      heads.forEach(function (h) { if (h.getBoundingClientRect().top <= cut) current = h; });
      links.forEach(function (a) { a.classList.toggle("on", a.hash === "#" + current.id); });
    };
    addEventListener("scroll", mark, { passive: true });
    mark();
  }

  // ---- reveal ----------------------------------------------------------
  // Exposed as window.tlRise so it can be re-run over markup inserted later —
  // the language toggle replaces whole blocks, and .rise starts at opacity:0.
  var io = null;
  if (!reduced && "IntersectionObserver" in window) {
    io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add("in");
        io.unobserve(e.target);
      });
    }, { rootMargin: "0px 0px -6% 0px", threshold: 0.05 });
  }

  function rise(root) {
    var targets = (root || document).querySelectorAll(".rise");
    if (!io) {
      [].forEach.call(targets, function (el) { el.classList.add("in"); });
      return;
    }
    [].forEach.call(targets, function (el, i) {
      if (el.classList.contains("in")) return;
      var r = el.getBoundingClientRect();
      if (r.top < window.innerHeight && r.bottom > 0) { el.classList.add("in"); return; }
      el.style.transitionDelay = (Math.min(i % 5, 4) * 55) + "ms";
      io.observe(el);
    });
  }

  window.tlRise = rise;
  rise(document);
})();
