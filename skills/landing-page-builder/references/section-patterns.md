# Section Patterns — HTML Structure Reference

Reference for Step 4 of the landing-page-builder skill. Contains HTML structure patterns for each of the 9 landing page sections.

> These are STRUCTURE patterns, not styled components. Apply design system colors/fonts/spacing on top.

## Section 1: HEAD

```html
<!DOCTYPE html>
<html lang="{LANGUAGE_CODE}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{PAGE_TITLE} | {BUSINESS_NAME}</title>
  <meta name="description" content="{META_DESCRIPTION}">

  <!-- OG Tags -->
  <meta property="og:title" content="{PAGE_TITLE}">
  <meta property="og:description" content="{META_DESCRIPTION}">
  <meta property="og:image" content="{OG_IMAGE_URL}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{PAGE_URL}">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{PAGE_TITLE}">
  <meta name="twitter:description" content="{META_DESCRIPTION}">
  <meta name="twitter:image" content="{OG_IMAGE_URL}">

  <!-- Favicon -->
  <link rel="icon" href="/favicon.ico" type="image/x-icon">

  <!-- Google Fonts Preload -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" as="style" href="{GOOGLE_FONTS_URL}">
  <link rel="stylesheet" href="{GOOGLE_FONTS_URL}">

  <!-- GTM (replace {GTM_ID}) -->
  <script><!-- GTM snippet here --></script>

  <!-- Critical CSS (inline above-fold styles) -->
  <style>
    /* Reset + above-fold styles here */
  </style>

  <!-- Schema Markup -->
  <script type="application/ld+json">
    {SCHEMA_JSON}
  </script>
</head>
```

## Section 2: HERO

```html
<header id="hero">
  <!-- NO <nav> — landing pages have zero navigation -->

  <div class="hero-container">
    <!-- Trust badges row (above headline on mobile) -->
    <div class="trust-badges">
      <img src="/img/badge-1.svg" alt="{BADGE_1_DESC}" width="80" height="40">
      <img src="/img/badge-2.svg" alt="{BADGE_2_DESC}" width="80" height="40">
      <img src="/img/badge-3.svg" alt="{BADGE_3_DESC}" width="80" height="40">
    </div>

    <div class="hero-content">
      <!-- h1 MUST match ad headline exactly -->
      <h1 data-dki>{EXACT_AD_HEADLINE}</h1>
      <p class="sub-headline">{VALUE_PROPOSITION}</p>

      <!-- Primary CTA — first instance -->
      <a href="#form" class="cta-button">{CTA_TEXT}</a>
    </div>

    <div class="hero-image">
      <img src="/img/hero.webp" alt="{DESCRIPTIVE_ALT_TEXT}"
           width="600" height="400" loading="eager">
    </div>
  </div>
</header>
```

Key rules:
- h1 is the ONLY h1 on the entire page
- CTA links to `#form` or `#contact` section
- Hero image: `loading="eager"` (above fold)
- Trust badges: small, non-intrusive, real credentials

## Section 3: PAIN POINTS (PAS: Problem + Agitation)

```html
<section id="pain-points">
  <h2>{SECTION_TITLE}</h2>

  <div class="pain-grid">
    <div class="pain-card">
      <div class="pain-icon"><!-- icon placeholder --></div>
      <h3>{PAIN_POINT_1_TITLE}</h3>
      <p>{PAIN_POINT_1_DESCRIPTION}</p>
    </div>

    <div class="pain-card">
      <div class="pain-icon"><!-- icon placeholder --></div>
      <h3>{PAIN_POINT_2_TITLE}</h3>
      <p>{PAIN_POINT_2_DESCRIPTION}</p>
    </div>

    <div class="pain-card">
      <div class="pain-icon"><!-- icon placeholder --></div>
      <h3>{PAIN_POINT_3_TITLE}</h3>
      <p>{PAIN_POINT_3_DESCRIPTION}</p>
    </div>
  </div>
</section>
```

Layout: 1 column on mobile (375px), 3 columns on desktop (1024px+).

## Section 4: BENEFITS / SOLUTION

```html
<section id="benefits">
  <h2>{SECTION_TITLE}</h2>
  <p class="section-subtitle">{BRIEF_INTRO}</p>

  <div class="benefits-grid">
    <div class="benefit-card">
      <div class="benefit-icon"><!-- icon placeholder --></div>
      <h3>{FEATURE_AS_BENEFIT_1}</h3>
      <p>{EXPLANATION}</p>
    </div>
    <!-- Repeat for 3-4 benefits -->
  </div>
</section>
```

Feature → Benefit format:
- BAD: "Modern equipment" (feature)
- GOOD: "Painless treatment with latest technology" (benefit)

## Section 5: SOCIAL PROOF

