# src/ebay_seo_crew/main.py

from crew import EbaySeoCrew

def main():
    """
    Main function to run the eBay SEO crew.
    """
    inputs = {
        'input': input("Enter eBay search term or URL: ").strip()
    }
    EbaySeoCrew().crew().kickoff(inputs=inputs)
    
if __name__ == "__main__":
    main()
