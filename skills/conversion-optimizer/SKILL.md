---
name: conversion-optimizer
description: "Audit a landing page and produce a scored optimization report with fix recommendations and A/B test suggestions. Use when user says 'audit landing page', 'optimize conversions', 'check my page', 'score the landing page', 'CRO audit', 'conversion rate optimization', 'what should I improve', 'review the page', or any request to evaluate or improve an existing landing page."
---

# Conversion Optimizer — 7-Category Landing Page Audit

You are running the conversion-optimizer skill. Your job: audit a landing page across 7 weighted categories, produce a total score out of 100, and generate prioritized fix recommendations with A/B test suggestions.

## Step 1: Get Landing Page Content

```
IF user provides a URL
  → web_fetch the URL to get HTML
  → IF web_fetch fails → ask user to paste HTML source
  → IF web_fetch unavailable → tell user:
    "web_fetch is not available. To audit, I need you to:
     1. Open the page in your browser
     2. Right-click → View Page Source
     3. Copy-paste the HTML here"

IF user provides a file path
  → Read the file directly

IF neither URL nor file path given
  → Check output/{PROJECT_NAME}/src/ for recently built page
  → IF found → use that file
  → IF not found → ask user: "Provide a URL or file path to the landing page to audit."
```

## Step 2: Read Research Context

Read these for message match checking and design compliance:

```
FOR MESSAGE MATCH:
  Read output/{PROJECT_NAME}/research/ad-copy-suggestions.md
  → Extract: expected h1 headline (headline 1 of target ad group)
  → IF missing → audit in "standalone mode" (skip message match sub-score, reweight)

FOR DESIGN COMPLIANCE:
  Read output/{PROJECT_NAME}/design-system/MASTER.md
  → Extract: expected colors, fonts, CTA rules
  → IF missing → skip design compliance check, audit visual elements generically

FOR PERSONA ALIGNMENT:
  Read output/{PROJECT_NAME}/research/personas.md
  → Extract: expected tone, pain points addressed, objections in FAQ
  → IF missing → skip persona-specific content checks
```

IF no research outputs exist at all:
  → Proceed in **standalone audit mode**. All 7 categories still apply, but:
  → Category 1 (Message Match) uses generic best practices instead of ad-specific checks.
  → Add note: "Audit performed in standalone mode — no research context available."

## Step 3: Run 7-Category Audit

Score each category. Read `references/audit-checklist.md` for detailed scoring criteria per sub-metric.

```
CATEGORY 1: MESSAGE MATCH (20% weight)
├── Headline matches ad copy?              0-40 points
│   IF ad-copy-suggestions.md exists → exact match check
│   IF standalone mode → check clarity and keyword presence
├── Keywords in first 100 words?           0-30 points
│   Count target keywords from niche-brief in opening content
└── Value prop clear within 5 seconds?     0-30 points
    Is the core offer obvious from above-fold content?
Score: {X}/100 → weighted: {X × 0.20}

CATEGORY 2: CTA EFFECTIVENESS (20% weight)
├── CTA visible above fold?                0-25 points
│   Check if CTA button appears before scroll at 375px
├── CTA copy is action + benefit?          0-25 points
│   "Đặt Lịch Miễn Phí" ✅ vs "Submit" ❌
├── CTA color contrasts with background?   0-25 points
│   Check contrast ratio (4.5:1 minimum for AA)
└── CTA repeated after social proof?       0-25 points
    Count CTA instances, check placement positions
Score: {X}/100 → weighted: {X × 0.20}

CATEGORY 3: TRUST & SOCIAL PROOF (15% weight)
├── Testimonials present?                  0-30 points
│   Real names, photos, specific outcomes = high score
├── Trust badges/certifications?           0-25 points
│   Industry-relevant certifications, awards, partner logos
├── Specific numbers/stats?                0-25 points
│   "2,847 khách hàng" > "nhiều khách hàng"
└── Real names/photos (not stock)?         0-20 points
    Identifiable as real vs generic stock imagery
Score: {X}/100 → weighted: {X × 0.15}

CATEGORY 4: PAGE SPEED SIGNALS (15% weight)
├── Image count and optimization           0-30 points
│   Count images, check loading="lazy", alt text, format hints
├── Script count (<5 is good)              0-25 points
│   Count <script> tags. <5 good, 5-10 okay, >10 bad
├── CSS approach (inline critical?)        0-25 points
│   Critical CSS in <head>? External sheets minimized?
└── Font loading strategy                  0-20 points
    Preload? display:swap? Max 2 families?
Score: {X}/100 → weighted: {X × 0.15}

CATEGORY 5: MOBILE EXPERIENCE (15% weight)
├── Viewport meta tag present?             0-20 points
│   <meta name="viewport" content="width=device-width, initial-scale=1">
├── Touch targets ≥ 48px?                  0-25 points
│   Check button/link sizing from CSS or inline styles
├── Font size ≥ 16px?                      0-25 points
│   Body text must be readable without zooming
└── Single column layout on mobile?        0-30 points
    No horizontal scrolling, no side-by-side elements on small screens
Score: {X}/100 → weighted: {X × 0.15}

CATEGORY 6: CONTENT QUALITY (10% weight)
├── Readability (short paragraphs)         0-30 points
│   Scannable? Bullet points? Short sections?
├── Benefit-focused (not feature-focused)  0-30 points
│   "Ăn nhai tự nhiên" (benefit) > "Công nghệ Đức" (feature)
├── Addresses objections (FAQ present?)    0-20 points
│   FAQ section with 4+ questions? Objections from personas?
└── Emotional triggers present?            0-20 points
    Pain amplification, aspiration, urgency, social belonging
Score: {X}/100 → weighted: {X × 0.10}

CATEGORY 7: TECHNICAL SEO (5% weight)
├── Schema markup present?                 0-30 points
│   FAQPage, LocalBusiness, Product, Organization
├── Meta title + description?              0-25 points
│   Both present, correct length, keyword-rich
├── OG/Twitter Card tags?                  0-25 points
│   og:title, og:description, og:image, twitter:card
└── Canonical URL?                         0-20 points
    <link rel="canonical"> present
Score: {X}/100 → weighted: {X × 0.05}

TOTAL SCORE = sum of all weighted scores → {X}/100
```

