# src/ebay_seo_crew/tools/ebay_listing_collector.py

import requests
import time
import os
import json
from bs4 import BeautifulSoup
from datetime import datetime
from typing import Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool

from utils.terminal_style import style_text


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9"
}

def normalize_url(url: str) -> str:
    return url.split('?')[0]


def is_captcha_page(html: str) -> bool:
    return "captcha" in html.lower() or "PageId: 2551517" in html

def get_listings_from_page(url: str, max_pages: int = 1):
    all_items = []
    seen_urls = set()

    for page in range(1, max_pages + 1):
        paged_url = f"{url}&_pgn={page}"
        print(f"🔍 Scraping page {page}: {paged_url}")

        try:
            response = requests.get(paged_url, headers=HEADERS)
            response.raise_for_status()

            if is_captcha_page(response.text):
                print(style_text("🛑 CAPTCHA detected. Scraping aborted.\n", color="red", bold=True))
                print(style_text("⚠️ Try using a keyword instead of a storefront page, like:\n", color="yellow"))
                print(style_text("    python main.py\n    > bike\n", color="cyan"))
                print(style_text("✅ Or use a direct store *listing* URL (not the /str/ page), e.g.:\n", color="yellow"))
                print(style_text("    https://www.ebay.co.uk/sch/i.html?...&store_name=yourstore", color="cyan"))
                break

        except requests.RequestException as e:
            print(f"❌ Request failed: {e}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        cards = soup.select(".s-item")

        if not cards:
            print("⚠️ No product cards found.")
            break

        first_link = cards[0].select_one(".s-item__link")
        if first_link:
            first_url = normalize_url(first_link["href"])
            if first_url in seen_urls:
                print("🔁 Duplicate page detected. Stopping.")
                break
            seen_urls.add(first_url)

        for card in cards:
            title_tag = card.select_one(".s-item__title")
            price_tag = card.select_one(".s-item__price")
            link_tag = card.select_one(".s-item__link")

            if title_tag and price_tag and link_tag and "Shop on eBay" not in title_tag.text:
                clean_url = normalize_url(link_tag["href"])
                if clean_url not in seen_urls:
                    seen_urls.add(clean_url)
                    all_items.append({
                        "title": title_tag.text.strip(),
                        "price": price_tag.text.strip(),
                        "url": clean_url
                    })

        time.sleep(2 + (page * 0.5))  # Add delay to be polite

    print(f"\n✅ Total products found: {len(all_items)}")
    return all_items[:2]

class EbayListingCollectorInput(BaseModel):
    query: str = Field(..., description="eBay search term or a full eBay URL.")

class EbayListingCollectorTool(BaseTool):
    name: str = "ebay_listing_collector"
    description: str = (
        "Scrapes eBay listings from a search term or store page URL and returns up to 20 product titles, prices, and URLs."
    )
    args_schema: Type[BaseModel] = EbayListingCollectorInput

    def _run(self, query: str) -> str:
        base_url = query if query.startswith("http") else f"https://www.ebay.com/sch/i.html?_nkw={query}"
        listings = get_listings_from_page(base_url, max_pages=3)

        os.makedirs("src/ebay_seo_crew_v3/output", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = f"src/ebay_seo_crew_v3/output/store_items_{timestamp}.json"

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(listings, f, indent=2)

        return json.dumps(listings, indent=2)
