# Keyword Research Guide

Reference for the niche-research skill. Read this when you need details on keyword methodology.

## Google Ads Keyword Match Types

| Match Type | Syntax | Behavior | Example |
|-----------|--------|----------|---------|
| Broad | `keyword` | Loosest — triggers on related searches, synonyms, misspellings | `dental implant` matches "tooth replacement cost" |
| Phrase | `"keyword"` | Triggers when search contains the phrase in order | `"dental implant"` matches "best dental implant clinic" |
| Exact | `[keyword]` | Tightest — triggers only on that exact meaning | `[dental implant]` matches "dental implant" or "dental implants" |

### Which to recommend:
- New campaigns with small budget → start with **Exact** and **Phrase** match
- Established campaigns exploring volume → add **Broad** with negative keywords
- Always pair Broad match with a negative keyword list

## How to Estimate CPC from Public Data

1. Search: `"{niche} google ads CPC {year}"` or `"{niche} cost per click benchmark"`
2. Check industry benchmark reports (WordStream, SEMrush, SpyFu blog posts)
3. For Vietnamese market: search `"google ads CPC vietnam {niche}"` and `"chi phí quảng cáo google {niche}"`
4. Cross-reference 2-3 sources — take the median, not the lowest

### CPC ranges by tier:
```
Low:    $0 - $2    (< 20,000 VND)   — low competition niches, long-tail keywords
Medium: $2 - $10   (20K - 200K VND) — most service businesses
High:   $10+       (> 200,000 VND)  — legal, finance, insurance, medical
```

### Always caveat:
Public CPC data is directional only. Actual CPC depends on Quality Score, bid strategy, competition at auction time. Always recommend verifying with Google Keyword Planner.

## Keyword Clustering Methodology

### Step 1: Group by root term
Keywords sharing the same root word belong together.
"implant giá", "implant bao nhiêu", "chi phí implant" → all in "Pricing" cluster.

### Step 2: Group by intent
Within root groups, split by intent if they diverge.
"implant tốt nhất" (COMMERCIAL) vs "mua implant" (TRANSACTIONAL) → could be separate ad groups.

### Step 3: Name descriptively
Bad: "Cluster 1"
Good: "Price-Conscious Implant Seekers"

### Step 4: Target size
- 5-10 keywords per cluster is ideal
- If a cluster has 15+ keywords → split it
- If a cluster has < 3 keywords → merge with the closest cluster

## Vietnamese Market Tips

### Diacritics matter
- "răng" (tooth) ≠ "rang" (cook/fry)
- ALWAYS search WITH diacritics for accurate results
- ALSO search WITHOUT diacritics — many users type without them on mobile

### Regional differences
- HCM/Saigon: more English mixed in, younger demographic
- Hanoi: more formal Vietnamese, government/institutional keywords
- Da Nang/other cities: lower competition, lower CPC

### Common Vietnamese search patterns
- Question format: "{product} có tốt không?" (is X good?)
- Location format: "{product} ở {city}" (X in city)
- Price format: "{product} giá bao nhiêu" (how much is X?)
- Comparison: "{product A} hay {product B}" (A or B?)

### Slang & abbreviations
- "nha khoa" = dental clinic (formal)
- "phòng khám" = clinic (general)
- "bs" or "bác sĩ" = doctor
- "TP.HCM" or "TPHCM" or "Sài Gòn" = Ho Chi Minh City
- "HN" = Hanoi
