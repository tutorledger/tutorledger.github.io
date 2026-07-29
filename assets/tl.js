/* TutorLedger — shared behaviour. No dependencies. */
(function () {
  "use strict";

  // Scroll reveal. Deliberately subtle: 14px rise + fade, one-shot, and fully
  // disabled when the visitor asks for reduced motion. Anything heavier costs
  // us Core Web Vitals, and ranking is this site's only distribution channel.
  var reduced = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var supported = "IntersectionObserver" in window;
  var io = null;

  if (!reduced && supported) {
    io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add("in");
        io.unobserve(e.target);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.06 });
  }

  /* Exposed so it can be re-run over freshly inserted markup. The language
     toggle replaces whole sections, and those new nodes carry .reveal — which
     is opacity:0. Without re-observing them the section stays invisible
     forever, which looks exactly like a blank page. */
  function reveal(root) {
    var targets = (root || document).querySelectorAll(".reveal");
    if (!io) {
      for (var i = 0; i < targets.length; i++) targets[i].classList.add("in");
      return;
    }
    targets.forEach(function (el, idx) {
      if (el.classList.contains("in")) return;
      // already on screen when inserted? show it now rather than waiting
      var r = el.getBoundingClientRect();
      if (r.top < window.innerHeight && r.bottom > 0) {
        el.classList.add("in");
        return;
      }
      el.style.transitionDelay = (Math.min(idx % 4, 3) * 60) + "ms";
      io.observe(el);
    });
  }

  window.tlReveal = reveal;
  reveal(document);
})();
