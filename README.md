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

## ✅ Running the Full v3 Pipeline

From `main.py`, you can:

1. Load SEO-rewritten JSON (from Flow)
2. Add SKUs with `generate_sku.py`
3. Convert to Markdown with `generate_markdown.py`
4. Save everything to disk

```bash
python src/ebay_seo_crew_v3/main.py
```

### ✅ You’ll Get:

- **`products_with_sku.json`** – Enriched JSON output with auto-generated SKUs  
- **`products.md`** – Ready-to-paste Markdown for listings, content pages, or storefronts

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