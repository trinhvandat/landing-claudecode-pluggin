# Plugin Structure Blueprint

> Read this file when you need to create or verify the plugin's directory structure.
> Every file listed here is intentional. DO NOT create files not listed here without asking.

## Complete Directory Tree

```
landing-page-pro/
│
├── .claude-plugin/
│   └── plugin.json                         # Plugin identity — name, version, author
│
├── .claude/
│   └── CLAUDE.md                           # → symlinked or copied to root CLAUDE.md
│
├── manifest.json                           # Skills registry — maps skill names to SKILL.md paths
├── README.md                               # Human-readable: what plugin does, install, usage
├── CLAUDE.md                               # Symlink → .claude/CLAUDE.md
│
├── blueprint/                              # Implementation specs (you're reading one now)
│   ├── plugin-structure.md                 # THIS FILE
│   └── plugin-spec.md                      # Detailed skill specifications
│
├── skills/
│   │
│   ├── niche-research/
│   │   ├── SKILL.md                        # Imperative prompt for keyword/niche research
│   │   ├── references/
│   │   │   ├── keyword-research-guide.md   # How to structure keyword research, search intent types
│   │   │   └── search-intent-mapping.md    # Intent categories: informational, commercial, transactional, navigational
│   │   └── assets/
│   │       └── niche-brief-template.md     # Output template with {PLACEHOLDER}s
│   │
│   ├── competitor-analysis/
│   │   ├── SKILL.md                        # Imperative prompt for competitor page analysis
│   │   ├── references/
│   │   │   ├── analysis-framework.md       # What to analyze: message, structure, trust, CTA, design, tech
│   │   │   └── scoring-rubric.md           # How to score each competitor dimension (1-10)
│   │   ├── scripts/
│   │   │   └── extract-page-structure.py   # Parse HTML → extract sections, headings, CTAs, forms
│   │   └── assets/
│   │       ├── competitor-report-template.md
│   │       └── swipe-file-template.md      # Best elements collected from competitors
│   │
│   ├── audience-persona/
│   │   ├── SKILL.md                        # Imperative prompt for persona + ad copy generation
│   │   ├── references/
│   │   │   ├── persona-framework.md        # Demographics, psychographics, pain points, triggers
│   │   │   └── ad-copy-formulas.md         # PAS, AIDA, BAB frameworks + Google Ads char limits
│   │   └── assets/
│   │       ├── persona-template.md         # Persona card template
│   │       └── ad-copy-template.md         # Ad headline/description template with char counts
│   │
│   ├── design-brief/
│   │   ├── SKILL.md                        # Imperative prompt — bridge between research and UUPM
│   │   ├── references/
│   │   │   ├── uupm-integration-guide.md   # How to call UUPM search.py, parse output, merge with LP rules
│   │   │   └── fallback-design-rules.md    # Subset of design intelligence if UUPM not installed
│   │   └── assets/
│   │       └── master-md-template.md       # MASTER.md template for landing pages specifically
│   │
│   ├── landing-page-builder/
│   │   ├── SKILL.md                        # Imperative prompt for code generation
│   │   ├── references/
│   │   │   ├── google-ads-lp-rules.md      # Google Ads-specific landing page rules (QS, conversion tracking, schema)
│   │   │   ├── section-patterns.md         # Standard section library: hero, benefits, social-proof, FAQ, CTA
│   │   │   └── stack-guides/
│   │   │       ├── html-tailwind.md        # HTML + Tailwind CSS generation rules
│   │   │       ├── react-nextjs.md         # React / Next.js generation rules
│   │   │       └── astro.md               # Astro generation rules
│   │   └── assets/
│   │       └── html-tailwind-starter.html  # Minimal starter template with Tailwind CDN, meta tags, GTM placeholder
│   │
│   └── conversion-optimizer/
│       ├── SKILL.md                        # Imperative prompt for audit & optimization
│       ├── references/
│       │   ├── audit-checklist.md          # 7-category scoring system with weights
│       │   └── ab-test-patterns.md         # Common A/B test variations for landing pages
│       └── assets/
│           └── audit-report-template.md    # Report template with score breakdown + recommendations
│
├── orchestration/                          # OMC integration configs
│   ├── pipeline.md                         # Sequential execution: research → build → audit
│   └── swarm-config.md                     # Parallel execution: research skills simultaneously
│
└── output/                                 # Generated project outputs (gitignored)
    └── .gitkeep
```

