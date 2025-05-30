# src/ebay_seo_crew/crew.py

import warnings
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, crew, agent, task
from crewai.agents.agent_builder.base_agent import BaseAgent

from typing import List

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
    def seo_rewriter_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["seo_rewriter_agent"],
            verbose=True
        )

    @task
    def rewrite_listings_task(self) -> Task:
        return Task(
            config=self.tasks_config["rewrite_seo_listings"],
            agent=self.seo_rewriter_agent(),
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[
                self.seo_rewriter_agent()
            ],
            tasks=[
                self.rewrite_listings_task()
            ],
            memory=False,
            verbose=True
        )

