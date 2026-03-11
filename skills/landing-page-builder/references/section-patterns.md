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

---

## Section 10: ZALO CHAT (Vietnamese Market Essential)

Zalo is the dominant messaging app in Vietnam. A landing page without Zalo chat loses leads.

```html
<!-- Zalo Chat Floating Button -->
<a href="https://zalo.me/{ZALO_OA_ID}"
   target="_blank"
   rel="noopener noreferrer"
   class="zalo-chat-button"
   aria-label="Chat với chúng tôi qua Zalo">
  <img src="/img/zalo-icon.svg" alt="Zalo" width="50" height="50">
</a>

<style>
.zalo-chat-button {
  position: fixed;
  bottom: 24px;
  right: 24px;
  z-index: 1000;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: #0068FF; /* Zalo blue */
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(0, 104, 255, 0.4);
  transition: transform 0.2s ease;
}
.zalo-chat-button:hover {
  transform: scale(1.1);
}
/* Mobile: larger touch target, more padding from edge */
@media (max-width: 768px) {
  .zalo-chat-button {
    bottom: 16px;
    right: 16px;
    width: 56px;
    height: 56px;
  }
}
</style>
```

Rules:
- Place in bottom-right corner (standard position for chat)
- Use official Zalo blue (#0068FF) for brand recognition
- `{ZALO_OA_ID}` = Zalo Official Account ID (user must provide)
- Include both Zalo button AND phone number (some prefer calling)
- Consider adding Facebook Messenger as secondary option

### Zalo + Phone Combo (Recommended)

```html
<div class="contact-buttons">
  <a href="tel:{PHONE}" class="phone-button">
    <svg><!-- phone icon --></svg>
    Gọi Ngay
  </a>
  <a href="https://zalo.me/{ZALO_OA_ID}" class="zalo-button">
    <img src="/img/zalo-icon.svg" alt="Zalo">
    Chat Zalo
  </a>
</div>
```

---

## Section 11: COUNTDOWN / URGENCY ELEMENTS

Use urgency elements to increase conversion. Use responsibly — fake urgency damages trust.

### Pattern 1: Countdown Timer

```html
<div class="countdown-banner" id="countdown">
  <p>Ưu đãi kết thúc sau:</p>
  <div class="countdown-timer">
    <div class="countdown-unit">
      <span id="days">00</span>
      <small>Ngày</small>
    </div>
    <div class="countdown-unit">
      <span id="hours">00</span>
      <small>Giờ</small>
    </div>
    <div class="countdown-unit">
      <span id="minutes">00</span>
      <small>Phút</small>
    </div>
    <div class="countdown-unit">
      <span id="seconds">00</span>
      <small>Giây</small>
    </div>
  </div>
</div>

<script>
(function() {
  // Set end date (replace with actual campaign end)
  const endDate = new Date('{YYYY-MM-DD}T23:59:59').getTime();

  function updateCountdown() {
    const now = new Date().getTime();
    const distance = endDate - now;

    if (distance < 0) {
      document.getElementById('countdown').style.display = 'none';
      return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    document.getElementById('days').textContent = String(days).padStart(2, '0');
    document.getElementById('hours').textContent = String(hours).padStart(2, '0');
    document.getElementById('minutes').textContent = String(minutes).padStart(2, '0');
    document.getElementById('seconds').textContent = String(seconds).padStart(2, '0');
  }

  updateCountdown();
  setInterval(updateCountdown, 1000);
})();
</script>
```

### Pattern 2: Limited Quantity

```html
<div class="scarcity-banner">
  <span class="scarcity-icon">🔥</span>
  <p>Chỉ còn <strong>{N}</strong> suất ưu đãi trong tháng này</p>
</div>
```

### Pattern 3: Social Proof Urgency

```html
<div class="live-visitors">
  <span class="pulse-dot"></span>
  <p><strong>{N}</strong> người đang xem trang này</p>
</div>

<style>
.pulse-dot {
  width: 8px;
  height: 8px;
  background: #22C55E;
  border-radius: 50%;
  animation: pulse 2s infinite;
}
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}
</style>
```

Rules for urgency elements:
- ONLY use if the urgency is REAL (actual deadline, actual limited quantity)
- Fake urgency = immediate trust destruction
- Hide countdown when expired (don't show negative time)
- Position: above CTA or in sticky banner

---

## Section 12: PRICING DISPLAY PATTERNS

### Pattern 1: Anchor Pricing (Strike-through)

```html
<div class="price-display anchor-pricing">
  <p class="original-price">
    <span class="label">Giá thị trường:</span>
    <span class="strike">25.000.000đ</span>
  </p>
  <p class="sale-price">
    <span class="label">Giá ưu đãi:</span>
    <span class="price">15.000.000đ</span>
  </p>
  <p class="savings">Tiết kiệm: 10.000.000đ (40%)</p>
</div>
```

### Pattern 2: Monthly Payment Breakdown (High-Ticket)

```html
<div class="price-display monthly-breakdown">
  <p class="headline-price">
    Chỉ từ <strong>500.000đ</strong>/tháng
  </p>
  <p class="total-price">
    (Tổng: 15.000.000đ × 30 tháng, lãi suất 0%)
  </p>
  <p class="partner">Qua VPBank / Home Credit</p>
</div>
```

### Pattern 3: Value Stack

```html
<div class="price-display value-stack">
  <h3>Bạn sẽ nhận được:</h3>
  <ul class="value-items">
    <li>
      <span class="item">Cấy ghép Implant Straumann</span>
      <span class="value">20.000.000đ</span>
    </li>
    <li>
      <span class="item">Chụp CT 3D miễn phí</span>
      <span class="value">500.000đ</span>
    </li>
    <li>
      <span class="item">Tái khám 10 lần miễn phí</span>
      <span class="value">2.000.000đ</span>
    </li>
    <li>
      <span class="item">Bảo hành 10 năm</span>
      <span class="value">Vô giá</span>
    </li>
  </ul>
  <div class="total-value">
    <p>Tổng giá trị: <span class="strike">22.500.000đ</span></p>
    <p class="actual-price">Bạn chỉ trả: <strong>15.000.000đ</strong></p>
  </div>
</div>
```

### Pattern 4: Tiered Pricing (Multiple Options)

```html
<div class="pricing-tiers">
  <div class="tier">
    <h4>Cơ Bản</h4>
    <p class="price">12.000.000đ</p>
    <ul>
      <li>Implant Hàn Quốc</li>
      <li>Bảo hành 5 năm</li>
    </ul>
    <a href="#form" class="cta-secondary">Chọn Gói Này</a>
  </div>

  <div class="tier featured">
    <span class="badge">Phổ Biến Nhất</span>
    <h4>Tiêu Chuẩn</h4>
    <p class="price">18.000.000đ</p>
    <ul>
      <li>Implant Straumann (Thụy Sĩ)</li>
      <li>Bảo hành 10 năm</li>
      <li>Tái khám miễn phí</li>
    </ul>
    <a href="#form" class="cta-button">Chọn Gói Này</a>
  </div>

  <div class="tier">
    <h4>Cao Cấp</h4>
    <p class="price">25.000.000đ</p>
    <ul>
      <li>Implant Nobel Biocare (Mỹ)</li>
      <li>Bảo hành trọn đời</li>
      <li>VIP lounge</li>
    </ul>
    <a href="#form" class="cta-secondary">Chọn Gói Này</a>
  </div>
</div>
```

Rules for pricing:
- Always show value before asking for money
- Use Vietnamese currency format: 15.000.000đ (not 15,000,000)
- Monthly breakdown makes high-ticket items feel affordable
- Highlight the "most popular" tier to guide decision
- Include "what's included" to justify price

---

## Section 13: VIETNAMESE PAYMENT METHODS

Essential for Vietnamese market — show payment options to reduce friction.

```html
<div class="payment-methods">
  <h4>Phương Thức Thanh Toán</h4>
  <div class="payment-icons">
    <img src="/img/payment/momo.svg" alt="MoMo" width="48" height="48">
    <img src="/img/payment/zalopay.svg" alt="ZaloPay" width="48" height="48">
    <img src="/img/payment/vnpay.svg" alt="VNPay" width="48" height="48">
    <img src="/img/payment/visa.svg" alt="Visa" width="48" height="48">
    <img src="/img/payment/mastercard.svg" alt="Mastercard" width="48" height="48">
  </div>
  <p class="payment-note">Hỗ trợ trả góp 0% qua VPBank, Home Credit, FE Credit</p>
</div>
```

### Installment Badge (Common in Vietnamese LPs)

```html
<div class="installment-badge">
  <span class="badge-icon">💳</span>
  <div class="badge-content">
    <strong>Trả Góp 0%</strong>
    <small>Qua thẻ tín dụng hoặc công ty tài chính</small>
  </div>
</div>
```

### Bank Transfer Info (For High-Value Transactions)

```html
<details class="bank-transfer-info">
  <summary>Thông tin chuyển khoản ngân hàng</summary>
  <div class="bank-details">
    <p><strong>Ngân hàng:</strong> {BANK_NAME}</p>
    <p><strong>Số tài khoản:</strong> {ACCOUNT_NUMBER}</p>
    <p><strong>Chủ tài khoản:</strong> {ACCOUNT_HOLDER}</p>
    <p><strong>Nội dung CK:</strong> {BUSINESS_NAME} + SĐT</p>
  </div>
</details>
```

Vietnamese payment patterns:
- MoMo, ZaloPay, VNPay are most popular e-wallets
- Installment (trả góp) is expected for items > 5 million VND
- Bank transfer is common for B2B or high-value consumer purchases
- Always mention "0%" interest — this is a major selling point
- Include VAT invoice availability: "Có hóa đơn VAT"

---

## Section 14: PRODUCT COMPARISON CARDS (Equal Height Grid)

Use this pattern when displaying multiple product variants/tiers side by side. The CSS ensures all cards have equal height with buttons aligned at the bottom.

### HTML Structure

```html
<section id="products">
  <h2>{SECTION_TITLE}</h2>
  <p class="section-subtitle">{SUBTITLE}</p>

  <div class="product-grid">
    <!-- Product Card -->
    <div class="product-card">
      <!-- Optional: Product Image -->
      <div class="product-image">
        <img src="{IMAGE_URL}" alt="{PRODUCT_NAME}"
             width="400" height="400" loading="lazy"
             class="product-img">
      </div>

      <!-- Optional: Badge (Best Seller, Premium, etc.) -->
      <div class="product-badge">{BADGE_TEXT}</div>

      <!-- Price Header -->
      <div class="product-header">
        <span class="original-price">{ORIGINAL_PRICE}</span>
        <h3 class="product-name">{PRODUCT_NAME}</h3>
        <p class="product-price">{SALE_PRICE}</p>
      </div>

      <!-- Features List (grows to fill space) -->
      <div class="product-content">
        <ul class="product-features">
          <li><span class="check">✓</span> {FEATURE_1}</li>
          <li><span class="check">✓</span> {FEATURE_2}</li>
          <li><span class="check">✓</span> {FEATURE_3}</li>
        </ul>

        <!-- CTA Button (always at bottom) -->
        <a href="#form" class="product-cta">{CTA_TEXT}</a>
      </div>
    </div>

    <!-- Repeat for each product -->
  </div>
</section>
```

### Critical CSS for Equal Height Cards

```css
/* Product Grid - Equal Height Cards */
.product-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
}

@media (min-width: 768px) {
  .product-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .product-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

/* THE CRITICAL RULES FOR EQUAL HEIGHT */
.product-card {
  display: flex;
  flex-direction: column;
  height: 100%;  /* Fill grid cell height */
  position: relative;
}

.product-content {
  flex-grow: 1;  /* Grow to fill remaining space */
  display: flex;
  flex-direction: column;
}

.product-features {
  flex-grow: 1;  /* Push CTA to bottom */
}

.product-cta {
  margin-top: auto;  /* Always at bottom */
}

/* Product Image */
.product-image {
  aspect-ratio: 1 / 1;
  overflow: hidden;
}

.product-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.product-card:hover .product-img {
  transform: scale(1.05);
}

/* Badge Positioning */
.product-badge {
  position: absolute;
  top: 0.5rem;
  right: 0.5rem;
  z-index: 10;
  padding: 0.25rem 0.75rem;
  border-radius: 0.25rem;
  font-size: 0.75rem;
  font-weight: 700;
}
```

### Tailwind Version

```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
  <!-- Product Card with Equal Height -->
  <div class="flex flex-col h-full bg-white rounded-xl shadow-md overflow-hidden relative">
    <!-- Badge -->
    <div class="absolute top-2 right-2 bg-primary text-white text-xs font-bold px-3 py-1 rounded z-10">
      BEST SELLER
    </div>

    <!-- Image -->
    <div class="aspect-square overflow-hidden">
      <img src="{URL}" alt="{ALT}"
           class="w-full h-full object-cover hover:scale-105 transition-transform duration-300"
           loading="lazy" width="400" height="400">
    </div>

    <!-- Header -->
    <div class="p-4 text-center bg-rose-50">
      <span class="text-sm text-gray-500"><s>{ORIGINAL_PRICE}</s></span>
      <h3 class="font-bold text-xl">{NAME}</h3>
      <p class="text-primary font-bold text-2xl">{PRICE}</p>
    </div>

    <!-- Content - MUST use flex-grow for equal height -->
    <div class="flex-grow flex flex-col p-4">
      <!-- Features list grows to push CTA down -->
      <ul class="flex-grow text-sm space-y-2 mb-4">
        <li class="flex items-start gap-2">
          <span class="text-green-600">✓</span> {FEATURE}
        </li>
      </ul>

      <!-- CTA uses mt-auto to stick to bottom -->
      <a href="#form" class="mt-auto block text-center bg-primary text-white py-3 rounded-lg font-semibold">
        {CTA_TEXT}
      </a>
    </div>
  </div>
</div>
```

### Rules for Product Cards
- ALWAYS use `flex flex-col h-full` on the card container
- ALWAYS use `flex-grow` on the content section
- ALWAYS use `flex-grow` on the features list
- ALWAYS use `mt-auto` on the CTA button
- Images should use `aspect-square` or fixed aspect ratio
- Badges should be `position: absolute` with `z-index: 10`

---

## Section 15: FAQ ACCORDION (CSS-Only with Details/Summary)

**IMPORTANT**: Prefer CSS-only `<details>/<summary>` over JavaScript-based accordions. It's more accessible, works without JS, and has no styling conflicts.

### CSS-Only Pattern (Recommended)

```html
<section id="faq">
  <h2>Câu Hỏi Thường Gặp</h2>

  <div class="faq-list">
    <details class="faq-item">
      <summary class="faq-question">
        <span>{QUESTION_1}</span>
        <span class="faq-icon">+</span>
      </summary>
      <div class="faq-answer">
        <p>{ANSWER_1}</p>
      </div>
    </details>

    <details class="faq-item">
      <summary class="faq-question">
        <span>{QUESTION_2}</span>
        <span class="faq-icon">+</span>
      </summary>
      <div class="faq-answer">
        <p>{ANSWER_2}</p>
      </div>
    </details>

    <!-- Repeat for 4-6 questions -->
  </div>
</section>
```

### CSS for Details/Summary Accordion

```css
.faq-list {
  max-width: 48rem;
  margin: 0 auto;
}

.faq-item {
  background: white;
  border-radius: 0.5rem;
  margin-bottom: 1rem;
  border: 1px solid #e5e7eb;
  overflow: hidden;
}

.faq-question {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 1.5rem;
  cursor: pointer;
  font-weight: 600;
  list-style: none; /* Remove default marker */
}

/* Remove default details marker in webkit */
.faq-question::-webkit-details-marker {
  display: none;
}

.faq-icon {
  font-size: 1.25rem;
  transition: transform 0.2s ease;
}

/* Rotate icon when open */
.faq-item[open] .faq-icon {
  transform: rotate(45deg);
}

/* Answer - hidden by default, shown when open */
.faq-answer {
  padding: 0 1.5rem 1rem 1.5rem;
  color: #6b7280;
}

/* Smooth animation (optional, works in modern browsers) */
.faq-item {
  transition: all 0.2s ease;
}
```

### Tailwind Version (CSS-Only)

```html
<div class="max-w-3xl mx-auto space-y-4">
  <details class="bg-white rounded-lg shadow-sm border border-gray-100 group">
    <summary class="flex justify-between items-center px-6 py-4 font-semibold cursor-pointer list-none">
      <span>Mùi nến thơm có nồng không?</span>
      <span class="text-xl transition-transform group-open:rotate-45">+</span>
    </summary>
    <div class="px-6 pb-4 text-gray-600">
      Nến BST Chill n Relax có mùi hương nhẹ nhàng, thư giãn, giúp ngủ ngon.
    </div>
  </details>
</div>
```

### JavaScript Accordion (If Required)

If you MUST use JavaScript (e.g., for animation), follow this pattern to avoid styling conflicts:

```html
<div class="faq-list">
  <div class="faq-item">
    <button class="faq-toggle" onclick="toggleFaq(this)">
      <span>Question text</span>
      <span class="faq-icon">+</span>
    </button>
    <!-- NO inline padding on faq-content - CSS handles it -->
    <div class="faq-content">
      <p>Answer text</p>
    </div>
  </div>
</div>
```

```css
/* CRITICAL: All padding controlled by CSS, not inline classes */
.faq-content {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease, padding 0.3s ease;
  padding: 0 1.5rem; /* horizontal only when closed */
}

.faq-content.open {
  max-height: 500px;
  padding: 0 1.5rem 1rem 1.5rem; /* add bottom padding when open */
}

/* DO NOT add inline padding classes like "px-6 pb-4" to faq-content */
/* They will conflict with max-height: 0 and show padding when closed */
```

```javascript
function toggleFaq(btn) {
  const content = btn.nextElementSibling;
  const icon = btn.querySelector('.faq-icon');

  content.classList.toggle('open');
  icon.textContent = content.classList.contains('open') ? '−' : '+';
}
```

### Rules for FAQ Section
- **PREFER** `<details>/<summary>` (CSS-only, accessible, no JS)
- If using JS accordion: **NEVER** add inline padding to `.faq-content`
- All padding must be controlled by CSS to work with `max-height: 0`
- Include `list-style: none` and `::-webkit-details-marker { display: none }` to remove default markers
- Use `group-open:` in Tailwind for open state styling

---

## Section 16: IMAGE FETCHING GUIDELINES

When a source product URL is provided, fetch real images instead of using placeholders.

### When to Fetch Images

```
IF user provides source URL (e.g., product page, existing website):
  1. Use WebFetch to extract image URLs from the page
  2. Look for: hero images, product gallery, variant images
  3. Use the actual URLs in the generated landing page

IF no source URL provided:
  1. Use placeholder structure with proper dimensions
  2. Add TODO comments for user to replace
```

### Image Optimization Checklist

```html
<!-- Hero Image (above fold) -->
<img src="{URL}"
     alt="{DESCRIPTIVE_ALT}"
     width="600" height="400"
     loading="eager"
     class="...">

<!-- Product/Gallery Images (below fold) -->
<img src="{URL}"
     alt="{DESCRIPTIVE_ALT}"
     width="400" height="400"
     loading="lazy"
     class="...">
```

### Required Image Attributes
- `alt` — Descriptive text for SEO and accessibility
- `width` + `height` — Prevents layout shift (CLS)
- `loading="eager"` — For above-fold images only
- `loading="lazy"` — For all other images
- `class` with `object-cover` — For consistent sizing
