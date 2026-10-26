# Vistigo by 444Video

Marketing site for **Vistigo**, the 444Video observability platform, with one page per pillar:

| Page | Path | Accent |
|------|------|--------|
| Hub - one view of everything you run | `/` | Aqua |
| Vistigo Maritime - every vessel, always connected | `/maritime/` | Aqua |
| Vistigo Broadcast - catch the error before the viewer does | `/broadcast/` | Orange |
| Vistigo Infra - know your hardware before it fails | `/infra/` | Purple |

Plain static HTML and CSS, no build step. Hosted on GitHub Pages from the `main` branch root.

## Structure

```
index.html            hub page
maritime/index.html   Maritime pillar
broadcast/index.html  Broadcast pillar
infra/index.html      Infra pillar
assets/site.css       all colour and type tokens, defined once at the top
assets/site.js        mobile menu toggle
assets/fonts/         Inter and IBM Plex Mono, self-hosted (no Google Fonts requests)
```

## Brand rules followed

Taken from the 444Video Marketing & Brand Guidelines v1.0 and the website design system in Outline:

- Dark ground `#0A141C`. Aqua `#00FEC8` for links and interactive states. Logo blue is never used for text.
- Pure brand hues only in the colour-bar rule and chart series.
- Inter for everything, IBM Plex Mono for data readouts. Both self-hosted.
- UK English. Hyphens, not em dashes.
- Comux figures are attributed to "a UK multiplex operator" and never generalised.
- Call to action: "Tell us what you can't see."

## Editing

Each page is self-contained HTML. The header and footer are repeated on every page, so change all four when editing them. The dashboards on each page are illustrative mock-ups with sample data, built in HTML and SVG. Swap them for real Grafana screenshots when they're ready.

## Custom domain

To serve from a domain such as `vistigo.io`, add a `CNAME` file containing the domain, then point DNS at GitHub Pages (see GitHub's docs on custom domains).