## File Size Guidelines

| File Type | Target Size | Max Size |
|-----------|-------------|----------|
| SKILL.md | 150-300 lines | 500 lines |
| references/*.md | 100-200 lines | 400 lines |
| assets/templates | 50-100 lines | 200 lines |
| scripts/*.py | As needed | Keep focused, single-purpose |

## Key Relationships

```
CLAUDE.md
  ↓ points to
blueprint/plugin-spec.md
  ↓ defines
skills/*/SKILL.md
  ↓ reads on-demand
skills/*/references/*.md
  ↓ uses as output format
skills/*/assets/*-template.md
```

## .claude-plugin/plugin.json

> **VERIFY BEFORE PUBLISHING**: The schema below is based on current Claude Code plugin conventions.
> Run `/plugin validate` in Claude Code to check if the format is still correct.
> If Claude Code uses a different format (e.g., `manifest.yaml`), adapt accordingly.

```json
{
  "name": "landing-page-pro",
  "version": "1.0.0",
  "description": "Research-driven Google Ads landing page builder — 6-skill pipeline from brief to deployed page",
  "author": "Leonard",
  "homepage": "",
  "license": "MIT",
  "claude_code_version": ">=1.0.0",
  "skills_dir": "skills"
}
```

## manifest.json

```json
{
  "name": "landing-page-pro",
  "version": "1.0.0",
  "skills": [
    {
      "name": "niche-research",
      "description": "Research keywords, search intent, and CPC estimates for Google Ads landing pages. Use when starting a new landing page project, when user says 'research keywords', 'find niche', 'market analysis', or any new client brief. Always use this BEFORE building any landing page.",
      "path": "skills/niche-research/SKILL.md"
    },
    {
      "name": "competitor-analysis",
      "description": "Crawl and analyze competitor landing pages to find patterns, strengths, weaknesses, and gaps. Use when user provides competitor URLs, says 'analyze competitor', 'check competition', or wants to understand the competitive landscape before building.",
      "path": "skills/competitor-analysis/SKILL.md"
    },
    {
      "name": "audience-persona",
      "description": "Generate buyer personas and Google Ads copy suggestions based on research data. Use when user says 'create persona', 'target audience', 'write ad copy', 'who is the customer', or after completing niche research and competitor analysis.",
      "path": "skills/audience-persona/SKILL.md"
    },
    {
      "name": "design-brief",
      "description": "Generate a design system (MASTER.md) for the landing page using UUPM design intelligence. Use when user says 'design the page', 'choose colors', 'pick style', 'create design brief', or before building the landing page. This bridges research outputs to visual design decisions.",
      "path": "skills/design-brief/SKILL.md"
    },
    {
      "name": "landing-page-builder",
      "description": "Generate complete landing page code optimized for Google Ads conversion. Use when user says 'build the page', 'create landing page', 'code the page', 'generate HTML'. Requires design-brief output (MASTER.md) and research outputs. Auto-detects or asks for tech stack.",
      "path": "skills/landing-page-builder/SKILL.md"
    },
    {
      "name": "conversion-optimizer",
      "description": "Audit an existing landing page for Google Ads conversion optimization. Scores across 7 categories, suggests specific fixes and A/B test variants. Use when user says 'audit page', 'optimize conversion', 'review landing page', 'improve page', or after building a page.",
      "path": "skills/conversion-optimizer/SKILL.md"
    }
  ]
}
```
