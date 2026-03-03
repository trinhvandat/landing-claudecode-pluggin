---
name: landing-page-builder
description: "Generate a complete, production-ready landing page from research and design inputs. Use when user says 'build landing page', 'create the page', 'generate landing page code', 'code the landing page', 'build the LP', 'make the page', or any request to produce the actual HTML/React/Astro code for a Google Ads landing page."
---

# Landing Page Builder — Code Generation from Research + Design

You are running the landing-page-builder skill. Your job: generate a complete, production-ready landing page from the project's research outputs and design system.

## Step 1: Validate Inputs Exist

```
REQUIRED (refuse to proceed without these):
  output/{PROJECT_NAME}/design-system/MASTER.md
  output/{PROJECT_NAME}/research/niche-brief.md

IF MASTER.md is missing
  → Stop: "⚠️ Required: output/{PROJECT_NAME}/design-system/MASTER.md
     → Run design-brief skill first: 'Create design system for {PROJECT_NAME}'"

IF niche-brief.md is missing
  → Stop: "⚠️ Required: output/{PROJECT_NAME}/research/niche-brief.md
     → Run niche-research skill first: 'Research keywords for {PROJECT_NAME}'"

RECOMMENDED (proceed with warning if missing):
  output/{PROJECT_NAME}/research/personas.md
  output/{PROJECT_NAME}/research/ad-copy-suggestions.md
  output/{PROJECT_NAME}/research/competitor-report.md

IF ad-copy-suggestions.md is missing
  → Warning: "No ad copy suggestions found. Headline will use the primary keyword from niche-brief.
     For best message match, run audience-persona first."

IF personas.md is missing
  → Warning: "No persona data. Pain points, objections, and FAQ will be generic."
```

Read ALL available inputs before generating any code.

## Step 2: Detect or Select Tech Stack

```
IF package.json exists in project root AND has "next" dependency → REACT/NEXT.JS
  → READ references/stack-guides/react-nextjs.md NOW
  → Component structure, App Router vs Pages, Tailwind integration

IF package.json exists AND has "astro" dependency → ASTRO
  → READ references/stack-guides/astro.md NOW
  → Island architecture, partial hydration, static-first

IF index.html exists OR no package.json → HTML + TAILWIND
  → READ references/stack-guides/html-tailwind.md NOW
  → Single-file, CDN-based, zero build step

ELSE → ASK user:
  "No tech stack detected. Which framework?
   1. HTML + Tailwind CSS (recommended — simplest, fastest)
   2. React / Next.js
   3. Astro
   4. Other (specify)"
  → Default to HTML + Tailwind if user doesn't respond.
```

## Step 3: Read Design System

Read `output/{PROJECT_NAME}/design-system/MASTER.md` and extract:

```
EXTRACT THESE (use defaults if not found):
  primary_color    → from MASTER.md colors section      (default: #2563EB)
  cta_color        → from MASTER.md CTA section         (default: #16A34A)
  bg_color         → from MASTER.md background          (default: #FFFFFF)
  text_color       → from MASTER.md text                (default: #1F2937)
  heading_font     → from MASTER.md typography           (default: Inter)
  body_font        → from MASTER.md typography           (default: Inter)
  google_fonts_url → from MASTER.md typography           (default: Inter URL)
  style_pattern    → from MASTER.md style                (default: modern-minimal)
  section_order    → from MASTER.md or LP pattern        (default: see Step 4)
```

IF a page-specific override exists at `design-system/pages/{ad-group}.md`:
  → Read it. Its rules override MASTER.md for this variant.

## Step 4: Build Section by Section

Generate code following this section order. Read `references/section-patterns.md` for detailed HTML/component patterns for each section.

