# fennickaddons.dev

This folder is the whole site: static HTML, one style sheet and images. There is no build step and the site has no scripts of its own. Cloudflare serves the folder as static assets (see `wrangler.jsonc` in the public repo).

- The homepage features Market Advisor as Coming soon. There is no download button or link.
- The header uses the Trailblazer banner (Fennick painted on the art, plus an HTML wordmark). There is no animated header fox.
- The other add-on pages are off the site for now. `_redirects` sends those old URLs home so bookmarks do not 404.
- `_headers` sets the security headers on every response, including a tight Content Security Policy that still allows Cloudflare Web Analytics.
- `.assetsignore` keeps this README and other notes from being served.
- The Support section shows the Ko-fi button only. The GitHub Sponsors button stays hidden.
- Bug reports link to https://github.com/Dagodeiwos/fennick-releases/issues.

`.dev` domains are HTTPS-only (HSTS preload).
