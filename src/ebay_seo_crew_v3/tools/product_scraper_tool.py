# src/ebay_seo_crew/tools/product_scraper_tool.py

import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from typing import Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool
from colorama import init, Fore

init(autoreset=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9"
}

class ProductScraperInput(BaseModel):
    url: str = Field(..., description="URL of the eBay product page")

class ProductScraperTool(BaseTool):
    name: str = "product_scraper_tool"
    description: str = (
        "Scrapes full product details (title, description, specs, price) from a given eBay product page."
    )
    args_schema: Type[BaseModel] = ProductScraperInput

    def _run(self, url: str) -> dict:

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=options)

        try:
            driver.get(url)
            time.sleep(2)
            html = driver.page_source
        except Exception as e:
            print(f"{Fore.RED}❌ Failed to load page: {e}")
            driver.quit()
            print(f"{Fore.YELLOW}⚠️ Skipping URL due to error.")
            return {"description": "", "specs": {}}

        soup = BeautifulSoup(html, "html.parser")
        driver.quit()

        # Extract description
        full_desc = ""
        iframe = soup.find("iframe", id="desc_ifr")
        if iframe and iframe.has_attr("src"):
            iframe_src = iframe["src"]
            try:
                iframe_resp = requests.get(iframe_src, headers=HEADERS)
                iframe_resp.raise_for_status()
                iframe_soup = BeautifulSoup(iframe_resp.text, "html.parser")
                full_desc = iframe_soup.get_text(separator="\n").strip()
            except:
                full_desc = ""
        else:
            desc_div = soup.select_one("#viTabs_0_is")
            if desc_div:
                full_desc = desc_div.get_text(separator="\n").strip()

        full_desc = full_desc.replace('"', "'")

        # Extract specs
        specs = {}
        spec_blocks = soup.select("dl[data-testid='ux-labels-values']")
        for block in spec_blocks:
            label_tag = block.select_one("dt .ux-textspans")
            value_tag = block.select_one("dd .ux-textspans")
            if label_tag and value_tag:
                label = label_tag.get_text(strip=True)
                value = value_tag.get_text(strip=True)
                specs[label] = value

        print(f"{Fore.GREEN}✅ Successfully scraped product details for URL: {url}")
        return {
            "description": full_desc,
            "specs": specs
        }