```
SECTION ORDER (9 sections):

1. HEAD
   - Meta tags: title, description, OG, Twitter Card
   - Google Fonts preload for heading + body fonts
   - Critical CSS inline (above-fold styles)
   - GTM container snippet: placeholder {GTM_ID}
   - Favicon link
   - Viewport meta: width=device-width, initial-scale=1

2. HERO (above fold — most critical section)
   - Headline: EXACT text from ad-copy-suggestions.md headline 1
     IF ad-copy-suggestions.md missing → use primary keyword from niche-brief
   - Sub-headline: value proposition from personas (1-2 lines)
   - CTA button: from ad-copy-suggestions.md CTA variation 1
   - Hero image: <img> placeholder with correct aspect ratio + alt text
   - Trust badges: 3-4 small badges/logos above fold
   - NO navigation bar. NO hamburger menu. Zero navigation.
   - Add data-dki attribute to headline for Dynamic Keyword Insertion

3. PROBLEM / PAIN POINTS (PAS framework)
   - 3 pain points from persona pain_points
   - Each: icon placeholder + short title + 1-2 sentence description
   - Emotional language matching persona tone
   - IF no persona data → use 3 generic industry pain points

4. SOLUTION / BENEFITS
   - 3-4 benefits in feature → benefit format
   - Card or grid layout (responsive: 1 col mobile, 2-3 col desktop)
   - Each card: icon placeholder + title + description

5. SOCIAL PROOF
   - 2-3 testimonials: photo placeholder + quote + name + title
   - Stats bar: 3-4 metrics (e.g., "500+ khách hàng", "4.9/5 đánh giá")
   - Client/partner logo grid: 4-6 placeholder logos
   - Use real numbers from niche-brief or competitor benchmarks

6. HOW IT WORKS
   - 3 numbered steps with simple descriptions
   - Visual flow: step number + title + description
   - Reduces perceived complexity of the service/product

7. FAQ
   - 4-6 questions derived from persona objections
   - Accordion/toggle format (CSS-only or minimal JS)
   - Add FAQPage schema markup (see Step 5)
   - IF no persona data → use generic industry FAQ

8. FINAL CTA
   - Repeat primary CTA button
   - Add guarantee / risk reversal text
   - Optional urgency element (countdown placeholder, limited spots)

9. FOOTER (minimal)
   - Company name + address (for local businesses)
   - Legal links: Privacy Policy, Terms of Service
   - Phone number + email
   - NO navigation links — landing page stays distraction-free
```

### Critical Build Rules

```
RULE 1 — MESSAGE MATCH:
  Landing page h1 MUST match ad headline WORD FOR WORD.
  IF ad says "Trồng Răng Implant Không Đau"
  THEN <h1> says "Trồng Răng Implant Không Đau"
  NO paraphrasing. NO "improving". EXACT text.

RULE 2 — MOBILE FIRST:
  Code for 375px viewport FIRST, then add responsive breakpoints.
  Breakpoints: 375px → 768px → 1024px → 1440px (max-width)

RULE 3 — SINGLE CTA:
  ONE primary CTA on the page. Same button text everywhere it appears.
  No competing buttons. No "Learn More" alongside "Book Now".

RULE 4 — NO NAVIGATION:
  Zero nav bars. Zero hamburger menus. Zero header links.
  The ONLY clickable elements: CTA buttons, legal links in footer, phone number.

RULE 5 — ACCESSIBILITY:
  All images have alt text.
  CTA contrast ratio ≥ 4.5:1 against background.
  Touch targets ≥ 48px.
  Font size ≥ 16px for body text.
  Focus states on all interactive elements.
```

## Step 5: Google Ads Integration

Add these to the generated code. Read `references/google-ads-lp-rules.md` for implementation details.

### Dynamic Keyword Insertion (DKI)
```html
<!-- Elements with data-dki get text replaced by ?keyword= URL param -->
<h1 data-dki>{DEFAULT_HEADLINE}</h1>

<script>
  const params = new URLSearchParams(window.location.search);
  const kw = params.get('keyword');
  if (kw) {
    document.querySelectorAll('[data-dki]').forEach(el => {
      el.textContent = decodeURIComponent(kw);
    });
  }
</script>
```

### UTM Tracking
```html
<!-- Expected URL format:
  ?utm_source=google&utm_medium=cpc&utm_campaign={campaign}&utm_content={ad_group}
  &keyword={keyword}&gclid={gclid} -->
```

### Google Tag Manager
```html
<!-- GTM Head (in <head>) -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','{GTM_ID}');</script>

<!-- GTM Body (after <body>) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
```

### Conversion Tracking
```html
<!-- Fire on form submit or CTA click -->
<script>
  function trackConversion() {
    if (typeof gtag !== 'undefined') {
      gtag('event', 'conversion', {
        send_to: '{CONVERSION_ID}/{CONVERSION_LABEL}'
      });
    }
  }
</script>
```

### Schema Markup
```
REQUIRED schemas:
  FAQPage      → from FAQ section (always include)
  LocalBusiness → IF service has physical location
  Product      → IF selling a specific product
  Organization → IF company/brand page

Generate as <script type="application/ld+json"> in <head>.
```

## Step 6: Performance Optimization

```
IMAGES:
  Hero image: loading="eager" (above fold)
  All other images: loading="lazy"
  Use width + height attributes to prevent layout shift
  Suggest WebP format in alt text comment

FONTS:
  <link rel="preload"> for primary font file
  font-display: swap on @font-face
  Max 2 font families loaded

CSS:
  Critical CSS (above-fold styles) inline in <head>
  Non-critical CSS: loaded via <link> with media="print" onload trick
  OR all CSS inline for single-file simplicity (HTML+Tailwind)

JAVASCRIPT:
  Minimal JS — only for: FAQ accordion, DKI, conversion tracking
  All scripts: defer or at end of body
  No jQuery. No heavy frameworks for static LP.
  FAQ accordion: prefer CSS-only (<details>/<summary>) or minimal vanilla JS

HTML:
  Semantic tags: <header>, <main>, <section>, <footer>, <article>
  No unnecessary wrapper divs
  IDs on sections for potential anchor linking
```

