# Plugin Specification — 6 Skills Detail

> Read this when implementing a specific skill.
> Jump to the skill you're building — DO NOT read all at once.

## How to Use This File
Each skill section contains a **"SKILL.md Writing Guide"** — this tells you *what to write inside SKILL.md*.
- Content under **Step N:** → PUT this logic INSIDE the SKILL.md as imperative instructions
- Content under **Output Template** → PUT this in `assets/` as a template file, reference from SKILL.md
- Content under **references/ should contain** → PUT this in the corresponding `references/` file
- Decision trees (`IF/ELSE`) → COPY verbatim into SKILL.md — these ARE the prompt instructions

Think of it this way: the "SKILL.md Writing Guide" is a spec for *what the SKILL.md should say*.
The SKILL.md itself is the prompt Claude reads when the skill triggers.

---

## Table of Contents

1. [Skill 1: niche-research](#skill-1-niche-research)
2. [Skill 2: competitor-analysis](#skill-2-competitor-analysis)
3. [Skill 3: audience-persona](#skill-3-audience-persona)
4. [Skill 4: design-brief](#skill-4-design-brief)
5. [Skill 5: landing-page-builder](#skill-5-landing-page-builder)
6. [Skill 6: conversion-optimizer](#skill-6-conversion-optimizer)
7. [OMC Orchestration Configs](#omc-orchestration)
8. [Cross-Skill Conventions](#cross-skill-conventions)

---

## Skill 1: niche-research

### Purpose
Analyze market/keyword landscape for a Google Ads landing page project. Produces the foundation that all other skills depend on.

### SKILL.md Writing Guide

The SKILL.md should instruct Claude to:

**Step 1: Gather Input** (DO NOT SKIP)
- Ask user for: product/service name, target market (geography + language), budget range (optional), existing website URL (optional)
- IF user provides a brief → extract these from the brief
- IF anything unclear → ask, suggest reasonable defaults

**Step 2: Keyword Research** (use web_search)
- Search for: `"{product} {location}"`, `"{product} price"`, `"{product} review"`, `"best {product}"`, `"{product} near me"`
- For Vietnamese market: search both Vietnamese and English terms
- Collect 20-40 keywords minimum

**Step 3: Classify by Search Intent**
```
IF keyword contains "buy", "price", "cost", "order", "book" → TRANSACTIONAL
IF keyword contains "best", "review", "compare", "vs" → COMMERCIAL
IF keyword contains "what is", "how to", "guide" → INFORMATIONAL
IF keyword contains brand name, specific location → NAVIGATIONAL
```
Landing pages target TRANSACTIONAL and COMMERCIAL intent primarily.

**Step 4: Cluster & Suggest Ad Groups**
- Group keywords by theme (3-5 clusters)
- Each cluster = 1 ad group = 1 landing page variant
- Name each cluster descriptively

**Step 5: Estimate CPC & Competition**
- Use web search to find public CPC data for the niche
- Categorize: Low ($0-2), Medium ($2-10), High ($10+)
- IMPORTANT CAVEAT: These are rough estimates from public data. For accurate CPC, use Google Keyword Planner directly. Always note this in the output: "CPC estimates are approximate. Verify with Google Keyword Planner before setting budgets."

**Step 6: Identify Negative Keywords**
- Keywords to exclude (irrelevant traffic)
- Example: "free" if selling premium, "DIY" if selling service

**Step 7: Generate Output**
- Fill `assets/niche-brief-template.md` with all data
- Save to `output/{project}/research/niche-brief.md`

### Output Template (niche-brief-template.md)

```markdown
# Niche Brief: {PROJECT_NAME}

## Project Overview
- **Product/Service**: {PRODUCT}
- **Target Market**: {GEO} — {LANGUAGE}
- **Budget Range**: {BUDGET}
- **Existing Website**: {URL_OR_NONE}
- **Generated**: {DATE}

## Keyword Clusters

### Cluster 1: {CLUSTER_NAME} — {INTENT_TYPE}
**Recommended Ad Group**: {AD_GROUP_NAME}
| Keyword | Est. CPC | Competition | Intent |
|---------|----------|-------------|--------|
| {KW}    | {CPC}    | {HIGH/MED/LOW} | {TYPE} |

### Cluster 2: {CLUSTER_NAME} — {INTENT_TYPE}
(same format)

## Recommended Ad Group → Landing Page Mapping
| Ad Group | Primary Keywords | LP Variant | Priority |
|----------|-----------------|------------|----------|
| {NAME}   | {KWs}           | {VARIANT}  | P0/P1/P2 |

## Negative Keywords
{LIST}

## Key Market Insights
1. {INSIGHT}
2. {INSIGHT}
3. {INSIGHT}

## Next Steps
- [ ] Run competitor-analysis with top keywords
- [ ] Create personas from audience data
```

### references/keyword-research-guide.md should contain:
- Google Ads keyword match types explained (broad, phrase, exact)
- How to estimate CPC from public data
- Keyword clustering methodology
- Vietnamese market-specific tips (diacritics, slang, regional differences)

### references/search-intent-mapping.md should contain:
- 4 intent types with 10+ signal words each
- Decision tree for ambiguous keywords
- How intent maps to landing page strategy

---

## Skill 2: competitor-analysis

### Purpose
Crawl competitor landing pages and extract actionable intelligence about their message, structure, trust signals, CTAs, and design patterns.

### SKILL.md Writing Guide

**Step 1: Gather Competitor URLs**
- IF user provides URLs → use those (3-5 recommended)
- IF user provides only keywords → web_search those keywords, extract top Google Ads results
- IF niche-brief exists → use top keywords from it to find competitors
- ALWAYS confirm URLs with user before crawling

**Step 2: Crawl Each Competitor** (use web_fetch)
- Fetch full HTML of each URL
- IF URL fails → try with/without www, try Google cache, log failure and continue
- Extract: page title, meta description, headings, body text, form fields, links

**Step 3: Analyze Per Competitor**
Score each dimension 1-10 (see `references/scoring-rubric.md`):

```
ANALYSIS FRAMEWORK:
├── MESSAGE
│   ├── Headline clarity (1-10)
│   ├── Value proposition strength (1-10)
│   └── Keyword-headline match (1-10)
├── STRUCTURE
│   ├── Section count and flow
│   ├── Content length (word count)
│   └── Above-fold content quality (1-10)
├── TRUST
│   ├── Testimonial presence and quality (1-10)
│   ├── Trust badges / certifications
│   ├── Social proof (numbers, logos, reviews)
│   └── Guarantee / risk reversal
├── CTA
│   ├── CTA copy clarity (1-10)
│   ├── CTA placement and frequency
│   ├── Urgency / scarcity elements
│   └── Form friction (number of fields)
├── DESIGN
│   ├── Color scheme description
│   ├── Typography (serif/sans, weight)
│   ├── Visual style (modern/classic/playful)
│   └── Image usage
└── TECH
    ├── Framework detection (from HTML source)
    ├── Page speed indicators (script count, image optimization)
    └── Mobile meta viewport present?
```

**Step 4: Cross-Competitor Comparison**
- Find COMMON patterns (what everyone does → table stakes)
- Find DIFFERENTIATORS (what 1-2 do differently)
- Find GAPS (what nobody does → opportunity for our page)

**Step 5: Create Swipe File**
- Best headline → from which competitor
- Best CTA copy → from which
- Best trust signal approach → from which
- Best section layout → from which

**Step 6: Generate Output**
- Fill templates, save to `output/{project}/research/competitor-report.md`

### scripts/extract-page-structure.py should:
- Accept HTML string as input
- Extract: all `<h1>-<h6>` tags, `<form>` fields, `<button>` text, `<img>` alt text
- Count: total word count, number of sections, number of CTAs
- Detect: framework (React? Next? WordPress?), GTM/analytics presence
- Output: structured JSON

---

## Skill 3: audience-persona

### Purpose
Create buyer personas and generate Google Ads copy suggestions that will be message-matched to the landing page.

### SKILL.md Writing Guide

**Step 1: Read Research Inputs**
- Read `output/{project}/research/niche-brief.md` — REQUIRED
- Read `output/{project}/research/competitor-report.md` — RECOMMENDED
- IF neither exists → tell user to run niche-research first

**Step 2: Identify 2-3 Buyer Segments**
From the keyword clusters and competitor messaging, identify distinct buyer types.
Decision criteria:
```
IF keywords show price-sensitivity ("giá", "rẻ", "cheap") → Price-Conscious Segment
IF keywords show quality focus ("tốt nhất", "uy tín", "premium") → Quality-Seeking Segment
IF keywords show urgency ("gấp", "ngay", "emergency") → Urgent-Need Segment
IF keywords show research behavior ("so sánh", "review") → Comparison Shopper Segment
```

**Step 3: Build Persona Cards** (for each segment)
```markdown
## Persona: {NAME}
- **Age**: {range}
- **Occupation**: {type}
- **Income**: {range}
- **Location**: {city/region}
- **Device**: {mobile/desktop preference}
- **Pain Points**: {3 specific problems}
- **Goals**: {what they want to achieve}
- **Objections**: {why they might NOT buy}
- **Buying Triggers**: {what pushes them to act}
- **Search Behavior**: {what they Google, when}
- **Preferred Tone**: {formal/casual/urgent/reassuring}
- **Maps to Ad Group**: {which ad group from niche-brief}
```

**Step 4: Generate Ad Copy Suggestions**
For EACH ad group, generate:
- 3 headlines (max 30 characters each — this is a Google Ads HARD LIMIT)
- 2 descriptions (max 90 characters each — HARD LIMIT)
- 2 CTA variations
- Sitelink suggestions (4 per ad group)

```
CRITICAL CHARACTER LIMITS:
- Headline: 30 chars max (including spaces)
- Description: 90 chars max (including spaces)
- Display URL path: 15 chars each (2 paths)
- Sitelink title: 25 chars max
- Sitelink description: 35 chars per line (2 lines)

COUNT CHARACTERS BEFORE OUTPUT. If over limit, rewrite shorter.
Vietnamese characters (ă, â, ê, ô, ơ, ư, đ) count as 1 character each.
```

**Step 5: Map Persona → Ad Group → LP Tone**
Create mapping table showing how each persona's needs translate to specific landing page messaging.

**Step 6: Generate Outputs**
- `output/{project}/research/personas.md`
- `output/{project}/research/ad-copy-suggestions.md`

---

## Skill 4: design-brief

### Purpose
Generate a design system (MASTER.md) for the landing page by calling UUPM and augmenting with Google Ads-specific design rules.

### SKILL.md Writing Guide

**Step 1: Prepare UUPM Search Query**
From research outputs, construct a search query:
```
FORMAT: "{industry} {product_type} {audience} {mood_keywords}"
EXAMPLE: "dental clinic implant healthcare Vietnamese trust professional"
```
Extract:
- Industry → from niche-brief
- Product type → from niche-brief
- Audience → from personas (age, style preference)
- Mood → from competitor gaps (what to differentiate)

**Step 2: Check UUPM and Execute**
```bash
# Check if UUPM exists
IF [ -f ".claude/skills/ui-ux-pro-max/scripts/search.py" ]; THEN

  # Generate main design system
  python3 .claude/skills/ui-ux-pro-max/scripts/search.py \
    "{search_query}" \
    --design-system --persist \
    -p "{ProjectName}"

  # Generate page-specific overrides for each ad group
  FOR EACH ad_group IN niche-brief.ad_groups:
    python3 .claude/skills/ui-ux-pro-max/scripts/search.py \
      "{ad_group_specific_query}" \
      --design-system --persist \
      -p "{ProjectName}" \
      --page "{ad_group_name}"

ELSE
  # Fallback: use built-in design rules
  READ references/fallback-design-rules.md
  MANUALLY construct MASTER.md from fallback rules
```

**Step 3: Augment with Google Ads Landing Page Rules**
UUPM gives generic design intelligence. Add these LP-specific rules to MASTER.md:

```markdown
## Google Ads Landing Page — Design Overrides

### CTA Button
- Color: MUST contrast with page background at 4.5:1 ratio minimum
- Size: minimum 48x48px touch target
- Position: above fold (visible without scrolling on mobile)
- Copy: action verb + benefit ("Đặt Lịch Miễn Phí", NOT just "Submit")

### Trust Section
- Position: immediately before or after primary CTA
- Must include at least 2 of: testimonials, logos, badges, stats
- Real photos preferred over stock

### Form (if lead gen)
- Maximum 3-5 fields for first interaction
- Name + Phone + Email is maximum for cold traffic
- Single column layout on mobile
- Progress indicator if multi-step

### Hero Section
- Headline: large, bold, matches ad copy exactly
- Sub-headline: expands on value prop, 1-2 lines
- NO navigation bar (distraction-free)
- NO hamburger menu
- Background: clean, not competing with text readability

### Typography for Landing Pages
- Headline: ≥ 32px on desktop, ≥ 24px on mobile
- Body: ≥ 16px (never smaller for readability)
- Line height: 1.5-1.7 for body text
- Max 2 font families per page
```

**Step 4: Generate Output**
- Move UUPM output to `output/{project}/design-system/MASTER.md`
- Merge Google Ads overrides into MASTER.md
- Copy page overrides to `output/{project}/design-system/pages/`

---

## Skill 5: landing-page-builder

### Purpose
Generate complete, production-ready landing page code from research + design inputs.

### SKILL.md Writing Guide

**Step 1: Validate Inputs Exist**
```
REQUIRED (refuse to proceed without these):
- output/{project}/design-system/MASTER.md
- output/{project}/research/niche-brief.md

RECOMMENDED (proceed with warning if missing):
- output/{project}/research/personas.md
- output/{project}/research/ad-copy-suggestions.md
- output/{project}/research/competitor-report.md
```

**Step 2: Detect or Select Tech Stack**
```
IF package.json exists AND has "next" → React/Next.js
  READ references/stack-guides/react-nextjs.md NOW
IF package.json exists AND has "astro" → Astro
  READ references/stack-guides/astro.md NOW
IF index.html exists OR no package.json → HTML+Tailwind
  READ references/stack-guides/html-tailwind.md NOW
ELSE → ASK user, default to HTML+Tailwind
```

**Step 3: Read Design System**
- Read `MASTER.md` for: colors, fonts, spacing, style, pattern, anti-patterns
- Read `pages/{ad-group}.md` if building specific variant
- Extract: primary color, CTA color, font family, section order

**Step 4: Build Section by Section**
Follow the pattern from MASTER.md. Default section order:

```
1. HEAD
   - Meta tags (title, description, OG, Twitter Card)
   - Google Fonts preload
   - Critical CSS inline
   - GTM container snippet (placeholder: {GTM_ID})
   - Favicon

2. HERO
   - Headline: EXACT text from ad-copy-suggestions.md, first headline of target ad group
   - Sub-headline: value proposition from personas
   - CTA button: from ad-copy-suggestions.md CTA variations
   - Hero image: placeholder with correct aspect ratio
   - Trust badges: 3-4 small logos/badges above fold
   - NO navigation bar

3. PROBLEM / PAIN POINTS (PAS Framework)
   - 3 pain points from persona's pain points
   - Icon + short title + 1-2 sentence description
   - Emotional language matching persona tone

4. SOLUTION / BENEFITS
   - 3-4 benefits (feature → benefit format)
   - Card or grid layout
   - Each card: icon + title + description

5. SOCIAL PROOF
   - 2-3 testimonials (photo placeholder + quote + name + title)
   - Stats bar (e.g., "500+ khách hàng", "4.9/5 đánh giá")
   - Client/partner logos (placeholder grid)

6. HOW IT WORKS
   - 3 numbered steps
   - Simple, visual flow
   - Reduces perceived complexity

7. FAQ
   - 4-6 questions from persona objections
   - Accordion/toggle format
   - Schema markup: FAQPage

8. FINAL CTA
   - Repeat primary CTA
   - Add guarantee / risk reversal
   - Urgency element (optional, based on campaign type)

9. FOOTER (minimal)
   - Company name, address (for local businesses)
   - Legal links: Privacy, Terms
   - Phone/email
   - NO navigation links
```

**Step 5: Google Ads Integration**
Add to the generated code:
```html
<!-- Dynamic Keyword Insertion support -->
<!-- URL param: ?keyword={keyword} -->
<script>
  const params = new URLSearchParams(window.location.search);
  const kw = params.get('keyword');
  if (kw) {
    document.querySelectorAll('[data-dki]').forEach(el => {
      el.textContent = decodeURIComponent(kw);
    });
  }
</script>

<!-- UTM tracking -->
<!-- URL format: ?utm_source=google&utm_medium=cpc&utm_campaign={campaign}&utm_content={ad_group} -->

<!-- Google Tag Manager (placeholder) -->
<!-- Replace {GTM_ID} with actual container ID -->

<!-- Conversion tracking placeholder -->
<!-- gtag('event', 'conversion', { send_to: '{CONVERSION_ID}/{CONVERSION_LABEL}' }); -->

<!-- Schema Markup -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [...]
}
</script>
```

**Step 6: Performance Optimization**
- Images: `loading="lazy"` on all below-fold images
- Fonts: `<link rel="preload">` for primary font
- CSS: Critical CSS inline in `<head>`, rest loaded async
- JS: Minimal, defer non-critical scripts
- HTML: Semantic tags, no unnecessary wrappers

**Step 7: Responsive Breakpoints**
```
Mobile:  375px  (primary — code this FIRST)
Tablet:  768px
Desktop: 1024px
Large:   1440px (max-width container)
```

**Step 8: Pre-Delivery Checklist**
Before marking complete, verify ALL:
```
[ ] Headline matches ad copy word-for-word
[ ] CTA above fold on mobile (375px)
[ ] CTA button has 4.5:1 contrast ratio
[ ] No navigation menu / no distractions
[ ] All images have alt text
[ ] Font size ≥ 16px for body
[ ] Touch targets ≥ 48px
[ ] Schema markup present (FAQPage, LocalBusiness/Product)
[ ] OG + Twitter Card meta tags
[ ] GTM placeholder present
[ ] Conversion tracking placeholder present
[ ] favicon linked
[ ] Page works without JavaScript (progressive enhancement)
[ ] HTML validates (no unclosed tags)
[ ] Responsive at 375, 768, 1024, 1440
```

**Step 9: Output**
- Save to `output/{project}/src/`
- Generate `output/{project}/landing-page-checklist.md` with check results

---

## Skill 6: conversion-optimizer

### Purpose
Audit a landing page (URL or local file) and produce a scored report with specific fix recommendations and A/B test suggestions.

### SKILL.md Writing Guide

**Step 1: Get Landing Page Content**
```
IF user provides URL → web_fetch the URL
IF user provides file path → read the file
IF neither → check output/{project}/src/ for recently built page
IF nothing found → ask user
```

**Step 2: Read Research Context** (for message match checking)
- Read `output/{project}/research/ad-copy-suggestions.md` for expected headline
- Read `output/{project}/design-system/MASTER.md` for design compliance
- IF no research outputs → audit in "standalone mode" (skip message match category)

**Step 3: Run 7-Category Audit**

```
CATEGORY 1: MESSAGE MATCH (20% weight)
├── Headline matches ad copy? (0-40 points)
├── Keywords present in first 100 words? (0-30 points)
└── Value prop clear within 5 seconds? (0-30 points)
Score: {X}/100 → weighted: {X * 0.20}

CATEGORY 2: CTA EFFECTIVENESS (20% weight)
├── CTA visible above fold? (0-25 points)
├── CTA copy is action + benefit? (0-25 points)
├── CTA color contrasts with background? (0-25 points)
└── CTA repeated after social proof? (0-25 points)
Score: {X}/100 → weighted: {X * 0.20}

CATEGORY 3: TRUST & SOCIAL PROOF (15% weight)
├── Testimonials present? (0-30 points)
├── Trust badges/certifications? (0-25 points)
├── Specific numbers/stats? (0-25 points)
└── Real names/photos (not stock)? (0-20 points)
Score: {X}/100 → weighted: {X * 0.15}

CATEGORY 4: PAGE SPEED SIGNALS (15% weight)
├── Image count and optimization (0-30 points)
├── Script count (<5 is good) (0-25 points)
├── CSS approach (inline critical?) (0-25 points)
└── Font loading strategy (0-20 points)
Score: {X}/100 → weighted: {X * 0.15}

CATEGORY 5: MOBILE EXPERIENCE (15% weight)
├── Viewport meta tag present? (0-20 points)
├── Touch targets ≥ 48px? (0-25 points)
├── Font size ≥ 16px? (0-25 points)
└── Single column layout on mobile? (0-30 points)
Score: {X}/100 → weighted: {X * 0.15}

CATEGORY 6: CONTENT QUALITY (10% weight)
├── Readability (short paragraphs, scannable) (0-30 points)
├── Benefit-focused (not feature-focused) (0-30 points)
├── Addresses objections (FAQ present?) (0-20 points)
└── Emotional triggers present? (0-20 points)
Score: {X}/100 → weighted: {X * 0.10}

CATEGORY 7: TECHNICAL SEO (5% weight)
├── Schema markup present? (0-30 points)
├── Meta title + description? (0-25 points)
├── OG/Twitter Card tags? (0-25 points)
└── Canonical URL? (0-20 points)
Score: {X}/100 → weighted: {X * 0.05}

TOTAL SCORE: sum of weighted scores → {X}/100
```

**Step 4: Generate Fix Recommendations**
Categorize into:
- **Critical** (score impact > 10 points): fix immediately
- **Quick Wins** (< 30 min effort, score impact 5-10 points): do next
- **Nice to Have** (score impact < 5 points): backlog

**Step 5: Generate A/B Test Suggestions**
For each "Quick Wins" item, suggest a testable variant:
```markdown
### A/B Test: {Test Name}
- **Element**: {what to change}
- **Control**: "{current version}"
- **Variant A**: "{alternative 1}"
- **Variant B**: "{alternative 2}" (optional)
- **Hypothesis**: {why variant might convert better}
- **Priority**: {HIGH/MEDIUM/LOW}
```

Generate 2-3 A/B tests per audit.

**Step 6: Output**
- Save to `output/{project}/audit/optimization-report.md`

---

## OMC Orchestration

> **IMPORTANT**: oh-my-claudecode does NOT read config files. It uses magic keywords in prompts.
> The files below are PROMPT TEMPLATES for the user to paste into Claude Code with OMC active.
> They are NOT machine-readable configs.

### orchestration/pipeline.md

```markdown
# Landing Page Pro — Pipeline Prompt Template

## How to Use
Copy-paste the prompt below into Claude Code (with OMC installed).

## Full Pipeline Prompt
autopilot: Build a Google Ads landing page for {client brief}.
Follow the landing-page-pro plugin pipeline:
1. Run niche-research skill → save to output/{project}/research/niche-brief.md
2. Run competitor-analysis skill → save to output/{project}/research/competitor-report.md
3. Run audience-persona skill → save to output/{project}/research/
4. Run design-brief skill (use UUPM) → save to output/{project}/design-system/MASTER.md
5. Run landing-page-builder skill → save to output/{project}/src/
6. Run conversion-optimizer skill → save to output/{project}/audit/
Show me each output before proceeding to the next step.
```

### orchestration/swarm-config.md

```markdown
# Landing Page Pro — Parallel Research Prompt Template

## How to Use
Copy-paste the prompt below into Claude Code (with OMC installed).

## Parallel Research Prompt
swarm: Research for a landing page project: {client brief}.
Run these tasks in parallel:
- Task 1: niche-research — find keywords, CPC, search intent
- Task 2: competitor-analysis — crawl and analyze top 3-5 competitor pages
Save all outputs to output/{project}/research/.
After both complete, continue sequentially with audience-persona.

## Ecomode Prompt (save tokens)
eco: Build a landing page for {client brief}.
Use the landing-page-pro pipeline. For research tasks, be concise.
For creative tasks (ad copy, design, code), be thorough.
```

---

## Cross-Skill Conventions

### SKILL.md Frontmatter (REQUIRED)
Every SKILL.md MUST start with YAML frontmatter for triggering:
```yaml
---
name: skill-name
description: "Trigger description — be pushy, include many trigger phrases.
Use when user says X, Y, Z. Also trigger for indirect requests like A, B, C."
---
```
Without this frontmatter, Claude Code will NOT know when to activate the skill.

### File Naming
- All output files: kebab-case
- Project folder: kebab-case of product/client name
- Templates: use `{PLACEHOLDER}` format (uppercase, curly braces)

### Error Messages
When a skill needs input from a previous skill that doesn't exist:
```
⚠️ Required input not found: output/{project}/research/niche-brief.md
→ Run `niche-research` skill first: "Research keywords for {project}"
```

### Progress Indicators
Each skill should output progress:
```
[niche-research] Step 1/7: Gathering input...
[niche-research] Step 2/7: Searching keywords...
...
[niche-research] ✅ Complete → output/{project}/research/niche-brief.md
```

### Vietnamese Language Support
- All templates support Vietnamese output
- Ad copy character counting: Vietnamese diacritics (ă, â, ê, ô, ơ, ư, đ) = 1 char each
- Search keywords: include both with and without diacritics
- Default language: Vietnamese (unless user specifies otherwise)
