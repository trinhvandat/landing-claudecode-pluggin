# landing-page-pro

A Claude Code plugin that automates the full Google Ads landing page workflow — from market research to deployed, conversion-optimized page.

## Skills

| # | Skill | What it does |
|---|-------|-------------|
| 1 | `niche-research` | Keyword research, search intent mapping, CPC estimates |
| 2 | `competitor-analysis` | Crawl & score competitor landing pages |
| 3 | `audience-persona` | Buyer personas + Google Ads copy suggestions |
| 4 | `design-brief` | Design system generation (via UUPM or fallback rules) |
| 5 | `landing-page-builder` | Full landing page code, mobile-first, single CTA |
| 6 | `conversion-optimizer` | 7-category audit with A/B test recommendations |

## Pipeline

```
niche-research ──┐
                  ├──→ audience-persona → design-brief → landing-page-builder → conversion-optimizer
competitor-analysis┘
```

Skills 1 & 2 run in parallel. Skills 3-6 are sequential.

## Install

```
claude /install-plugin landing-page-pro
```

## License

MIT
