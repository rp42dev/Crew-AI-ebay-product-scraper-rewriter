# src/ebay_seo_crew/main.py
from colorama import init, Fore, Style
import pandas as pd
from IPython.display import Markdown
from crew import EbaySeoCrew



def main():
    """
    Main function to run the eBay SEO crew.
    """
    inputs = {
        'input': input("Enter eBay search term or URL: ").strip()
    }
    crew = EbaySeoCrew().crew()
 
    crew.kickoff(inputs=inputs)
    
    print(f"{Fore.GREEN}📄 SEO rewriting completed. Saved to: output/seo_rewritten_listings.md")
    costs = 0.150 * (crew.usage_metrics.prompt_tokens + crew.usage_metrics.completion_tokens) / 1_000_000
    print(f"Total costs: ${costs:.4f}")

    # Convert UsageMetrics instance to a DataFrame
    df_usage_metrics = pd.DataFrame([crew.usage_metrics.dict()])
    df_usage_metrics
    print(f"\n{Fore.YELLOW}📊 Usage Metrics:\n{df_usage_metrics.to_string(index=False)}")
    
    with open("src/ebay_seo_crew_v1/output/seo_rewritten_listings.md", "r", encoding="utf-8") as f:
        content = f.read().strip()

    markdown  = content.raw
    Markdown(markdown)

if __name__ == "__main__":
    main()
