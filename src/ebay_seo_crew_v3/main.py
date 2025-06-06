# src/ebay_seo_crew_v2/main.py

from flow import EbaySeoPipeline

from utils.terminal_style import style_text
if __name__ == "__main__":
    print(style_text("🛠️  eBay SEO Engine (v3)", color="cyan", bold=True))

    while True:
        user_query = input(style_text("🔎 Enter eBay search term or resolved listing URL: ", color="white")).strip()

        # Valid if it's either a resolved listing URL or keyword
        if user_query.startswith("https://www.ebay.co.uk/sch/") or not user_query.startswith("http"):
            break
        else:
            print(style_text("\n⚠️  That looks like a storefront URL or unsupported page.", color="yellow", bold=True))
            print(style_text("👉  Please open it in your browser, click 'See All', and paste the resulting URL here.", color="yellow"))
            print(style_text("💡  Or just enter a keyword like:", color="magenta"), style_text(" bike", color="white"))
    while True:
        try:
            limit = int(input(style_text("🔢 Enter the number of listings to scrape (default is 2): ", color="white")).strip() or 3)
            if limit <= 0:
                raise ValueError("Limit must be a positive integer.")
            break
        except ValueError as e:
            print(style_text(f"\n⚠️  Invalid input: {e}. Please enter a valid number.", color="red", bold=True))
    if limit > 20:
        print(style_text("\n⚠️  Limit is capped at 20 listings to avoid performance issues.", color="yellow", bold=True))
        limit = 20
    
    print(style_text("\n🚀 Launching pipeline...\n", color="green", bold=True))
    flow = EbaySeoPipeline(query=user_query, limit=limit)
    flow.kickoff()