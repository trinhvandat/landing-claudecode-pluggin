# Landing Page Pro — Pipeline Prompt Template

> **IMPORTANT**: oh-my-claudecode does NOT read config files. It uses magic keywords in prompts.
> This file is a PROMPT TEMPLATE for the user to paste into Claude Code with OMC active.
> It is NOT a machine-readable config.

## How to Use

1. Replace `{client brief}` with your actual client brief or description.
2. Replace `{project}` with the kebab-case project name (e.g., `dental-implant-clinic`).
3. Copy-paste the prompt below into Claude Code (with OMC installed).
4. The pipeline keyword triggers sequential execution through all 6 skills.

## Full Pipeline Prompt

```
pipeline: Build a Google Ads landing page for {client brief}.
Follow the landing-page-pro plugin pipeline:

1. Run niche-research skill
   → Save to output/{project}/research/niche-brief.md

2. Run competitor-analysis skill
   → Save to output/{project}/research/competitor-report.md
   → Save to output/{project}/research/swipe-file.md

3. Run audience-persona skill
   → Save to output/{project}/research/personas.md
   → Save to output/{project}/research/ad-copy-suggestions.md

4. Run design-brief skill (use UUPM if available)
   → Save to output/{project}/design-system/MASTER.md
   → Save to output/{project}/design-system/pages/ (per ad group)

5. Run landing-page-builder skill
   → Save to output/{project}/src/index.html (or framework equivalent)
   → Save to output/{project}/landing-page-checklist.md

6. Run conversion-optimizer skill
   → Save to output/{project}/audit/optimization-report.md

Show me each output before proceeding to the next step.
```

## Pipeline with Parallel Research Start

Steps 1 and 2 are independent — they can run in parallel before the sequential chain.

```
pipeline: Build a Google Ads landing page for {client brief}.

Phase 1 (parallel):
  - niche-research → output/{project}/research/niche-brief.md
  - competitor-analysis → output/{project}/research/competitor-report.md

Phase 2 (sequential, depends on Phase 1):
  - audience-persona → output/{project}/research/personas.md + ad-copy-suggestions.md
  - design-brief → output/{project}/design-system/MASTER.md
  - landing-page-builder → output/{project}/src/
  - conversion-optimizer → output/{project}/audit/optimization-report.md

Show me each output before proceeding.
```

## Skip-to-Build Prompt (when research already exists)

If you've already completed research and design, start from step 5:

```
pipeline: Build the landing page for {project}.
Research and design system already exist at:
  - output/{project}/research/niche-brief.md
  - output/{project}/research/ad-copy-suggestions.md
  - output/{project}/design-system/MASTER.md

Skip to landing-page-builder skill, then run conversion-optimizer.
Save to output/{project}/src/ and output/{project}/audit/.
```

## Output Path Reference

All paths follow the convention in CLAUDE.md:

```
output/{project}/
├── research/
│   ├── niche-brief.md           ← Skill 1: niche-research
│   ├── competitor-report.md     ← Skill 2: competitor-analysis
│   ├── swipe-file.md            ← Skill 2: competitor-analysis
│   ├── personas.md              ← Skill 3: audience-persona
│   └── ad-copy-suggestions.md   ← Skill 3: audience-persona
├── design-system/
│   ├── MASTER.md                ← Skill 4: design-brief
│   └── pages/*.md               ← Skill 4: design-brief (per ad group)
├── src/
│   └── index.html               ← Skill 5: landing-page-builder
├── landing-page-checklist.md    ← Skill 5: landing-page-builder
└── audit/
    └── optimization-report.md   ← Skill 6: conversion-optimizer
```
