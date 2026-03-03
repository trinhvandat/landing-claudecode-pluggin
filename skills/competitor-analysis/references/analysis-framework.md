# Competitor Analysis Framework

Reference for Step 3 of the competitor-analysis skill. Use this to know WHAT to look for in each dimension.

## Dimension 1: MESSAGE

### Headline Clarity (1-10)
- **10**: Instantly clear what the page offers. Specific benefit in < 10 words.
- **7-9**: Clear offer but could be more specific or compelling.
- **4-6**: Vague or generic. Could apply to any business in the niche.
- **1-3**: Confusing, missing, or misleading headline.

What to extract:
- Exact h1 text
- Whether h1 contains the primary keyword
- Word count of h1 (ideal: 5-12 words)

### Value Proposition Strength (1-10)
- **10**: Unique, specific, quantified. "500+ patients treated with 98% success rate"
- **7-9**: Clear benefit but not unique. Could be any competitor.
- **4-6**: Features listed, not benefits. "We have modern equipment."
- **1-3**: No discernible value proposition.

What to extract:
- The core promise (1 sentence)
- Whether it's quantified (numbers, percentages, timeframes)
- Whether it's unique vs generic

### Keyword-Headline Match (1-10)
- **10**: Headline would perfectly match a Google Ad headline for the target keyword.
- **7-9**: Close match — same topic, slightly different wording.
- **4-6**: Related but not a direct match. Would lower Quality Score.
- **1-3**: No relationship between likely ad keywords and page headline.

What to extract:
- Likely Google Ads keywords this page targets
- Whether the h1 contains those keywords verbatim

## Dimension 2: STRUCTURE

### Section Count and Flow
What to extract:
- Total number of distinct sections (separated by visual breaks or `<section>` tags)
- Section order (list them: Hero → Benefits → Testimonials → etc.)
- Whether the flow follows a known framework:
  - **PAS**: Problem → Agitation → Solution
  - **AIDA**: Attention → Interest → Desire → Action
  - **BAB**: Before → After → Bridge

Ideal section count: 6-10 for lead gen, 8-15 for e-commerce.

### Content Length
What to extract:
- Total word count (use extract-page-structure.py)
- Words above the fold (first ~300px of content)

Benchmarks:
```
Short landing page:  300-600 words   — for simple offers, low-cost products
Medium:              600-1500 words  — most lead gen pages
Long:                1500-3000 words — high-ticket, complex services
Very long:           3000+ words     — only for very high-ticket / educational
```

### Above-Fold Content Quality (1-10)
What's visible without scrolling on a 375px mobile viewport:
- **10**: Headline + value prop + CTA + trust signal all visible.
- **7-9**: Headline + CTA visible, trust signal below fold.
- **4-6**: Only headline visible. CTA requires scrolling.
- **1-3**: Large image/video dominates. No clear message above fold.

## Dimension 3: TRUST

### Testimonials (1-10)
- **10**: 3+ testimonials with real photos, full names, titles, specific results.
- **7-9**: Testimonials present with names but no photos or vague outcomes.
- **4-6**: Generic quotes with first names only. "Rất hài lòng — Anh T."
- **1-3**: No testimonials, or clearly fake/stock photo testimonials.

### Trust Badges (1-10)
- **10**: Relevant certifications, awards, partner logos, verified review badges.
- **7-9**: Some badges but not highly relevant (generic SSL, payment icons).
- **4-6**: Only 1 badge or certifications that seem self-awarded.
- **1-3**: No trust badges at all.

What to look for:
- Industry certifications (ISO, medical licenses, professional associations)
- Review platform badges (Google Reviews, TrustPilot)
- Partner/client logos
- "As seen in" media mentions
- Years in business / number of customers

### Social Proof (1-10)
- **10**: Specific numbers ("2,847 khách hàng", "4.9/5 trên Google"), client logos, case studies.
- **7-9**: Numbers present but round/vague ("hàng nghìn khách hàng").
- **4-6**: Claims without evidence ("được nhiều người tin tưởng").
- **1-3**: No social proof elements.

