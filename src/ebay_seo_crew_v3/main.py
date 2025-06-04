# src/ebay_seo_crew_v2/main.py

from crewai.flow.flow import Flow, start, listen
from tools.ebay_listing_collector import EbayListingCollectorTool
from tools.product_scraper_tool import ProductScraperTool
from datetime import datetime
from crew import EbaySeoCrew
from pydantic import BaseModel
from typing import List
import os, json
import pandas as pd

from models.products import SEOProductInput, ProductListPayload, SEOProductOutput

class State(BaseModel):
    success_flag: bool = False
    product_list: List[SEOProductOutput] = []


class EbaySeoPipeline(Flow[State]):
    def __init__(self, query: str):
        super().__init__()
        self.query = query

    @start()
    def collect_urls(self):
        collector = EbayListingCollectorTool()
        listings = json.loads(collector._run(query=self.query))
        if not listings:
            print("⚠️ No listings found. Please check your query or try a different one.")
            return []

        for i, l in enumerate(listings, 1):
            print(f"[{i}] {l['title']} - {l['price']}")
        return listings

    @listen(collect_urls)
    def scrape_details(self, listings):
        scraper = ProductScraperTool()

        for item in listings:
            print(f"🔍 Scraping: {item['url']}")
            details = scraper.run(item["url"])
            item["description"] = details.get("description", "")
            item["specs"] = details.get("specs", {})

        products = [SEOProductInput(**item) for item in listings]
        payload = ProductListPayload(products=products)

        os.makedirs("src/ebay_seo_crew_v3/output", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = f"src/ebay_seo_crew_v3/output/detailed_listings_{timestamp}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload.dict(), f, indent=2, ensure_ascii=False)

        print(f"✅ Scraped product details saved to: {path}")
        print(f"Total products: {len(products)}")
        print(json.dumps(payload.dict(), indent=2)[:500])  # Preview

        return [p.dict() for p in products]  # Return for next flow step

    @listen(scrape_details)
    def rewrite_seo(self, products):
        print("✍️ Rewriting product listings for SEO...")
        crew = EbaySeoCrew().crew()
        results = crew.kickoff_for_each(products)
        
        
        for i, result in enumerate(results, 1):
            if isinstance(result.pydantic, SEOProductOutput):
                self.state.product_list.append(result.pydantic)
            else:
                print(f"❌ Error rewriting product {i}: {result.pydantic}")
                
        if not self.state.product_list:
            print("⚠️ No products were successfully rewritten. Please check the input data.")
            self.state.success_flag = False
            return []
        
        self.state.success_flag = True
        if self.state.success_flag:
            print(f"Total successful rewrites: {len([p for p in self.state.product_list if p.rewritten_title])}")
            print(f"Total failed rewrites: {len([p for p in self.state.product_list if not p.rewritten_title])}")
            with open(f"src/ebay_seo_crew_v3/output/seo_rewritten_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json", "w", encoding="utf-8") as f:
                json.dump([p.dict() for p in self.state.product_list], f, indent=2, ensure_ascii=False)

            usage = crew.usage_metrics.dict()
            df_usage_metrics = pd.DataFrame([usage])
            costs = 0.150 * df_usage_metrics['total_tokens'].sum() / 1_000_000

            print("📊 Token usage:")
            print(df_usage_metrics.to_string(index=False))
            print(f"💰 Total costs: ${costs:.4f}")
            return results
        else:
            print("❌ No successful rewrites. Please check the input data")
            return []

if __name__ == "__main__":
    user_query = input("🔎 Enter eBay search term or store URL: ").strip()
    flow = EbaySeoPipeline(query=user_query)
    flow.kickoff()
    # flow.plot()