# fennickaddons.dev

This folder is the whole site: static HTML, one style sheet, images and `data/compat.json`. There is no build step and one small script (`assets/ambient.js`, the optional marsh sound). Cloudflare Web Analytics counts page views. Cloudflare serves the folder as static assets (see `wrangler.jsonc` in the public repo).

- `_headers` sets the security headers on every response.
- `.assetsignore` keeps this README and other notes from being served.
- The donation section in `index.html` is commented out and stays hidden until I open donations.
- Downloads, the changelog and bug reports link to https://github.com/Dagodeiwos/fennick-releases.

`.dev` domains are HTTPS-only (HSTS preload).

## Parallax layers

The pages scroll inside `.px` with three layers (back art, the content, front edge art). It's CSS only. The art files and speeds are in the "Three-layer parallax" block at the end of `style.css`. The art files and their PNG fallbacks are listed in the `--px-*-art` and `--px-*-set` variables; when you change one, update its size in `tools/art_claims.json`:

- `back-map-tile`: far background map tile, repeats down the page (1600 wide, its `@2x` is 2304 wide and offered as 1.44x so it decodes to under 16 MB; fades into the page colour at its sides on wider screens).
- Edge strips: composed from pieces in `assets/parallax/edge/` (the `--edge-*` variables): `cap-top` (240x640, frames the banner), `seg-a` to `seg-d` (240x400 each, any segment must join any other), `cap-bottom` (240x560, marsh ground and water, lands on the window bottom at the page end). All 240 wide at 1x, PNG + WebP + @2x PNG/WebP. The right strip uses its own `-right` pieces (`cap-top-right` ... `cap-bottom-right`, the `--edge-*-right` variables); nothing is mirrored. `cap-bottom` ends in solid #2a1e14, the footer soil. The irregular left and right orders come from `tools/edge_sequence.py`. The old `edge-left` strip repeats underneath as a safety net.
- The home page banner is `assets/hero/hero-trailblazer` (phones: the 4:3 `hero-trailblazer-mobile`; its `@2x` WebP is 3264 wide, offered as 1.7x, to stay under 16 MB decoded) with the wordmark as HTML text (`.hero-title`, `.hero-tagline`).

## Marsh side critters

Wisps and some dragonflies sit beside the content at irregular heights (`.mx-anchor` > `.mx-slot` > `<picture>`), scrolling with the edge foliage. Their places come from `tools/wisp_placement.py` (seeded, so the same every run; run it with the site served locally after content changes): left and right are independent, at least 180px of content apart on each side, every section gets at least one, and each starts its loop at a random phase. Each section's anchor covers the section, and the offsets are clamped to it, so a shorter section never pushes its critters into the next one.

The art is one horizontal sprite sheet per critter in `assets/marsh/`, all frames side by side, no gaps, frame 1 at the left (that frame is the reduced-motion still):

- `wisp-sm` (40x40), `wisp` (64x64), `wisp-lg` (96x96): 8 frames each, 3.2 s a loop, used on both sides (the tool picks a size; the middle one twice as often).
- `dragonfly` / `dragonfly-right`: 4 frames of 96x64 (sheet 384x64), 0.5 s a loop.

Each comes as `.webp`, `@2x.webp`, `.png` and `@2x.png`. Frame size, frame count and loop length per critter are the `--mx-*` variables in the marsh block in `style.css`. If a sheet's size changes, update `SHEETS` in `tools/wisp_placement.py`, rerun it, and update `tools/art_claims.json`. The critters are hidden at 900px and below, and with reduced motion they show frame 1 only.

## Header animation

On wide screens the banner is a fox-free plate (`assets/hero/banner-plate`, 1920x672; its `@2x` WebP is 3264 wide, offered as 1.7x) and Fennick runs through the branches over it. Tablets and phones (900px and narrower) keep the Trailblazer art with Fennick in it and no header layers. Everything follows `branding/site-parallax/marsh2/final/README.md`. Layers in `.hdr`, back to front, files in `assets/header/`, positions in banner pixels:

| Layer | Art (1x) | Motion | Position |
|---|---|---|---|
| `hdr-stars-a` / `-b` | 537x672 each, static | cross-fade: a = .5 + .5 sin(2 pi 2t/8), b the inverse (same keyframes half a pass later) | x 20, y 0 |
| `hdr-branches-left` / `-right` (back canopy) | 953x517 / 958x506, static | sway: skewX(0.65 deg x sin(2 pi 2t/8)) hinged at the canopy top | canopy box 1920x760, 90px above the banner; x 0 / 962, y 1 |
| `hdr-trail` x3 | 64x64 spark, 8 frames, 8 passes per 10 s | follows Fennick's route 0.15 / 0.40 / 0.70 s late, 40px up and left of his paws, opacity .95 / .65 / .35 x his | above the back canopy, under the front |
| `hdr-fox` | 384x272 frames, 8, 12 passes per 10 s, drawn 1.8x big | the route (position, lean, size, layer, opacity) | paw point 192,266 in the frame |
| `hdr-branches-front-left` / `-right` (front canopy) | 861x474 / 900x506 (rev3: cut clear of the wordmark), static | same sway | same canopy box; x 0 / 1020, y 1 |

Each piece has `.webp`, `.png`, `@2x.webp` and `@2x.png`. Reduced motion: `hdr-stars-still` replaces the stars, the canopies stop, the sparks are hidden, and `hdr-fox-still` sits on the left bough at x 640. All header motion runs on one clock, `--hdr-cycle` (10 s; Artzy drew the route for 8 s, and since every keyframe is a percentage it just plays 1.25x slower); every loop ends where it starts.

