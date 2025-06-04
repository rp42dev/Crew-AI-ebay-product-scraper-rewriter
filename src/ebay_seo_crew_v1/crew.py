# src/ebay_seo_crew/crew.py

import warnings
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, crew, agent, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import ScrapeElementFromWebsiteTool, FileReadTool

# Initialize the tool
scrape_tool = ScrapeElementFromWebsiteTool()

from typing import List

from tools.ebay_listing_collector import EbayListingCollectorTool
from tools.product_scraper_tool import ProductScraperTool
# from tools.product_scraper import ProductScraperTool

warnings.filterwarnings("ignore")

@CrewBase
class EbaySeoCrew:
    """
    Crew for scraping eBay listings and rewriting them for SEO.
    """
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def listing_collector_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["listing_collector_agent"],
            tools=[EbayListingCollectorTool()],
            verbose=True
        )

    @agent
    def product_scraper_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["product_scraper_agent"],
            tools=[ProductScraperTool()],
            verbose=True
        )

    @agent
    def seo_rewriter_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["seo_rewriter_agent"],
            verbose=True
        )

    @task
    def scrape_listing_urls_task(self) -> Task:
        return Task(
            config=self.tasks_config["scrape_listing_urls"],
            agent=self.listing_collector_agent(),
            output_format="json"
        )

    @task
    def scrape_product_details_task(self) -> Task:
        return Task(
            config=self.tasks_config["scrape_product_details"],
            agent=self.product_scraper_agent(),
            # output_file="output/product_details.json",
        )

    @task
    def rewrite_listings_task(self) -> Task:
        return Task(
            config=self.tasks_config["rewrite_seo_listings"],
            agent=self.seo_rewriter_agent(),
            output_file="output/seo_rewritten_listings.md",
            output_format="markdown"
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[
                self.listing_collector_agent(),
                self.product_scraper_agent(),
                self.seo_rewriter_agent()
            ],
            tasks=[
                self.scrape_listing_urls_task(),
                self.scrape_product_details_task(),
                self.rewrite_listings_task()
            ],
            memory=True,
            verbose=True
        )
