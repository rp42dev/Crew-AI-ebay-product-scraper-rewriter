# 🚀 CrewAI eBay Product Scraper + SEO Rewriter

🎥 [V1 Watch Demo on Facebook](https://www.facebook.com/61571514151327/videos/706298025685350/)
🎥 [V2 Watch Demo on Facebook](https://fb.watch/z-TH3QyFYe/)


This project is an intelligent multi-version toolchain designed to:
- 🔎 Scrape eBay listings based on search terms or seller store pages
- 📋 Extract full product details (title, specs, description, price)
- ✍️ Rewrite listings using SEO-optimized structure and keyword strategy

It leverages **CrewAI** agents, **Flows**, and **Pydantic validation** to offer flexible, scalable, and low-cost options for listing rewriting.

---

## 🔁 Version Comparison

| Version | Architecture | Agents Used | LLM Usage | Speed | Output Type | Best For |
|---------|--------------|-------------|-----------|-------|-------------|----------|
| **v1**  | Classic CrewAI | 3 agents (Collector, Scraper, Rewriter) | 🔴 High | 🟡 Medium | Markdown | Showcases full agent orchestration |
| **v2**  | Scripted Single Agent | 1 agent | 🟢 Low | 🟢 Fast | Markdown | Cost-effective bulk rewriting |
| **v3**  | CrewAI Flow + Pydantic | 1 agent + `Flow` orchestrator | 🟢 Optimized | 🟢 Fast | JSON + Markdown | Structured pipelines, async-ready |

---

## 🛠 How to Use (v3 Recommended)

```bash
python src/ebay_seo_crew_v3/main.py
```

## 📝 Requirements

```bash	
pip install -r requirements.txt
```

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.	

## 📧 Contact
For questions or contributions, please open an issue on GitHub.