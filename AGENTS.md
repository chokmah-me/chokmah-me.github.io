# AGENTS.md — chokmah-me.github.io

Public site for Chokmah LLC. Live at chokmah.me. Vanilla HTML/CSS (Tailwind via CDN). GitHub Pages deploys from `main`.

## Commands

No build step.

```powershell
python -m http.server 8000
python scripts/sort_research_catalog.py
```

HTML, JSON-LD, and `sitemap.xml` must stay in agreement when a page is added, removed, or demoted.

## Work rules

- Training/course pages under `training/` and `ai-ciso-training/` / `cloud-security-intro/` are demoted: reachable by URL, not in nav, sitemap, or JSON-LD `hasOfferCatalog`. Do not re-link them without the user's word.
- Research catalog lives in `research/`. Prefer concept DOIs for “latest.”
- Brand palette is in `theme.html`. No emojis in body copy.
- `functions/_middleware.js` is Cloudflare middleware; keep it in sync with how the live host actually serves the site.

## Pointers

- `README.md` — portfolio index
- `CLAUDE.md` — page map, SEO, demotion note
- `sitemap.xml` / `robots.txt` — crawl surface
- `research/` — paper catalog
