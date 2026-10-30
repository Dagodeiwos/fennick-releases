// Ambient marsh sound for the home page.
//
// What it does: a quiet marsh loop (frogs and crickets) plus, once every few minutes, a short fennec fox call. It is OFF unless
// the visitor turns it on with the speaker button on the banner. I remember the choice in localStorage so it
// stays on (or off) on the next visit.
//
// A few rules I follow here, and why:
// - Nothing is downloaded until the sound is actually turned on. I create the <audio> objects only then, with
//   preload "none", so a visitor who never clicks never downloads a single byte of audio.
// - If the visitor prefers reduced motion (an operating system setting), I never start the sound by myself, even
//   if it was left on last time. It only plays after they click the button again during this visit.
// - When the tab is hidden I fade the sound out and pause it; when the tab comes back I fade it in again.
// - Volume changes are faded over about a second and a half so the sound never starts or stops abruptly.
//
// The script is loaded with "defer", which means the browser runs it after the page's HTML has been read, so
// the button already exists when this code looks for it.

(function () {
  "use strict";

  var STORAGE_KEY = "fennick-ambient";   // localStorage key; the value is "on" or "off"
  var VOLUME = 0.25;                      // target loudness, from 0 (silent) to 1 (full)
  var FADE_MS = 1500;                     // fade length in milliseconds
  // The rare fox call. FOX_FILE is the file name in /assets/audio/ without its extension (I ship .ogg and .mp3).
  // To turn the call off, set FOX_FILE to null: then nothing is ever scheduled or downloaded. To use a different
  // recording, drop its .ogg and .mp3 in /assets/audio/ and put its name here (and list it in AUDIO-SOURCES.md).
  // If the file turns out to be missing, the "error" handler below switches the call off quietly.
  var FOX_FILE = "fox-call";
  var FOX_MIN_S = 120, FOX_MAX_S = 300;   // one call every 2 to 5 minutes, at random
  var FOX_VOLUME = VOLUME * 0.6;          // quieter than the loop: it's meant to sound far away
  var FOX_FADE_MS = 250;                  // a short fade in, so the call doesn't start with a click

  var button = document.querySelector(".amb-toggle");
  if (!button) return;                    // a page without the button: nothing to do

  // Pick a format the browser can play. Opus in an Ogg file is smaller; MP3 is the fallback (older Safari).
  var probe = document.createElement("audio");
  var ext = probe.canPlayType('audio/ogg; codecs="opus"') ? "ogg" : "mp3";

  var loop = null;        // the marsh loop, created on first use
  var fox = null;         // the fox call, created on first use
  var foxTimer = null;    // id of the pending fox call, so I can cancel it
  var isOn = false;       // what the visitor wants right now

  // localStorage can throw (private modes, blocked storage), so I wrap both reads and writes.
  function load() { try { return localStorage.getItem(STORAGE_KEY); } catch (e) { return null; } }
  function save(v) { try { localStorage.setItem(STORAGE_KEY, v); } catch (e) { /* not saved; that's fine */ } }

  // Make an <audio> object that downloads nothing until play() is called.
  function makeAudio(name, loops) {
    var a = new Audio();
    a.preload = "none";
    a.loop = loops;
    a.volume = 0;
    a.src = "/assets/audio/" + name + "." + ext;
    return a;
  }

  // Fade an audio element's volume to "target" over FADE_MS (or "ms"). A timer runs "step" every 40 ms, and each
  // step sets the volume for how far along the fade we are. I use a timer rather than requestAnimationFrame
  // because the browser only calls the latter when it draws a new frame, which on a still page (reduced motion)
  // may be rarely. A newer fade on the same element cancels the older one.
  function fade(a, target, done) { fadeTo(a, target, FADE_MS, done); }
  function fadeTo(a, target, ms, done) {
    var start = a.volume, t0 = performance.now();
    clearInterval(a._fadeTimer);
    a._fadeTimer = setInterval(function () {
      var k = Math.min(1, (performance.now() - t0) / ms);
      a.volume = start + (target - start) * k;
      if (k >= 1) { clearInterval(a._fadeTimer); if (done) done(); }
    }, 40);
  }

  // Background tabs slow timers down to about once a second, so when the tab is already hidden I skip the fade
  // and pause straight away.
  function fadeOutAndPause(a) {
    if (!a) return;
    if (document.hidden) { clearInterval(a._fadeTimer); a.volume = 0; a.pause(); return; }
    fade(a, 0, function () { a.pause(); });
  }

  function scheduleFox() {
    clearTimeout(foxTimer);
    if (!FOX_FILE) return;                           // no fox file configured: the call is switched off
    var seconds = FOX_MIN_S + Math.random() * (FOX_MAX_S - FOX_MIN_S);
    foxTimer = setTimeout(function () {
      if (!isOn || document.hidden) return;          // it will be rescheduled when the sound resumes
      if (!fox) {
        fox = makeAudio(FOX_FILE, false);
        // A missing or broken file: switch the call off for this visit instead of retrying or showing errors.
        fox.addEventListener("error", function () { FOX_FILE = null; clearTimeout(foxTimer); });
      }
      clearInterval(fox._fadeTimer);                 // stop any fade still running on it
      fox.currentTime = 0;
      fox.volume = 0;
      fox.play().then(function () { fadeTo(fox, FOX_VOLUME, FOX_FADE_MS); }).catch(function () {});
      scheduleFox();
    }, seconds * 1000);
  }

  // Start (or resume) the sound. play() returns a promise; it fails if the browser blocks sound before the visitor
  // has clicked anything (autoplay rules). Then I wait for their first click or key press and try again.
  function start() {
    if (!loop) loop = makeAudio("marsh-loop", true);
    loop.play().then(function () {
      fade(loop, VOLUME);
      scheduleFox();
    }).catch(function () {
      function retry() {
        document.removeEventListener("pointerdown", retry);
        document.removeEventListener("keydown", retry);
        if (isOn && !document.hidden) start();
      }
      document.addEventListener("pointerdown", retry);
      document.addEventListener("keydown", retry);
    });
  }

  function stop() {
    clearTimeout(foxTimer);
    fadeOutAndPause(loop);
    fadeOutAndPause(fox);
  }

  // Keep the button's state in step: aria-pressed tells screen readers whether it's on, the label says what it is.
  function render() {
    button.setAttribute("aria-pressed", isOn ? "true" : "false");
    button.title = isOn ? "Marsh sounds: on" : "Marsh sounds: off";
  }

  button.addEventListener("click", function () {
    isOn = !isOn;
    save(isOn ? "on" : "off");
    render();
    if (isOn) start(); else stop();
  });

  document.addEventListener("visibilitychange", function () {
    if (!isOn) return;
    if (document.hidden) stop(); else start();
  });

  // First load: turn on only if it was left on AND the visitor doesn't prefer reduced motion.
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  isOn = load() === "on" && !reduce;
  render();
  button.hidden = false;                 // JavaScript is running, so the button can work: show it
  if (isOn) start();
})();