### Standalone Mode Reweighting

IF message match context is unavailable (no ad-copy-suggestions.md):
```
Category 1 weight → 10% (instead of 20%, use generic headline quality check)
Category 2 weight → 25% (absorbs 5%)
Category 5 weight → 20% (absorbs 5%)
All other weights unchanged.
Total still = 100%
```

## Step 4: Generate Fix Recommendations

After scoring, categorize every item scoring below 70% into:

```
CRITICAL (score impact > 10 weighted points):
  → Fix immediately. These are conversion killers.
  → Format: "🔴 CRITICAL: {problem} → {specific fix}"

QUICK WINS (< 30 min effort, 5-10 weighted points impact):
  → Do next. High ROI improvements.
  → Format: "🟡 QUICK WIN: {problem} → {specific fix} (est. {time})"

NICE TO HAVE (< 5 weighted points impact):
  → Backlog. Low impact but good practice.
  → Format: "🟢 NICE TO HAVE: {problem} → {specific fix}"
```

Rules:
- Be SPECIFIC. Not "improve CTA" but "Change CTA from 'Gửi' to 'Đặt Lịch Tư Vấn Miễn Phí'"
- Include the current state AND the recommended state.
- Estimate effort where possible (5 min, 15 min, 30 min, 1 hour).

## Step 5: Generate A/B Test Suggestions

For each QUICK WIN, suggest a testable variant. Read `references/ab-test-patterns.md` for common patterns.

Generate 2-3 A/B tests per audit:

```
### A/B Test: {TEST_NAME}
- **Element**: {what to change — button, headline, section, etc.}
- **Control (A)**: "{current version — exact text or description}"
- **Variant B**: "{alternative 1}"
- **Variant C**: "{alternative 2}" (optional)
- **Hypothesis**: "{why variant might convert better — be specific}"
- **Metric**: {what to measure — CTR, form submissions, scroll depth}
- **Priority**: {HIGH / MEDIUM / LOW}
- **Effort**: {estimated implementation time}
```

Rules:
- Only 1 variable per test (isolate the change).
- Hypothesis must be specific and testable.
- Priority based on expected impact × ease of implementation.
- Always include what metric to track.

## Step 6: Generate Output

Fill `assets/audit-report-template.md` and save:

```
output/{PROJECT_NAME}/audit/optimization-report.md
```

Show progress:
```
[conversion-optimizer] Step 1/6: Getting landing page content...
[conversion-optimizer] Step 2/6: Reading research context...
[conversion-optimizer]   → Ad copy: {FOUND / NOT FOUND (standalone mode)}
[conversion-optimizer]   → Design system: {FOUND / NOT FOUND}
[conversion-optimizer]   → Personas: {FOUND / NOT FOUND}
[conversion-optimizer] Step 3/6: Running 7-category audit...
[conversion-optimizer]   → 1. Message Match:   {SCORE}/100 (weighted: {W})
[conversion-optimizer]   → 2. CTA Effectiveness: {SCORE}/100 (weighted: {W})
[conversion-optimizer]   → 3. Trust & Proof:    {SCORE}/100 (weighted: {W})
[conversion-optimizer]   → 4. Page Speed:       {SCORE}/100 (weighted: {W})
[conversion-optimizer]   → 5. Mobile:           {SCORE}/100 (weighted: {W})
[conversion-optimizer]   → 6. Content Quality:  {SCORE}/100 (weighted: {W})
[conversion-optimizer]   → 7. Technical SEO:    {SCORE}/100 (weighted: {W})
[conversion-optimizer]   ══════════════════════════════════
[conversion-optimizer]   → TOTAL SCORE: {TOTAL}/100
[conversion-optimizer] Step 4/6: Generating fix recommendations...
[conversion-optimizer] Step 5/6: Creating A/B test suggestions...
[conversion-optimizer] Step 6/6: Saving report...
[conversion-optimizer] ✅ Complete → output/{PROJECT_NAME}/audit/optimization-report.md
```

After saving, tell the user:
```
Score: {TOTAL}/100 — {RATING}

{N} critical fixes, {N} quick wins, {N} nice-to-haves.
{N} A/B tests suggested.

Top priority: {MOST_CRITICAL_FIX}
```

## Error Handling

- **web_fetch unavailable or fails**: Ask user to paste HTML source. Process identically to fetched HTML.
- **URL returns non-HTML content**: Tell user the URL didn't return HTML. Ask for correct LP URL.
- **SPA/JavaScript-rendered page**: web_fetch may get empty body. Tell user to paste rendered HTML from browser DevTools.
- **No research outputs at all**: Proceed in standalone mode. All 7 categories still scored, message match uses generic quality check with reweighted scores.
- **Page is extremely short** (< 100 words): Flag as critical issue. Score content quality low. Still complete full audit.
- **Page is not a landing page** (has nav menu, multiple CTAs, blog layout): Note this in report header. Adjust expectations — audit still useful but some criteria don't apply.
- **Output directory cannot be created**: Report error, suggest checking file permissions.
