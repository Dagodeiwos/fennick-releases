# fennickaddons.dev landing page

Static files only (`index.html`, `style.css`). No build step, no scripts, no tracking.

**Before publishing:** the Ko-fi (`https://ko-fi.com/J5M529GC4X`) and GitHub Sponsors (`https://github.com/sponsors/Dagodeiwos`) buttons in `index.html` are placeholders until the author creates the accounts. Downloads, changelog and bug reports point at the public repo Dagodeiwos/fennick-releases.

**The repo is private.** That matters for two things:
- Free GitHub Pages does **not** publish from a private repo. It needs a paid plan (GitHub Pro, Team or Enterprise), or the repo must be public.
- The page's download, changelog and bug-report links point at this repo. Visitors who aren't collaborators get a 404 until the repo is public. Make it public (or move the releases to a public repo) before launch.

## Option A (recommended while private): Cloudflare Pages, free
1. Create a free Cloudflare account and add the domain `fennickaddons.dev` (Cloudflare shows two nameservers).
2. At the domain registrar, replace the nameservers with Cloudflare's two. Wait until Cloudflare says the domain is active (minutes to 24 h). Note: if the Fennick email already runs on this domain, copy its MX/TXT records into Cloudflare DNS first, or mail will stop.
3. Cloudflare dashboard → Workers & Pages → Create → Pages → Connect to Git → authorize GitHub and pick `Dagodeiwos/fennick-addons` (private is fine).
4. Build settings: framework **None**, build command **empty**, output directory **`site`**. Deploy.
5. Pages project → Custom domains → add `fennickaddons.dev` (and `www.fennickaddons.dev`). Cloudflare creates the DNS records and HTTPS certificate.

## Option B: GitHub Pages (needs a public repo or a paid plan)
1. Repo Settings → Pages → Source: GitHub Actions (or "Deploy from a branch" if the files are moved to `/docs`). A Pages workflow that uploads `site/` can be added on request.
2. Custom domain: `fennickaddons.dev`, then tick **Enforce HTTPS**.
3. At the DNS provider: four `A` records for `@` → 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153 (optional `AAAA` 2606:50c0:8000::153 … 8003::153), and a `CNAME` for `www` → `dagodeiwos.github.io`.
4. Optional: verify the domain under GitHub account Settings → Pages to prevent takeover.

`.dev` domains are HTTPS-only (HSTS preload), so the site won't load until the certificate is issued.
