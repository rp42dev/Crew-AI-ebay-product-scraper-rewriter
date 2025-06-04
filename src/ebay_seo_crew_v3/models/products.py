from pydantic import BaseModel, Field
from typing import Dict, List
from pydantic.types import Annotated


class SEOProductInput(BaseModel):
    title: str = Field(..., description="Original eBay product title")
    price: str = Field(..., description="Original price text")
    url: str = Field(..., description="Product listing URL")
    description: str = Field(..., description="Full scraped description")
    specs: Dict[str, str] = Field(default_factory=dict, description="Product specs as key-value pairs")


class ProductListPayload(BaseModel):
    products: List[SEOProductInput]


class SEOProductOutput(BaseModel):
    rewritten_title: str = Field(
        ..., description="SEO-optimized product title starting with main keyword"
    )
    subtitle: str = Field(
        ..., description="Short benefit-driven phrase to entice user"
    )
    rewritten_description: str = Field(
        ..., description="3-paragraph max summary, use cases, trust-building"
    )
    key_specs: List[str] = Field(
        ..., description="Exactly 5 bullet points. Format: - **Feature** – benefit + keyword"
    )
    specs: Dict[str, str] = Field(
        ..., description="Original key-value product specifications"
    )
    seo_keywords: List[str] = Field(
        ..., description="2–3 high-value keywords"
    )
    original_url: str = Field(
        ..., description="Canonical eBay product URL"
    )


class SEOProductOutputList(BaseModel):
    products: List[SEOProductOutput]