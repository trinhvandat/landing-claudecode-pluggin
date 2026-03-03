# Google Ads Landing Page Rules

Reference for Step 5 of the landing-page-builder skill. These are conversion-critical requirements.

## Message Match — The #1 Rule

```
Ad Headline  ═══must match═══►  Landing Page <h1>

EXACT. WORD. FOR. WORD.

WHY: Google's Quality Score algorithm checks headline relevance.
  - Match → higher Quality Score → lower CPC → more impressions
  - Mismatch → lower Quality Score → higher CPC → wasted budget
  - Mismatch also increases bounce rate (user expected X, got Y)
```

### Implementation
```html
<!-- The h1 text must come from ad-copy-suggestions.md, Headline 1 -->
<h1 data-dki>Trồng Răng Implant Không Đau</h1>

<!-- data-dki enables Dynamic Keyword Insertion override via URL param -->
```

## Dynamic Keyword Insertion (DKI)

DKI lets Google Ads replace the headline with the user's actual search query for better relevance.

### How It Works
1. Google Ads inserts the search keyword into the ad headline
2. The ad links to `landing-page.com?keyword={keyword}`
3. JavaScript on the LP reads the `keyword` param and replaces `[data-dki]` text

### Implementation
```html
<script>
  // DKI: Replace headline with keyword from Google Ads URL param
  (function() {
    var params = new URLSearchParams(window.location.search);
    var kw = params.get('keyword');
    if (kw) {
      var decoded = decodeURIComponent(kw);
      document.querySelectorAll('[data-dki]').forEach(function(el) {
        el.textContent = decoded;
      });
    }
  })();
</script>
```

### Rules
- ONLY apply DKI to the h1 (and optionally the meta title)
- The `data-dki` attribute marks elements that can be replaced
- The default text (without ?keyword=) must be the ad headline
- DKI text should NOT break the layout (test with long keywords)
- Sanitize: `decodeURIComponent` is sufficient for display-only text
- Do NOT use `innerHTML` — textContent only (XSS prevention)

## UTM Tracking Parameters

### Expected URL Format
```
https://example.com/landing-page
  ?utm_source=google
  &utm_medium=cpc
  &utm_campaign={campaign_name}
  &utm_content={ad_group}
  &utm_term={keyword}
  &gclid={gclid}
```

### Implementation
```html
<!-- Store UTM params in hidden form fields for lead gen -->
<script>
  (function() {
    var params = new URLSearchParams(window.location.search);
    var utmFields = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'gclid'];
    utmFields.forEach(function(field) {
      var value = params.get(field);
      if (value) {
        var inputs = document.querySelectorAll('input[name="' + field + '"]');
        inputs.forEach(function(input) { input.value = value; });
      }
    });
  })();
</script>

<!-- Add hidden fields to every form -->
<input type="hidden" name="utm_source" value="">
<input type="hidden" name="utm_medium" value="">
<input type="hidden" name="utm_campaign" value="">
<input type="hidden" name="utm_content" value="">
<input type="hidden" name="utm_term" value="">
<input type="hidden" name="gclid" value="">
```

## Google Tag Manager (GTM)

### Head Snippet (inside `<head>`, as early as possible)
```html
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','{GTM_ID}');</script>
```

### Body Snippet (immediately after `<body>`)
```html
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
```

### Placeholder
Use `{GTM_ID}` as placeholder. User replaces with their actual GTM container ID (format: `GTM-XXXXXXX`).

## Conversion Tracking

### Google Ads Conversion
```html
<script>
  function trackConversion() {
    // dataLayer push for GTM-based tracking
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({
      'event': 'form_submit',
      'conversion_type': 'lead'
    });

    // Direct gtag call (fallback if not using GTM)
    if (typeof gtag !== 'undefined') {
      gtag('event', 'conversion', {
        send_to: '{CONVERSION_ID}/{CONVERSION_LABEL}',
        value: 1.0,
        currency: 'VND'
      });
    }
  }
</script>
```

### When to Fire
- Form submission (primary): `<form onsubmit="trackConversion()">`
- Phone click: `<a href="tel:..." onclick="trackConversion()">`
- Do NOT fire on page load — only on user actions

### Placeholders
- `{CONVERSION_ID}` → format: `AW-XXXXXXXXX`
- `{CONVERSION_LABEL}` → format: `XXXXXXXXXXXXXXXXXXXX`

## Schema Markup

### FAQPage (always include if FAQ section exists)
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "{QUESTION_TEXT}",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "{ANSWER_TEXT}"
      }
    }
  ]
}
</script>
```

### LocalBusiness (for services with physical location)
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "{BUSINESS_NAME}",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "{ADDRESS}",
    "addressLocality": "{CITY}",
    "addressCountry": "{COUNTRY}"
  },
  "telephone": "{PHONE}",
  "url": "{URL}",
  "image": "{IMAGE_URL}"
}
</script>
```

### Which Schema to Use
```
IF service with physical address → LocalBusiness + FAQPage
IF e-commerce product → Product + FAQPage
IF company/brand → Organization + FAQPage
IF none of the above → FAQPage only
```

## Google Ads Quality Score Factors (LP-Related)

| Factor | What Google Checks | How to Score Well |
|--------|-------------------|-------------------|
| Relevance | Headline matches ad keywords | Message match (exact h1) |
| Transparency | Business info visible | Footer: name, address, phone, legal links |
| Navigation | Easy to use | Single CTA, no confusing menus |
| Load time | Page speed | Optimize images, minimal JS, inline critical CSS |
| Mobile | Mobile-friendly | Viewport meta, responsive, touch targets |
| Content | Original, useful | Real content, not thin/duplicate |
| Trust | Trust signals | Testimonials, badges, guarantees |
