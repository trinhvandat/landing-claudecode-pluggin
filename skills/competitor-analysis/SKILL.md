---
name: competitor-analysis
description: "Crawl and analyze competitor landing pages to find patterns, strengths, weaknesses, and gaps. Use when user provides competitor URLs, says 'analyze competitor', 'check competition', 'competitor research', 'what are competitors doing', 'spy on competitors', 'competitive analysis', or wants to understand the competitive landscape before building a landing page."
---

# Competitor Analysis — Landing Page Intelligence

You are running the competitor-analysis skill. Your job: crawl competitor landing pages, score them on 6 dimensions, find patterns and gaps, and produce a swipe file of the best elements.

## Step 1: Gather Competitor URLs

You need 3-5 competitor URLs. Get them using this decision tree:

```
IF user provides URLs directly
  → Use those. Confirm the list with user before crawling.

IF user provides only keywords (no URLs)
  → web_search those keywords
  → Extract the top Google Ads results (sponsored listings) and top organic results
  → Present the list to user for confirmation

IF output/{PROJECT_NAME}/research/niche-brief.md exists
  → Read it. Use the top 3 keywords from the highest-priority cluster.
  → web_search those keywords
  → Extract competitor URLs from results
  → Present to user for confirmation

IF none of the above
  → Ask user: "Provide 3-5 competitor landing page URLs, or give me keywords to find them."
```

ALWAYS confirm the URL list with the user before crawling. Never crawl without consent.

## Step 2: Crawl Each Competitor

For each URL, use `web_fetch` to get the full HTML.

```
FOR EACH url IN competitor_urls:
  result = web_fetch(url)

  IF result succeeds
    → Extract HTML content
    → Run analysis (Step 3)

  IF result fails (timeout, blocked, 403, 404)
    → Try alternate URL: add/remove "www.", try "https" vs "http"
    → IF still fails → ask user:
      "Could not fetch {url}. Options:
       1. Paste the page HTML here (right-click → View Source → copy)
       2. Provide a different URL
       3. Skip this competitor"
    → Log the failure in the report: "❌ {url} — could not fetch (reason)"
    → Continue with remaining competitors

  IF web_fetch is completely unavailable (tool not available)
    → Tell user: "web_fetch is not available. To analyze competitors, I need you to:
       1. Open each URL in your browser
       2. Right-click → View Page Source
       3. Copy-paste the HTML here
       I'll analyze each one as you paste it."
    → Process pasted HTML through the same analysis pipeline
```

For each successfully fetched page, run `scripts/extract-page-structure.py` mentally or extract:
- All headings (h1-h6) with hierarchy
- All form fields (input names, types, count)
- All button/CTA text
- Total word count
- Number of distinct sections
- Framework detection (React, Next, WordPress, Wix, etc.)
- Analytics/GTM presence

## Step 3: Analyze Per Competitor

Score each competitor across 6 dimensions. Read `references/scoring-rubric.md` for detailed criteria.

```
ANALYSIS FRAMEWORK (score each 1-10):

MESSAGE
├── Headline clarity: Is the value prop immediately clear?
├── Value proposition strength: Unique? Compelling? Specific?
└── Keyword-headline match: Would this match a Google Ad?

STRUCTURE
├── Section count and flow: Logical progression?
├── Content length: Appropriate for the offer?
└── Above-fold content: What's visible without scrolling?

TRUST
├── Testimonials: Present? Real names/photos? Specific results?
├── Trust badges: Certifications, awards, guarantees?
├── Social proof: Numbers, client logos, review scores?
└── Risk reversal: Money-back guarantee? Free trial?

CTA
├── CTA copy: Action verb + benefit? Or just "Submit"?
├── CTA placement: Above fold? Repeated after proof?
├── Urgency/scarcity: Time limits? Limited spots?
└── Form friction: How many fields? Multi-step?

DESIGN
├── Color scheme: Professional? Consistent? CTA contrast?
├── Typography: Readable? Hierarchy clear?
├── Visual style: Modern/dated/playful/corporate?
└── Image usage: Real photos vs stock? Hero image quality?

TECH
├── Framework: What's it built with?
├── Speed signals: Script count, image optimization, lazy loading?
└── Mobile: Viewport meta? Responsive layout?
```

Read `references/analysis-framework.md` for what to look for in each dimension.

## Step 4: Cross-Competitor Comparison

After analyzing all competitors individually, find patterns:

**COMMON patterns** (what everyone does → these are table stakes, we MUST have them):
- List 3-5 elements that appear on all/most competitor pages

**DIFFERENTIATORS** (what only 1-2 do → potential competitive advantage):
- List elements unique to top-scoring competitors

**GAPS** (what NOBODY does → our biggest opportunity):
- List 2-3 things no competitor is doing well
- These become our landing page's unique strengths

## Step 5: Create Swipe File

Extract the single best element from each dimension across all competitors:

```
Best headline      → "{exact text}" — from {competitor}
Best CTA copy      → "{exact text}" — from {competitor}
Best trust approach → {describe it}  — from {competitor}
Best section layout → {describe it}  — from {competitor}
Best design element → {describe it}  — from {competitor}
Best above-fold    → {describe it}  — from {competitor}
```

Read `assets/swipe-file-template.md` for the output format.

Do NOT copy these verbatim into our landing page. They are inspiration. Our page must be original but learn from what works.

## Step 6: Generate Output

Fill templates and save:

```
output/{PROJECT_NAME}/research/competitor-report.md  ← Full analysis
output/{PROJECT_NAME}/research/swipe-file.md         ← Best elements collection
```

Read `assets/competitor-report-template.md` for the report format.

Show progress:
```
[competitor-analysis] Step 1/6: Gathering competitor URLs...
[competitor-analysis] Step 2/6: Crawling {N} competitor pages...
[competitor-analysis]   → Fetching {url}... ✅
[competitor-analysis]   → Fetching {url}... ❌ (fallback: user paste)
[competitor-analysis] Step 3/6: Analyzing each competitor...
[competitor-analysis] Step 4/6: Cross-competitor comparison...
[competitor-analysis] Step 5/6: Building swipe file...
[competitor-analysis] Step 6/6: Generating reports...
[competitor-analysis] ✅ Complete → output/{PROJECT_NAME}/research/competitor-report.md
```

After saving, tell the user:
```
Next steps:
- Run audience-persona: "Create personas for {PROJECT_NAME}"
- Review the swipe file for inspiration before design phase
```

## Error Handling

- **web_fetch unavailable**: Ask user to paste HTML source for each competitor. Process identically.
- **web_fetch blocked/timeout on specific URL**: Try URL variations → ask user for paste or alternate URL → skip with logged failure.
- **All competitors fail to load**: Ask user to paste at least 2 competitor pages. Cannot produce useful analysis with 0 pages.
- **niche-brief.md missing**: Not fatal — ask user for keywords or URLs directly. Add note: "Analysis performed without niche-brief context."
- **Competitor page is SPA (JavaScript-rendered)**: web_fetch may get empty body. Tell user: "This page uses JavaScript rendering. Please paste the rendered HTML (Inspect Element → copy outer HTML of body)."
