---
name: niche-research
description: "Research keywords, search intent, and CPC estimates for Google Ads landing pages. Use when starting a new landing page project, when user says 'research keywords', 'find niche', 'market analysis', 'keyword research', 'new client brief', 'new project', 'new campaign', or any request that involves understanding a market before building a landing page. Always use this BEFORE building any landing page."
---

# Niche Research — Keyword & Market Intelligence

You are running the niche-research skill for a Google Ads landing page project.
Your job: produce a niche brief that the entire pipeline depends on. Be thorough.

## Step 1: Gather Input (DO NOT SKIP)

Ask the user for these inputs. Do NOT proceed without them:

1. **Product/Service name** — what are we selling?
2. **Target market** — geography (country/city) + language
3. **Budget range** — monthly Google Ads spend (optional — default: "Not specified")
4. **Existing website URL** — if they have one (optional)

IF the user provided a brief or description → extract all 4 inputs from it.
IF anything is unclear → ask. Suggest reasonable defaults.
IF user says "Vietnamese dental implant clinic in Ho Chi Minh City" → you have product, geo, and language. Ask only for budget and URL.

Set `{PROJECT_NAME}` = kebab-case of the product/service name.
Create the output directory:
```
output/{PROJECT_NAME}/research/
```

## Step 2: Keyword Research

Use `web_search` to find keywords. Run these searches:

```
"{product} {location}"
"{product} giá" OR "{product} price"
"{product} review" OR "{product} đánh giá"
"best {product}" OR "{product} tốt nhất"
"{product} near me" OR "{product} gần đây"
"{product} uy tín"
"{product} ở đâu"
```

For Vietnamese market: ALWAYS search both Vietnamese AND English terms.
Example: search "trồng răng implant giá" AND "dental implant price ho chi minh".

Collect **20-40 keywords minimum**. If you get fewer than 20, add more search variations:
- "{product} + {benefit}" (e.g., "implant không đau")
- "{product} + {objection}" (e.g., "implant có đau không")
- "{product} + {competitor type}" (e.g., "nha khoa implant")

IF `web_search` fails or is unavailable:
1. Retry once with a simpler query
2. Ask user: "Web search is unavailable. Can you provide a list of keywords your customers might search?"
3. If user provides keywords → continue with those
4. If user cannot → generate a reasonable keyword list from your knowledge, but add this warning to the output: "⚠️ Keywords generated without live search data. Validate with Google Keyword Planner."

## Step 3: Classify by Search Intent

Classify EVERY keyword using these rules:

```
IF keyword contains "mua", "buy", "giá", "price", "cost", "đặt", "order", "book", "đặt lịch"
  → TRANSACTIONAL

IF keyword contains "tốt nhất", "best", "review", "đánh giá", "so sánh", "compare", "vs", "top"
  → COMMERCIAL

IF keyword contains "là gì", "what is", "how to", "cách", "hướng dẫn", "guide"
  → INFORMATIONAL

IF keyword contains brand name, clinic name, specific address, "ở đâu"
  → NAVIGATIONAL
```

IF a keyword is ambiguous → classify as COMMERCIAL (safer for landing pages).

Read `references/search-intent-mapping.md` for the full signal word list.

Landing pages target **TRANSACTIONAL** and **COMMERCIAL** intent. Mark INFORMATIONAL keywords as "blog content opportunity" — do not target them with ads.

## Step 4: Cluster & Suggest Ad Groups

Group the keywords into **3-5 clusters** by theme.

Rules:
- Each cluster = 1 ad group = 1 landing page variant
- Name each cluster descriptively (e.g., "Price-Focused Implant Seekers")
- Put the highest-intent keywords first in each cluster
- Each cluster should have 5-10 keywords

Example clusters for dental implant:
```
Cluster 1: "Implant Pricing" (TRANSACTIONAL) → giá implant, chi phí implant, implant bao nhiêu
Cluster 2: "Implant Quality" (COMMERCIAL) → implant tốt nhất, nha khoa implant uy tín
Cluster 3: "Implant Process" (COMMERCIAL) → quy trình implant, implant có đau không
```

## Step 5: Estimate CPC & Competition

Use `web_search` to find public CPC data:
- Search: "{niche} google ads CPC {country}"
- Search: "{niche} cost per click average"
- Check industry reports, blog posts with CPC benchmarks

Categorize each cluster:
```
Low:    $0 - $2   (or < 20,000 VND)
Medium: $2 - $10  (or 20,000 - 200,000 VND)
High:   $10+      (or > 200,000 VND)
```

**MANDATORY CAVEAT** — include this exact text in the output:
> CPC estimates are approximate, based on public data. Verify with Google Keyword Planner before setting budgets.

IF CPC data is unavailable → mark as "Unknown — check Keyword Planner" and move on. Do NOT guess.

## Step 6: Identify Negative Keywords

Generate 10-20 negative keywords to exclude irrelevant traffic.

Decision logic:
```
IF selling premium service → add: "miễn phí", "free", "tự làm", "DIY", "cheap"
IF selling local service → add: competitor city names, "online"
IF B2B → add: "consumer", "personal", "home"
IF specific niche → add: related-but-wrong products
```

Example for premium dental implant:
```
Negative: free, miễn phí, tự, DIY, học, learn, training, đào tạo, tuyển dụng, job
```

## Step 7: Generate Output

Read `assets/niche-brief-template.md` and fill ALL placeholders with the research data.

Save the completed brief to:
```
output/{PROJECT_NAME}/research/niche-brief.md
```

Show progress throughout:
```
[niche-research] Step 1/7: Gathering input...
[niche-research] Step 2/7: Searching keywords...
[niche-research] Step 3/7: Classifying search intent...
[niche-research] Step 4/7: Clustering into ad groups...
[niche-research] Step 5/7: Estimating CPC & competition...
[niche-research] Step 6/7: Identifying negative keywords...
[niche-research] Step 7/7: Generating niche brief...
[niche-research] ✅ Complete → output/{PROJECT_NAME}/research/niche-brief.md
```

After saving, tell the user:
```
Next steps:
- Run competitor-analysis: "Analyze competitors for {PROJECT_NAME}"
- Or run both research skills in parallel if using OMC
```

## Error Handling

- **web_search unavailable**: Retry once → ask user for manual keywords → proceed with partial data + warning
- **Too few keywords found** (< 10): Broaden search terms, try English equivalents, ask user for seed keywords
- **CPC data not found**: Mark as "Unknown" — never fabricate numbers
- **Output directory creation fails**: Report the error, suggest checking file permissions