### Risk Reversal (1-10)
- **10**: Clear guarantee with specifics ("hoàn tiền 100% trong 30 ngày").
- **7-9**: Guarantee mentioned but vague.
- **4-6**: Implied safety ("cam kết chất lượng") without specific guarantee.
- **1-3**: No risk reversal. Buyer assumes all risk.

## Dimension 4: CTA

### CTA Copy (1-10)
- **10**: Action verb + specific benefit: "Đặt Lịch Tư Vấn Miễn Phí"
- **7-9**: Action verb but generic benefit: "Đăng Ký Ngay"
- **4-6**: Weak verb: "Tìm Hiểu Thêm", "Gửi"
- **1-3**: No CTA, or just "Submit" / "Gửi"

What to extract:
- Exact CTA button text (all buttons on the page)
- Button color (hex if possible, or description)

### CTA Placement (1-10)
- **10**: Above fold + after social proof + at page end. 3+ instances.
- **7-9**: Above fold + 1 more placement.
- **4-6**: Only 1 CTA on the entire page, or only below fold.
- **1-3**: CTA hidden, hard to find, or requires scrolling past many sections.

### Urgency/Scarcity (1-10)
- **10**: Real, specific urgency: "Ưu đãi đến 15/03", countdown timer with real deadline.
- **7-9**: Moderate urgency: "Số lượng có hạn", "Đăng ký hôm nay".
- **4-6**: Weak urgency: "Liên hệ ngay" (always available).
- **1-3**: No urgency elements at all.

### Form Friction (1-10, inverse — fewer fields = higher score)
- **10**: 1-2 fields (name + phone). Minimal barrier.
- **7-9**: 3 fields (name + phone + email). Acceptable.
- **4-6**: 4-5 fields. Starting to lose conversions.
- **1-3**: 6+ fields, or asks for sensitive info upfront (address, ID number).

What to extract:
- Number of form fields
- Field names and types
- Whether form is multi-step
- Required vs optional fields

## Dimension 5: DESIGN

### Color Scheme
What to extract:
- Primary brand color (hex or description)
- CTA button color (MUST note contrast against background)
- Background color (white/dark/colored)
- Overall palette impression: professional, playful, clinical, luxury

### Typography
What to extract:
- Font family (if identifiable from CSS or visual inspection)
- Serif vs sans-serif
- Headline weight (bold/light/regular)
- Body text size (appears readable? too small?)

### Visual Style
Categorize as one of:
- **Modern minimal**: lots of whitespace, clean lines, flat design
- **Corporate professional**: structured, formal, blues/grays
- **Playful/friendly**: rounded shapes, bright colors, illustrations
- **Luxury/premium**: dark backgrounds, gold accents, serif fonts
- **Clinical/medical**: white, clean, trust-focused, medical imagery
- **Aggressive sales**: red accents, urgency banners, busy layout

### Image Usage
What to extract:
- Hero image type: real photo / stock / illustration / none
- People in images: yes/no, real staff or stock models
- Image count on entire page
- Alt text present: yes/no (accessibility and SEO signal)

## Dimension 6: TECH

### Framework Detection
Look for these signals in HTML source:
```
React/Next.js → __next div, _next/ in script paths, __NEXT_DATA__
Vue/Nuxt      → __nuxt, _nuxt/ in paths, data-v- attributes
WordPress     → wp-content/, wp-includes/, generator meta tag
Wix           → wix.com in scripts, _wixCIDX
Squarespace   → squarespace.com in scripts, .sqs-block classes
Shopify       → cdn.shopify.com, Shopify.theme
Webflow       → webflow.com in scripts, w-embed classes
Static HTML   → none of the above, simple HTML structure
```

### Page Speed Indicators
What to extract:
- Total `<script>` tag count (< 5 is good, > 10 is concerning)
- Image count and whether they use `loading="lazy"`
- CSS approach: inline critical CSS? External stylesheet count?
- Font loading: preload? display=swap?

### Mobile Readiness
What to extract:
- `<meta name="viewport">` present? (REQUIRED for mobile)
- Responsive meta content correct? (`width=device-width, initial-scale=1`)
- Any fixed-width elements visible in source?
