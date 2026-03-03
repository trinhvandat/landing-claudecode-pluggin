# Stack Guide: Astro

Use this guide when the project has Astro detected (package.json contains "astro" or astro.config.* exists).

## When to Use
- Zero JS by default — fastest possible page load
- Content-focused landing pages
- When page speed is the #1 priority
- Islands architecture for selective interactivity (form, FAQ)

## File Structure
```
output/{PROJECT_NAME}/src/
├── pages/
│   └── index.astro              ← landing page
├── layouts/
│   └── LandingLayout.astro      ← shared layout (head, GTM, fonts)
├── components/
│   ├── Hero.astro
│   ├── PainPoints.astro
│   ├── Benefits.astro
│   ├── SocialProof.astro
│   ├── HowItWorks.astro
│   ├── FAQ.astro                ← static (details/summary, no JS needed)
│   ├── FinalCTA.astro
│   ├── Footer.astro
│   └── CTAButton.astro
└── styles/
    └── global.css
```

## Layout (LandingLayout.astro)

```astro
---
interface Props {
  title: string;
  description: string;
  ogImage?: string;
}

const { title, description, ogImage = '/og-image.jpg' } = Astro.props;
---

<!DOCTYPE html>
<html lang="{LANGUAGE_CODE}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content={description}>

  <!-- OG Tags -->
  <meta property="og:title" content={title}>
  <meta property="og:description" content={description}>
  <meta property="og:image" content={ogImage}>
  <meta property="og:type" content="website">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content={title}>
  <meta name="twitter:description" content={description}>

  <!-- Favicon -->
  <link rel="icon" href="/favicon.ico">

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{GOOGLE_FONTS_URL}&display=swap" rel="stylesheet">

  <!-- GTM -->
  <script is:inline>
    (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','{GTM_ID}');
  </script>

  <!-- Schema -->
  <script type="application/ld+json" set:html={JSON.stringify(schemaData)} />
</head>
<body class="font-body antialiased">
  <!-- GTM noscript -->
  <noscript>
    <iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}"
      height="0" width="0" style="display:none;visibility:hidden"></iframe>
  </noscript>

  <slot />
</body>
</html>
```

## Page (pages/index.astro)

```astro
---
import LandingLayout from '../layouts/LandingLayout.astro';
import Hero from '../components/Hero.astro';
import PainPoints from '../components/PainPoints.astro';
import Benefits from '../components/Benefits.astro';
import SocialProof from '../components/SocialProof.astro';
import HowItWorks from '../components/HowItWorks.astro';
import FAQ from '../components/FAQ.astro';
import FinalCTA from '../components/FinalCTA.astro';
import Footer from '../components/Footer.astro';
---

<LandingLayout
  title="{PAGE_TITLE} | {BUSINESS_NAME}"
  description="{META_DESCRIPTION}">

  <main>
    <Hero />
    <PainPoints />
    <Benefits />
    <SocialProof />
    <HowItWorks />
    <FAQ />
    <FinalCTA />
    <Footer />
  </main>
</LandingLayout>
```

## DKI in Astro

Since Astro ships zero JS by default, DKI needs a small inline script:

```astro
<!-- In Hero.astro -->
<h1 data-dki>{DEFAULT_HEADLINE}</h1>

<script is:inline>
  (function() {
    var params = new URLSearchParams(window.location.search);
    var kw = params.get('keyword');
    if (kw) {
      document.querySelectorAll('[data-dki]').forEach(function(el) {
        el.textContent = decodeURIComponent(kw);
      });
    }
  })();
</script>
```

Use `is:inline` to prevent Astro from bundling — keeps it small and immediate.

## Astro + Tailwind Setup

```bash
# If starting fresh
npx astro add tailwind
```

```javascript
// astro.config.mjs
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  integrations: [tailwind()],
  output: 'static',  // Landing pages are always static
});
```

## Performance Advantages

Astro ships ZERO JavaScript by default. This means:
- No framework runtime (~0KB JS vs ~80KB+ for React)
- Instant FCP and LCP
- Perfect Lighthouse performance scores
- Only send JS for interactive islands (form validation, DKI)

### What Needs JS (use `is:inline` for tiny scripts)
- DKI headline replacement (~200 bytes)
- UTM parameter capture (~300 bytes)
- Conversion tracking (~200 bytes)
- FAQ accordion: use `<details>/<summary>` (no JS needed)

### What Does NOT Need JS
- All content sections (static HTML)
- Testimonials
- Stats bar
- Image rendering
- Footer

## Do / Don't

| Do | Don't |
|----|-------|
| Use `.astro` components (zero JS) | Use React/Vue components unless interactive |
| Use `is:inline` for small scripts | Bundle large JS files |
| Use `<details>/<summary>` for FAQ | Import a JS accordion library |
| Set `output: 'static'` | Use SSR for a landing page |
| Use Astro Image integration | Use raw `<img>` without optimization |
| Prerender everything | Use client-side routing |
