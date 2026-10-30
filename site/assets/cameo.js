// Scroll cameos: now and then Fennick slips through the side foliage while you scroll.
//
// The rules I keep, and how:
// - Only one Fennick on screen. The header has its own animated Fennick, so a cameo only plays while the header
//   is out of view (an IntersectionObserver watches it), and the .cameo-on class hides the header fox meanwhile.
// - Rare: at most one cameo per 15-20 seconds of actual scrolling, alternating left and right.
// - Cheap: I never listen to the scroll event. IntersectionObservers tell me when the little critters at the
//   sides cross the window edge, which only happens while the page is scrolling, so each of their callbacks is
//   a sign of "scrolling now". Those callbacks just add up time; no layout is read there.
// - Edge layer only: the cameo goes inside the left or right edge strip, never over the text.
// - Nothing for visitors who prefer reduced motion, nothing at 900px and narrower (no edge strips there), and
//   nothing without JavaScript (the element is created here, so without this script it doesn't exist).
//
// Loaded with "defer", so the page's HTML is ready when this runs.

(function () {
  "use strict";

  var scroller = document.querySelector(".px");
  var strips = { left: document.querySelector(".px-left"), right: document.querySelector(".px-right") };
  if (!scroller || !strips.left || !strips.right || !window.IntersectionObserver) return;

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");
  var wide = window.matchMedia("(min-width: 901px)");

  // The cameo clips to rotate through: the ONE place to list them. Each entry is the clip (<clip>.png, .webp and a
  // 1.5x @2x.webp in assets/cameo/, the same 8 x 3 grid of 240x240 frames and length (3.75 s) as cameo-fox) and the
  // leaves drawn in front of it (<leaves>.png, .webp, @2x.webp). Add an entry only once its files are in the
  // folder. With one entry it is always that one; with more, a random one that is never the same as the last.
  var VARIANTS = [
    { clip: "cameo-fox",   leaves: "cameo-leaves" },
    { clip: "cameo-fox-b", leaves: "cameo-fox-b-leaves" },
    { clip: "cameo-fox-c", leaves: "cameo-fox-c-leaves" }
  ];
  var lastVariant = "";
  function pickVariant() {
    var options = VARIANTS.filter(function (v) { return v.clip !== lastVariant; });
    if (!options.length) options = VARIANTS;
    var pick = options[Math.floor(Math.random() * options.length)];
    lastVariant = pick.clip;
    return pick;
  }

  var CLIP_MS = 3750;                      // length of the clip (3.75 s, slowed from 3 s); matches --hdr-cycle on .cameo-clip in style.css
  var MIN_S = 15, MAX_S = 20;              // seconds of scrolling between two cameos
  var ACTIVE_GAP_MS = 1500;                // the most one gap between two scroll signals can count for

  var headerVisible = !!document.querySelector(".hdr");   // pages without the animated header start "out of view"
  var scrolledMs = 0, lastSignal = 0, needMs = nextWait(), side = Math.random() < 0.5 ? "left" : "right";
  var playing = false;

  function nextWait() { return (MIN_S + Math.random() * (MAX_S - MIN_S)) * 1000; }

  // 1. Is the header on screen? Watch the banner; rootMargin 0 means "any part of it inside the scroller".
  var header = document.querySelector(".hero-art");
  if (header) {
    new IntersectionObserver(function (entries) {
      headerVisible = entries[entries.length - 1].isIntersecting;
    }, { root: scroller }).observe(header);
  }

  // 2. Scroll activity: any critter or section crossing the window edge means the page is moving.
  var signals = new IntersectionObserver(function () {
    var now = performance.now();
    // Count the time since the previous signal, but at most ACTIVE_GAP_MS: a longer gap means the page probably
    // stood still for a while, and standing still shouldn't bring the next cameo closer.
    if (lastSignal) scrolledMs += Math.min(now - lastSignal, ACTIVE_GAP_MS);
    lastSignal = now;
    if (scrolledMs >= needMs) tryCameo();
  }, { root: scroller, threshold: [0, 0.25, 0.5, 0.75, 1] });   // more steps = more frequent signals
  document.querySelectorAll(".mx-slot, main.panel > section, .ftr").forEach(function (el) { signals.observe(el); });

  // 3. Play one: put the clip into the chosen strip at a random height inside the window.
  function tryCameo(force) {
    if (playing || (!force && (headerVisible || reduce.matches || !wide.matches))) return false;
    if (strips[side].offsetWidth < 40) return false;      // the margin beside the text is too narrow for him
    playing = true; scrolledMs = 0; needMs = nextWait();

    // The edge strips move faster than the page (their scale, --px-front-scale, sets how much), so a point that
    // should appear at height v in the window sits at v + scrollTop / scale inside the strip.
    var scale = parseFloat(getComputedStyle(document.documentElement).getPropertyValue("--px-front-scale")) || 1;
    var v = scroller.clientHeight * (0.2 + Math.random() * 0.45);
    var el = document.createElement("div");
    el.className = "cameo";
    el.setAttribute("aria-hidden", "true");
    el.style.top = Math.round(v + scroller.scrollTop / scale) + "px";
    var v = pickVariant(), clip = "/assets/cameo/" + v.clip, leaves = "/assets/cameo/" + v.leaves;
    // The @2x clip is 1.5x (2880 wide) to stay under 16 MB decoded, so it is offered as 1.5x.
    el.innerHTML =
      '<div class="cameo-clip"><picture><source type="image/webp" srcset="' + clip + '.webp 1x, ' + clip + '@2x.webp 1.5x">' +
      '<img src="' + clip + '.png" alt=""></picture></div>' +
      '<picture><source type="image/webp" srcset="' + leaves + '.webp 1x, ' + leaves + '@2x.webp 2x">' +
      '<img class="cameo-leaves" src="' + leaves + '.png" alt=""></picture>';
    strips[side].appendChild(el);
    scroller.classList.add("cameo-on");

    // Clean up when the clip is over (its last frame is empty, he's behind the leaves, so removing it is invisible).
    setTimeout(function () {
      el.remove();
      scroller.classList.remove("cameo-on");
      playing = false;
    }, CLIP_MS + 100);
    side = side === "left" ? "right" : "left";
    return true;
  }

  // For the automated click-through check: play one now, whatever the timer says.
  window.fennickCameo = function () { return tryCameo(true); };
  window.fennickCameo.state = function () { return { headerVisible: headerVisible, scrolledMs: scrolledMs, needMs: needMs, playing: playing, variant: lastVariant, variants: VARIANTS.map(function (v) { return v.clip; }) }; };
})();
