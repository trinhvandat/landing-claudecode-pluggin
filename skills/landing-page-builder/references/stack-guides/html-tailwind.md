# Stack Guide: HTML + Tailwind CSS

Use this guide when building a landing page as a single HTML file with Tailwind CSS.

## When to Use
- No build step needed — simplest deployment
- Client just needs an HTML file to host
- Quick prototypes and MVPs
- Static landing pages with no dynamic data

## File Structure
```
output/{PROJECT_NAME}/src/
└── index.html          ← single file, everything inline
```

## Tailwind Setup (CDN — Zero Build)

```html
<!-- In <head> — Tailwind Play CDN -->
<script src="https://cdn.tailwindcss.com"></script>
<script>
  tailwind.config = {
    theme: {
      extend: {
        colors: {
          primary: '{PRIMARY_COLOR}',
          cta: '{CTA_COLOR}',
        },
        fontFamily: {
          heading: ['{HEADING_FONT}', 'sans-serif'],
          body: ['{BODY_FONT}', 'sans-serif'],
        },
      },
    },
  }
</script>
```

### For Production (if user wants optimized CSS)
Recommend switching from CDN to Tailwind CLI:
```bash
npx tailwindcss -i ./input.css -o ./output.css --minify
```

## Key Tailwind Classes for LP Sections

### Hero
```html
<header class="min-h-screen flex items-center px-4 py-12 md:py-0">
  <div class="max-w-6xl mx-auto grid md:grid-cols-2 gap-8 items-center">
    <div>
      <h1 class="text-3xl md:text-5xl font-heading font-bold text-gray-900 leading-tight" data-dki>
        {HEADLINE}
      </h1>
      <p class="mt-4 text-lg text-gray-600 font-body">
        {SUB_HEADLINE}
      </p>
      <a href="#contact" class="mt-6 inline-block bg-cta text-white px-8 py-4 rounded-lg text-lg font-semibold hover:opacity-90 transition-opacity">
        {CTA_TEXT}
      </a>
    </div>
    <div>
      <img src="/img/hero.webp" alt="{ALT}" width="600" height="400" loading="eager"
           class="rounded-xl shadow-lg w-full h-auto">
    </div>
  </div>
</header>
```

### CTA Button (reusable pattern)
```html
<!-- Primary CTA — use everywhere -->
<a href="#contact"
   class="inline-block bg-cta text-white px-8 py-4 rounded-lg text-lg font-semibold
          hover:opacity-90 transition-opacity focus:outline-none focus:ring-2
          focus:ring-offset-2 focus:ring-cta min-h-[48px] min-w-[48px]">
  {CTA_TEXT}
</a>
```

### Cards Grid (pain points, benefits)
```html
<div class="grid grid-cols-1 md:grid-cols-3 gap-6">
  <div class="p-6 rounded-xl bg-white shadow-md">
    <!-- icon + h3 + p -->
  </div>
</div>
```

### FAQ Accordion
```html
<details class="border-b border-gray-200 py-4 group">
  <summary class="flex justify-between items-center cursor-pointer text-lg font-semibold
                  text-gray-900 list-none">
    {QUESTION}
    <svg class="w-5 h-5 transition-transform group-open:rotate-180" ...></svg>
  </summary>
  <p class="mt-3 text-gray-600 leading-relaxed">{ANSWER}</p>
</details>
```

### Form
```html
<form class="max-w-md mx-auto space-y-4" action="{ACTION}" method="POST"
      onsubmit="trackConversion()">
  <input type="text" name="name" placeholder="{PLACEHOLDER}" required
         autocomplete="name" aria-label="{LABEL}"
         class="w-full px-4 py-3 border border-gray-300 rounded-lg text-base
                focus:outline-none focus:ring-2 focus:ring-primary">
  <!-- more fields -->
  <button type="submit"
          class="w-full bg-cta text-white py-4 rounded-lg text-lg font-semibold
                 hover:opacity-90 transition-opacity min-h-[48px]">
    {CTA_TEXT}
  </button>
</form>
```

## Performance Tips

1. **Tailwind CDN is large** (~300KB) — fine for development, but for production recommend:
   - Tailwind CLI with `--minify` to tree-shake unused classes
   - Or inline only the CSS classes actually used

2. **Single file advantage**: no HTTP requests for CSS/JS (except CDN + fonts)

3. **Font optimization**:
   ```html
   <link rel="preconnect" href="https://fonts.googleapis.com">
   <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
   <link href="{GOOGLE_FONTS_URL}&display=swap" rel="stylesheet">
   ```

4. **Image optimization**: recommend user converts images to WebP before deploying

## Do / Don't

| Do | Don't |
|----|-------|
| Use Tailwind utility classes | Write custom CSS (unless critical CSS) |
| Use `class` for all styling | Use inline `style` attributes |
| Use responsive prefixes (`md:`, `lg:`) | Use `@media` in custom CSS |
| Set colors in tailwind.config | Hardcode hex values in classes |
| Use `<details>/<summary>` for FAQ | Import a JS accordion library |
| Use semantic HTML (`<header>`, `<section>`) | Use `<div>` for everything |
