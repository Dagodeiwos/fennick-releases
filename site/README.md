# fennickaddons.dev

This folder is the whole site: static HTML, one style sheet and images. There is no build step and the site has no scripts of its own. Cloudflare serves the folder as static assets (see `wrangler.jsonc` in the public repo).

- The homepage links to the versioned seven-module suite ZIP and its SHA-256 checksum. Market Advisor is coming soon.
- The header displays the original 1200 × 675 cinematic spirit fox at `assets/hero/spirit-fox-hero.webp`, with the wordmark underneath.
- Guidepost and its companion add-ons have development notes on the homepage. `_redirects` sends those old URLs home so bookmarks do not 404.
- `_headers` sets the security headers on every response, including a tight Content Security Policy that still allows Cloudflare Web Analytics.
- `.assetsignore` keeps this README and other notes from being served.
- The Support section shows the Ko-fi button only. The GitHub Sponsors button stays hidden.
- Bug reports link to https://github.com/Dagodeiwos/fennick-releases/issues.

`.dev` domains are HTTPS-only (HSTS preload).

## Branding assets

`assets/spirit-fox.svg` is the scalable emblem and favicon. `assets/spirit-icons.svg` contains nine reusable artifact symbols. `assets/og/spirit-social.svg` is the social card source. The Spirit artwork validation workflow generates PNG previews; these are not deployed automatically. Preserve the static site and existing security policy.