## Step 7: Pre-Delivery Checklist

Before saving, verify ALL items. Fix any failures before delivering.

```
MESSAGE MATCH:
  [ ] h1 matches ad copy headline word-for-word
  [ ] Primary keyword appears in first 100 words

CTA:
  [ ] CTA visible above fold at 375px
  [ ] CTA button color contrasts at 4.5:1 ratio
  [ ] CTA repeated at least 3 times (hero, after proof, final)
  [ ] CTA text is action verb + benefit

MOBILE:
  [ ] Viewport meta tag present
  [ ] Responsive at 375px, 768px, 1024px, 1440px
  [ ] Touch targets ≥ 48px
  [ ] Font size ≥ 16px body
  [ ] Single column on mobile

STRUCTURE:
  [ ] No navigation menu / no header links
  [ ] All 9 sections present
  [ ] FAQ uses accordion format

ACCESSIBILITY:
  [ ] All images have alt text
  [ ] Focus states on interactive elements
  [ ] Semantic HTML tags used

SEO & TRACKING:
  [ ] <title> and <meta description> present
  [ ] OG + Twitter Card meta tags
  [ ] FAQPage schema markup
  [ ] GTM placeholder present ({GTM_ID})
  [ ] Conversion tracking placeholder present
  [ ] Favicon linked

PERFORMANCE:
  [ ] Hero image: loading="eager", others: loading="lazy"
  [ ] Font preloaded
  [ ] < 5 script tags
  [ ] Page works without JavaScript (progressive enhancement)

CODE QUALITY:
  [ ] HTML validates (no unclosed tags)
  [ ] No inline styles (unless critical CSS)
  [ ] Consistent class naming
```

IF any item fails → fix it before saving. Show the checklist results to user.

## Step 8: Output

Save generated code:

```
FOR html-tailwind:
  output/{PROJECT_NAME}/src/index.html

FOR react-nextjs:
  output/{PROJECT_NAME}/src/app/page.tsx
  output/{PROJECT_NAME}/src/app/layout.tsx
  output/{PROJECT_NAME}/src/components/Hero.tsx
  output/{PROJECT_NAME}/src/components/...

FOR astro:
  output/{PROJECT_NAME}/src/pages/index.astro
  output/{PROJECT_NAME}/src/layouts/LandingLayout.astro
  output/{PROJECT_NAME}/src/components/...
```

Also generate:
```
output/{PROJECT_NAME}/landing-page-checklist.md  ← checklist results from Step 7
```

Show progress:
```
[landing-page-builder] Step 1/8: Validating inputs...
[landing-page-builder] Step 2/8: Detecting tech stack... → {STACK}
[landing-page-builder] Step 3/8: Reading design system...
[landing-page-builder] Step 4/8: Building sections... (1/9 HEAD)
[landing-page-builder]   → 2/9 HERO ✅
[landing-page-builder]   → 3/9 PAIN POINTS ✅
[landing-page-builder]   → ... (each section)
[landing-page-builder]   → 9/9 FOOTER ✅
[landing-page-builder] Step 5/8: Adding Google Ads integration...
[landing-page-builder] Step 6/8: Optimizing performance...
[landing-page-builder] Step 7/8: Running pre-delivery checklist...
[landing-page-builder]   → 18/18 checks passed ✅
[landing-page-builder] Step 8/8: Saving output...
[landing-page-builder] ✅ Complete → output/{PROJECT_NAME}/src/index.html
```

After saving, tell the user:
```
Next steps:
- Preview the page: open output/{PROJECT_NAME}/src/index.html in browser
- Run conversion-optimizer: "Audit landing page for {PROJECT_NAME}"
- Replace placeholders: {GTM_ID}, {CONVERSION_ID}, hero image, testimonial photos
- Test on actual mobile device at 375px width
```

## Error Handling

- **MASTER.md or niche-brief.md missing**: STOP. Show specific error with skill to run first.
- **Ad copy suggestions missing**: Proceed — use primary keyword from niche-brief as headline. Warn about message match risk.
- **Personas missing**: Proceed — use generic pain points and FAQ. Warn that content will be less targeted.
- **Tech stack unclear**: Default to HTML+Tailwind. Ask user only if multiple signals conflict.
- **Design system incomplete** (missing colors/fonts): Use defaults (blue primary, green CTA, Inter font). Note in checklist.
- **Checklist item fails**: Fix automatically if possible. If not fixable (e.g., contrast ratio), flag to user with specific recommendation.
- **Output directory cannot be created**: Report error, suggest checking file permissions.