```html
<section id="social-proof">
  <h2>{SECTION_TITLE}</h2>

  <!-- Stats bar -->
  <div class="stats-bar">
    <div class="stat">
      <span class="stat-number">{NUMBER}</span>
      <span class="stat-label">{LABEL}</span>
    </div>
    <!-- 3-4 stats -->
  </div>

  <!-- Testimonials -->
  <div class="testimonials">
    <div class="testimonial-card">
      <img src="/img/testimonial-1.webp" alt="Photo of {NAME}"
           width="64" height="64" loading="lazy" class="testimonial-photo">
      <blockquote>"{QUOTE}"</blockquote>
      <cite>
        <strong>{FULL_NAME}</strong>
        <span>{TITLE_OR_CONTEXT}</span>
      </cite>
    </div>
    <!-- 2-3 testimonials -->
  </div>

  <!-- Client logos -->
  <div class="client-logos">
    <img src="/img/logo-1.svg" alt="{CLIENT_NAME}" width="120" height="40" loading="lazy">
    <!-- 4-6 logos -->
  </div>

  <!-- CTA — second instance (after social proof) -->
  <a href="#form" class="cta-button">{CTA_TEXT}</a>
</section>
```

## Section 6: HOW IT WORKS

```html
<section id="how-it-works">
  <h2>{SECTION_TITLE}</h2>

  <div class="steps">
    <div class="step">
      <span class="step-number">1</span>
      <h3>{STEP_1_TITLE}</h3>
      <p>{STEP_1_DESCRIPTION}</p>
    </div>

    <div class="step">
      <span class="step-number">2</span>
      <h3>{STEP_2_TITLE}</h3>
      <p>{STEP_2_DESCRIPTION}</p>
    </div>

    <div class="step">
      <span class="step-number">3</span>
      <h3>{STEP_3_TITLE}</h3>
      <p>{STEP_3_DESCRIPTION}</p>
    </div>
  </div>
</section>
```

## Section 7: FAQ

```html
<section id="faq">
  <h2>{SECTION_TITLE}</h2>

  <div class="faq-list">
    <!-- CSS-only accordion using details/summary (no JS needed) -->
    <details class="faq-item">
      <summary>{QUESTION_1}</summary>
      <p>{ANSWER_1}</p>
    </details>

    <details class="faq-item">
      <summary>{QUESTION_2}</summary>
      <p>{ANSWER_2}</p>
    </details>

    <!-- 4-6 questions from persona objections -->
  </div>
</section>
```

Prefer `<details>/<summary>` over JavaScript accordion — works without JS, accessible by default.

## Section 8: FINAL CTA

```html
<section id="contact">
  <h2>{FINAL_CTA_HEADING}</h2>
  <p>{GUARANTEE_OR_RISK_REVERSAL}</p>

  <!-- For lead gen: form -->
  <form action="{FORM_ACTION}" method="POST" onsubmit="trackConversion()">
    <input type="text" name="name" placeholder="{NAME_PLACEHOLDER}" required
           autocomplete="name" aria-label="{NAME_LABEL}">
    <input type="tel" name="phone" placeholder="{PHONE_PLACEHOLDER}" required
           autocomplete="tel" aria-label="{PHONE_LABEL}">
    <input type="email" name="email" placeholder="{EMAIL_PLACEHOLDER}"
           autocomplete="email" aria-label="{EMAIL_LABEL}">

    <!-- UTM hidden fields -->
    <input type="hidden" name="utm_source" value="">
    <input type="hidden" name="utm_medium" value="">
    <input type="hidden" name="utm_campaign" value="">
    <input type="hidden" name="utm_content" value="">
    <input type="hidden" name="utm_term" value="">
    <input type="hidden" name="gclid" value="">

    <button type="submit" class="cta-button">{CTA_TEXT}</button>
  </form>

  <!-- Optional urgency element -->
  <p class="urgency">{URGENCY_TEXT}</p>
</section>
```

Form rules:
- Max 3 fields for cold traffic (name + phone + email)
- Single column on mobile
- Submit button: full-width on mobile, same color as CTA
- All fields have `autocomplete` attributes
- All fields have `aria-label` for accessibility

## Section 9: FOOTER

```html
<footer id="footer">
  <div class="footer-content">
    <p class="business-info">
      <strong>{BUSINESS_NAME}</strong><br>
      {ADDRESS}<br>
      <a href="tel:{PHONE}">{PHONE_DISPLAY}</a> |
      <a href="mailto:{EMAIL}">{EMAIL}</a>
    </p>
    <p class="legal">
      <a href="/privacy">Privacy Policy</a> |
      <a href="/terms">Terms of Service</a>
    </p>
    <p class="copyright">&copy; {YEAR} {BUSINESS_NAME}. All rights reserved.</p>
  </div>
</footer>
```

Footer rules:
- NO navigation links
- Phone number is clickable (`tel:`)
- Legal links are required for Google Ads policy compliance
- Copyright year: use current year

## Responsive Breakpoints

```css
/* Mobile first — 375px is the default */

/* Tablet */
@media (min-width: 768px) {
  /* 2-column grids, larger typography */
}

/* Desktop */
@media (min-width: 1024px) {
  /* 3-column grids, hero side-by-side layout */
}

/* Large desktop */
@media (min-width: 1440px) {
  /* Max-width container, prevent over-stretching */
  .container { max-width: 1200px; margin: 0 auto; }
}
```
