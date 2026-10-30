# fennickaddons.dev

This folder is the whole site: static HTML, one style sheet, images and `data/compat.json`. There is no build step, no script and no tracking. Cloudflare serves the folder as static assets (see `wrangler.jsonc` in the public repo).

- `_headers` sets the security headers on every response.
- `.assetsignore` keeps this README and other notes from being served.
- The donation section in `index.html` is commented out and stays hidden until I open donations.
- Downloads, the changelog and bug reports link to https://github.com/Dagodeiwos/fennick-releases.

`.dev` domains are HTTPS-only (HSTS preload).
