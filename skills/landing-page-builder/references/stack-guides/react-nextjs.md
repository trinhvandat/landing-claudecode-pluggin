# Stack Guide: React / Next.js

Use this guide when the project has Next.js detected (package.json contains "next").

## When to Use
- Project already uses Next.js
- Client needs SSR/SSG for performance
- Landing page is part of a larger Next.js application
- Need dynamic features (A/B testing, personalization)

## File Structure
```
output/{PROJECT_NAME}/src/
├── app/
│   ├── layout.tsx           ← root layout (fonts, GTM, meta)
│   ├── page.tsx             ← landing page (all sections)
│   └── globals.css          ← Tailwind imports + custom styles
├── components/
│   ├── Hero.tsx
│   ├── PainPoints.tsx
│   ├── Benefits.tsx
│   ├── SocialProof.tsx
│   ├── HowItWorks.tsx
│   ├── FAQ.tsx
│   ├── FinalCTA.tsx
│   ├── Footer.tsx
│   └── CTAButton.tsx        ← reusable CTA component
└── lib/
    └── tracking.ts          ← GTM + conversion helpers
```

## App Router Layout (layout.tsx)

```tsx
import type { Metadata } from 'next'
import { {HEADING_FONT_VAR}, {BODY_FONT_VAR} } from 'next/font/google'
import './globals.css'

const headingFont = {HEADING_FONT_VAR}({
  subsets: ['latin', 'vietnamese'],
  variable: '--font-heading',
  display: 'swap',
})

const bodyFont = {BODY_FONT_VAR}({
  subsets: ['latin', 'vietnamese'],
  variable: '--font-body',
  display: 'swap',
})

export const metadata: Metadata = {
  title: '{PAGE_TITLE} | {BUSINESS_NAME}',
  description: '{META_DESCRIPTION}',
  openGraph: {
    title: '{PAGE_TITLE}',
    description: '{META_DESCRIPTION}',
    images: ['{OG_IMAGE_URL}'],
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: '{PAGE_TITLE}',
    description: '{META_DESCRIPTION}',
  },
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="{LANGUAGE_CODE}"
          className={`${headingFont.variable} ${bodyFont.variable}`}>
      <head>
        {/* GTM Head Script */}
        <script dangerouslySetInnerHTML={{ __html: `
          (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
          new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
          j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
          'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
          })(window,document,'script','dataLayer','{GTM_ID}');
        `}} />

        {/* FAQPage Schema */}
        <script type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify({SCHEMA_OBJECT}) }} />
      </head>
      <body className="font-body antialiased">
        {/* GTM noscript */}
        <noscript>
          <iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}"
            height="0" width="0" style={{ display: 'none', visibility: 'hidden' }} />
        </noscript>
        {children}
      </body>
    </html>
  )
}
```

## Page Component (page.tsx)

```tsx
import Hero from '@/components/Hero'
import PainPoints from '@/components/PainPoints'
import Benefits from '@/components/Benefits'
import SocialProof from '@/components/SocialProof'
import HowItWorks from '@/components/HowItWorks'
import FAQ from '@/components/FAQ'
import FinalCTA from '@/components/FinalCTA'
import Footer from '@/components/Footer'

export default function LandingPage() {
  return (
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
  )
}
```

## DKI with Next.js (Client Component)

```tsx
'use client'
import { useSearchParams } from 'next/navigation'
import { Suspense } from 'react'

function HeadlineContent({ defaultText }: { defaultText: string }) {
  const searchParams = useSearchParams()
  const keyword = searchParams.get('keyword')
  return (
    <h1 className="text-3xl md:text-5xl font-heading font-bold">
      {keyword ? decodeURIComponent(keyword) : defaultText}
    </h1>
  )
}

export function DKIHeadline({ defaultText }: { defaultText: string }) {
  return (
    <Suspense fallback={<h1 className="text-3xl md:text-5xl font-heading font-bold">{defaultText}</h1>}>
      <HeadlineContent defaultText={defaultText} />
    </Suspense>
  )
}
```

## Tracking Helper (lib/tracking.ts)

```tsx
export function trackConversion() {
  if (typeof window !== 'undefined') {
    window.dataLayer = window.dataLayer || []
    window.dataLayer.push({
      event: 'form_submit',
      conversion_type: 'lead',
    })
  }
}

export function getUTMParams(): Record<string, string> {
  if (typeof window === 'undefined') return {}
  const params = new URLSearchParams(window.location.search)
  const utmFields = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'gclid']
  const result: Record<string, string> = {}
  utmFields.forEach(field => {
    const value = params.get(field)
    if (value) result[field] = value
  })
  return result
}
```

## Performance Notes

- Use `next/font/google` for fonts — automatic optimization, no layout shift
- Use `next/image` for hero image: automatic WebP, srcset, lazy loading
- Static export (`output: 'export'`) for pure static LP — no server needed
- Prefer Server Components (default) — only use `'use client'` for DKI and form

## Do / Don't

| Do | Don't |
|----|-------|
| Use App Router (app/) | Use Pages Router (pages/) for new projects |
| Use `next/font` for fonts | Load fonts via `<link>` tags |
| Use `next/image` with priority on hero | Use raw `<img>` tags |
| Use Server Components by default | Mark everything `'use client'` |
| Use Metadata API for SEO | Use raw `<meta>` tags in JSX |
| Static export for simple LP | SSR unless dynamic features needed |