Fennick's route is generated by `tools/hdr_fox_route.py` from `tools/data/hdr-fox-route.json` (Artzy's `final/header/hdr-fox-route.json`, copied unchanged): one keyframe per 1/24 s row with left/top (paw point), rotate, css_scale, opacity and z-index (`back` = 1, behind the back canopy; `mid`/`front` = 3, between the canopies; the switches are instant). The same file gives the three trail sparks (`hdr-trail-1..3` keyframes). To use a new route, copy the new JSON over that file and run the tool.

## Scroll cameos

`assets/cameo.js` lets Fennick slip through the side foliage now and then: one of three clips from `assets/cameo/` (`cameo-fox`, `-b`, `-c`; 24 frames of 240x240 in an 8x3 grid, 1920x720, 3.75 s (drawn for 3 s, slowed for a calmer pace), played once; first and last frames empty because he is behind the leaves) each with its own leaves (`cameo-leaves`, `cameo-fox-b-leaves`, `cameo-fox-c-leaves`, one 240x240 frame drawn in front of him). Drawn for the left strip (mirrored on the right). Each clip has `.webp`, `.png` and a 1.5x `@2x.webp` (2880x1080, to stay under 16 MB decoded). Only one Fennick at a time: cameos play only while the header is off screen, at most one per 15-20 s of scrolling, alternating sides, never at 900px and narrower, with reduced motion, or without JavaScript. The clips to use are the `VARIANTS` list at the top of `cameo.js`: with one name it always plays that one; with several it picks a random one that is never the one it just played.

## Marsh footer

Every page ends in a full-width marsh scene (`.ftr`), with the legal text on the soil band below the roots, on a soft dark backing (WCAG AA). Files in `assets/footer/`, positions in plate pixels:

| Layer | Frame (1x) | Frames | Passes per 7 s | Position in the plate |
|---|---|---|---|---|
| `ftr-plate` | 1920x640 | 1 (still) | - | the whole scene; soil from y 300 (the text goes there), `--ftr-soil` #2a1e14 |
| `ftr-water` | 1920x60 | 4 | 4 | top 236 |
| `ftr-fox` | 480x200 | 32 (8x4), 1x only | 1 | x 700, top 40: Fennick chasing a frog, behind the grass |
| `ftr-grass` | 1920x220 | 6 | 2 | top 20 (WebP only); delayed half a pass so frame 4 (closest to the still) shows at 0%. Always drawn: the plate has only a dark backdrop where the grass goes, so with reduced motion it shows `ftr-grass-still` instead |
| `ftr-insects` | 1180x260 | 8 | 2 | x 380, top 40; delayed 9/16 of a pass so the dragonfly is by the lily pad when the fox lands |

`ftr-plate` has a 1.7x `@2x.webp` (3264x1088). Phones (600px and narrower) draw the art at 1x, centred, with `ftr-plate-mobile` (Artzy's 1100x640 centre crop) as the plate. Each animated layer has a one-frame `-still` for reduced motion. The footer clock is `--ftr-cycle` (7 s; it was 4 s).

## Dropping in Artzy's follow-ups

All of these are file copies plus, at most, a few variables. After any of them run `python3 tools/anim_seam_check.py` and `python3 tools/art_qa.py`, and update the sizes in `tools/art_claims.json`.

1. **Footer fox (now 32 frames, 8x4, done in rev2).** For another frame count copy the new `ftr-fox.png`/`.webp` and `ftr-fox-still.*` into `assets/footer/` and set `--hdr-cols`, `--hdr-rows`, `--hdr-frames` on `.ftr-fox` in `style.css` (cols x rows = frames). The seam check reads these and checks them against the sheet. Optional: update the `width`/`height` attributes on the `ftr-fox` `<img>` in each page (only a layout hint).
2. **More cameo variants (b and c are in, rev2).** Copy `<name>.png`, `.webp`, `@2x.webp` (1.5x), and its `<name>-leaves.*` into `assets/cameo/`, same grid and size as `cameo-fox`, then add `{ clip: "<name>", leaves: "<name>-leaves" }` to `VARIANTS` at the top of `assets/cameo.js`. Nothing else.
3. **Grass or plate changes** (the rev2 doubling fix was a plate swap). Copy the new `ftr-plate*` / `ftr-grass*` files over the old ones. Same sizes, so no CSS change.
4. **Cameo leaves.** Copy the new `cameo-leaves.*` / `cameo-fox-b-leaves.*` / `cameo-fox-c-leaves.*` (240x240, `@2x` 480x480) over the old ones. No code change.

Every image must decode to under 16 MB (width x height x 4 bytes, e.g. 2048x2048); `anim_seam_check.py` checks this for every file in `assets/`.

## Checks for the animation

- `tools/anim_seam_check.py`: every loop ends where it starts, frame counts match the sheets, no fill-mode or positive delay, the header shares one clock, depth switches are instant, every image decodes to under 16 MB.
- `tools/click_through_check.py` (site served locally): no decoration blocks a link or button, on every page at 1440 and 390 wide, with a cameo running.
- `tools/footer_grass_check.py` (site served locally): the footer grass is loaded, opaque and on screen on every page, with motion (the sheet) and with reduced motion (`ftr-grass-still`), since the plate has no grass of its own.

## Ambient sound

`assets/ambient.js` adds the speaker button on the home banner. It's off by default, remembered in localStorage, never starts by itself for visitors who prefer reduced motion, and fetches no audio until it's turned on. A short fennec call plays once every 2 to 5 minutes while it's on; set `FOX_FILE` to `null` in `ambient.js` to switch that off. Sources and licenses: `AUDIO-SOURCES.md`.

## Footer date

The footer's "Last updated" line is written by `tools/stamp_updated.py` from the date of the newest commit that touched `site/` (month and year, for example "October 2026"). Run it, commit, then publish; `python3 tools/stamp_updated.py --check` is part of the site checks and fails if a page shows another month.
