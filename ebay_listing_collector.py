import requests
from bs4 import BeautifulSoup
import csv
import time
import os
from datetime import datetime

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9"
}

def normalize_url(url):
    return url.split('?')[0]

def get_listings_from_page(url, max_pages=1):
    all_items = []
    seen_urls = set()

    for page in range(1, max_pages + 1):
        paged_url = f"{url}&_pgn={page}"
        print(f"Scraping page {page}: {paged_url}")

        try:
            response = requests.get(paged_url, headers=HEADERS)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        cards = soup.select(".s-item")

        if cards:
            first_link = cards[0].select_one(".s-item__link")
            if first_link:
                first_url = normalize_url(first_link["href"])
                if first_url in seen_urls:
                    print(f"First item URL on page {page} already seen, stopping scrape.")
                    break
                else:
                    seen_urls.add(first_url)

        for card in cards:
            title_tag = card.select_one(".s-item__title")
            price_tag = card.select_one(".s-item__price")
            link_tag = card.select_one(".s-item__link")

            if title_tag and price_tag and link_tag and "Shop on eBay" not in title_tag.text:
                clean_url = normalize_url(link_tag["href"])
                if clean_url not in seen_urls:
                    seen_urls.add(clean_url)
                    item = {
                        "title": title_tag.text.strip(),
                        "price": price_tag.text.strip(),
                        "url": clean_url
                    }
                    all_items.append(item)

        time.sleep(1)

    return all_items

def save_to_csv(items, filename="store_items.csv"):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    full_path = os.path.join(output_dir, filename)

    with open(full_path, "w", newline='', encoding="utf-8") as f:
        fieldnames = ["title", "price", "url"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for item in items:
            writer.writerow({
                "title": item.get("title", ""),
                "price": item.get("price", ""),
                "url": item.get("url", "")
            })

    print(f"✅ Results saved to {full_path}")

def run_url_scraper(input_str):
    """Run the eBay scraper with the provided URL or search term."""
    base_url = input_str if input_str.startswith("http") else f"https://www.ebay.com/sch/i.html?_nkw={input_str}"
    listings = get_listings_from_page(base_url, max_pages=3)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"store_items_{timestamp}.csv"
    save_to_csv(listings, filename=filename)

    print("✅ Scrape complete")

# Example call
if __name__ == "__main__":
    run_url_scraper("https://www.ebay.co.uk/sch/i.html?_ssn=ranem_20&_sacat=177831")
