# fennickaddons.dev

This folder is the whole site: static HTML, one style sheet, images and `data/compat.json`. There is no build step, no script and no tracking. Cloudflare serves the folder as static assets (see `wrangler.jsonc` in the public repo).

- `_headers` sets the security headers on every response.
- `.assetsignore` keeps this README and other notes from being served.
- The donation section in `index.html` is commented out and stays hidden until I open donations.
- Downloads, the changelog and bug reports link to https://github.com/Dagodeiwos/fennick-releases.

`.dev` domains are HTTPS-only (HSTS preload).

## Parallax layers

The pages scroll inside `.px` with three layers (back art, the content, front edge art). It's CSS only (no scripts, the CSP stays `script-src 'none'`). The art files and speeds are in the "Three-layer parallax" block at the end of `style.css`. The art files and their PNG fallbacks are listed in the `--px-*-art` and `--px-*-set` variables; when you change one, update its size in `tools/art_claims.json`:

- `back-map-tile`: far background map tile, repeats down the page (1600 wide; fades into the page colour at its sides on wider screens).
- `edge-left`: left edge strip, mirrored for the right (240 wide, repeats down).
- `fox-peek`: Fennick peeking out of the left edge (the `<img class="px-fox">` in each page).
- The home page banner is `assets/hero/hero-trailblazer` (phones: the 4:3 `hero-trailblazer-mobile`) with the wordmark as HTML text (`.hero-title`, `.hero-tagline`).
