# 🚀 CrewAI eBay Product Scraper + SEO Rewriter + SKU + Markdown Generator

🎥 [V1 Demo on Facebook](https://www.facebook.com/61571514151327/videos/706298025685350/)  
🎥 [V2 Demo on Facebook](https://fb.watch/z-TH3QyFYe/)

This project is an intelligent multi-version toolchain designed to:
- 🔎 Scrape eBay listings based on search terms or seller store pages
- 📋 Extract full product details (title, specs, description, price)
- ✍️ Rewrite listings using SEO-optimized structure and keyword strategy
- 🆔 Automatically generate SKUs based on product data
- 📝 Convert listings into human-readable Markdown (for blogs, Shopify, Notion, etc.)

It leverages **CrewAI** agents, **Flows**, **Pydantic validation**, and modular processors to offer scalable, structured listing automation.

---

## 🔁 Version Comparison

| Version | Architecture              | Agents Used                         | LLM Usage     | Speed     | Output Type          | Best For                       |
|---------|---------------------------|--------------------------------------|---------------|-----------|------------------------|--------------------------------|
| **v1**  | Classic CrewAI             | 3 agents (Collector, Scraper, Rewriter) | 🔴 High       | 🟡 Medium | Markdown              | Full agent orchestration demo |
| **v2**  | Scripted single agent      | 1 agent                             | 🟢 Low         | 🟢 Fast   | Markdown              | Fast bulk rewriting            |
| **v3**  | CrewAI Flow + Pydantic     | 1 agent + `Flow` orchestrator       | 🟢 Optimized   | 🟢 Fast   | JSON → SKU + Markdown | Full structured automation     |

---

## 📝 Requirements

```bash	
pip install -r requirements.txt
```
---

## 🔁 Pipeline Overview

This is the step-by-step process for version 3:

### 🧩 Stage 1 – URL Collection

- Accepts an **eBay keyword** or full **store URL**
- Resolves store “See All” link
- Scrapes up to **product listing URLs** from eBay

### 🧪 Stage 2 – Product Detail Scraping

- For each URL:
  - Visits the product page
  - Extracts key details: `title`, `price`, `description`, `specs`, and `URL`
- Saves structured output using a `Pydantic` model (`SEOProductInput`). Output JSON saved as `store_items_<timestamp>.json`.

### ✍️ Stage 3 – AI-Powered SEO Rewriting

- One product at a time is passed to the SEO rewriting agent
- Output conforms to strict `Pydantic` schema (`SEOProductOutput`). Output JSON saved as `detailed_listings_<timestamp>.json`.

### 💾 Stage 4 – Output

- ✅ Saves all rewritten products to a single
- **`rewritten_products<timestamp>.json`** file
- ✅ Generates a SKU for each product based on:
  - **Category** (e.g., `BIK` for bikes, `HLM` for helmets)
  - **Size** (e.g., `24IN`, `700C`)
  - **Department** (e.g., `UK` for Kids, `MA` for
- ✅ Also generates individual `.md` files for each product with:
    - Title (max 80 chars): starts with primary keyword ()
    - Subtitle (max 120 chars): 1-line benefit
    - SKU 
    - Price
    - Description (250–650) chars, 3 short paragraphs
    - Key Specs (Exactly 5)
    - Spec (all original specs from eBay)
    - Meta Title (max 60 chars): starts with primary keyword
    - Meta Keywords (2–3 high-value terms)
    - Meta Description (max 160 chars): starts with primary keyword
    - Original URL
- ✅ Token usage and cost summary included

---

🔍 Total Control  
✅ Fully structured. ✅ Easy to scale. ✅ Markdown-ready. ✅ Minimal LLM cost.


```bash
python src/ebay_seo_crew_v3/main.py
```

### ✅ You’ll Get:

- **`store_items_<timestamp>.json`** – Raw scraped product data
- **`detailed_listings_<timestamp>.json`** – SEO-rewritten product details
- **`rewritten_products_<timestamp>.json`** – Final enriched product data.
- **`products_with_skus_<timestamp>.json`** – Products with generated SKUs
- **`<productSKU>.md`** – Ready-to-paste Markdown for listings, content pages, or storefronts

---

### 🧠 SKU Logic Summary

- `BIK`, `HLM`, `SCT`, etc. → Based on keywords like **bike**, **helmet**, **scooter**, etc.  
- **Wheel Size**, **Size**, or **Model** → Used for segment 2 (e.g., `24IN`, `700C`)  
- `UK`, `MA`, `FA`, `UN` → Department codes for **Kids**, **Men**, **Women**, or **Unisex**  
- Short token from title + random 4-character suffix for uniqueness

#### 🧪 Example Output:
**Example SKU:** `BIK-24IN-UK-24MOU-87A3`  
**Product Title:** *24-Inch Mountain Bike with Suspension and Disc Brakes*



## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.	

## 📧 Contact
For questions or contributions, please open an issue on GitHub.