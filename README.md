# 🚀 CrewAI eBay Product Scraper + SEO Rewriter

🎥 [Watch Demo on Facebook](https://www.facebook.com/61571514151327/videos/706298025685350/)

This project is a multi-agent system powered by [CrewAI](https://github.com/joaomdmoura/crewai) to collect eBay product listings and rewrite them using SEO best practices.

---

## 🧩 Project Versions

### ✅ `v2/` — **Current Lightweight Version**
- 🧠 Uses **just one agent**: SEO rewriter
- ⚙️ Scraping logic is hardcoded outside of the LLM agent to save costs
- 💡 **Optimized for minimum OpenAI token usage**
- 🔄 Runs in sequence but can be extended for parallelism
- 📂 Uses Pydantic for structured product input
- 🔍 Ideal for fast bulk SEO rewrite with minimal overhead

### 🗃️ `v1/` — **Legacy 3-Agent Version**
- 🤖 Agents for scraping URLs, scraping product data, and rewriting
- 🔁 Fully autonomous but **uses more LLM tokens**
- 🧠 Good for demonstrating multi-agent orchestration
- ❌ Less efficient for large-scale batch runs

---

### 📁 Folder Structure

```bash
.
├── v1/                       
│   ├── crew.py
│   └── main.py
├── v2/                        
│   ├── crew.py
│   ├── main.py            
│   ├── models/
│   │   └── products.py
│   └── tools/
│       ├── ebay_listing_collector.py
│       └── product_scraper_tool.py
├── config/
│   ├── agents.yaml
│   └── tasks.yaml
└── knowledge/
    └── seo_template.md
```
### 📝 How It Works
#### Step-by-step (v2):
 1. Accepts a keyword or eBay store URL as input
 2. Scrapes the listings and product details (done outside LLM agent)
 3. Feeds each product to the SEO Rewriter agent
 4. Outputs Markdown-formatted SEO listings

```bash
cd v2
python main.py
```
## 📦 Output

- ✅ **Markdown**: `output/seo_rewritten_listings.md`
- ✅ **JSON**: Scraped product listing data for reuse or debugging

---

## 💰 Efficiency Comparison

| Version | Agents | LLM Usage | Speed   | Best For               |
|---------|--------|-----------|---------|------------------------|
| `v1`    | 3      | High ❌    | Medium  | Demos, experimentation |
| `v2`    | 1      | Low ✅     | Fast ✅ | Bulk SEO rewriting     |

---

## 🔥 SEO Template

See [`knowledge/seo_template.md`](knowledge/seo_template.md) for full SEO structure.

**Title**:  
`[Brand] [Feature] [Product Type] [Model]`

**Description**:
- 1–2 punchy benefit-driven lines  
- Bullet list of key specs  
- Close with shipping, return, or trust-building info

**SEO Rules**:
- Include 2–3 high-value keywords  
- Use short, engaging paragraphs  
- Match tone to the target audience

## 📝 Requirements

```bash	
pip install -r requirements.txt
```

## 📄 License
This project is licensed under the MIT License. See the

## 📧 Contact
For questions or contributions, please open an issue on GitHub or contact the project maintainer.