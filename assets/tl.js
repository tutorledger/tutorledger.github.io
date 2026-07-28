/* TutorLedger — shared behaviour. No dependencies. */
(function () {
  "use strict";

  // Scroll reveal. Deliberately subtle: 14px rise + fade, one-shot, and fully
  // disabled when the visitor asks for reduced motion. Anything heavier costs
  // us Core Web Vitals, and ranking is this site's only distribution channel.
  var reduced = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var targets = document.querySelectorAll(".reveal");

  if (reduced || !("IntersectionObserver" in window)) {
    for (var i = 0; i < targets.length; i++) targets[i].classList.add("in");
    return;
  }

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      e.target.classList.add("in");
      io.unobserve(e.target);
    });
  }, { rootMargin: "0px 0px -8% 0px", threshold: 0.06 });

  targets.forEach(function (el, idx) {
    // Stagger siblings slightly so a grid doesn't pop in as one block.
    el.style.transitionDelay = (Math.min(idx % 4, 3) * 60) + "ms";
    io.observe(el);
  });
})();
