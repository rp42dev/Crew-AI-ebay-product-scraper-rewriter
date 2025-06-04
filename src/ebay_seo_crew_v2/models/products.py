from pydantic import BaseModel, Field
from typing import Dict, List


class SEOProductInput(BaseModel):
    title: str = Field(..., description="Original eBay product title")
    price: str = Field(..., description="Original price text")
    url: str = Field(..., description="Product listing URL")
    description: str = Field(..., description="Full scraped description")
    specs: Dict[str, str] = Field(default_factory=dict, description="Product specs as key-value pairs")


class ProductListPayload(BaseModel):
    products: List[SEOProductInput]


class SEOProductOutput(BaseModel):
    rewritten_title: str = Field(..., max_length=80, description="SEO-optimized title")
    subtitle: str = Field(..., max_length=100, description="SEO-optimized subtitle")
    rewritten_description: str = Field(..., description="Optimized product description")
    key_specs: List[str] = Field(..., min_items=3, max_items=5, description="List of 3–5 key spec bullet points")
    specs: Dict[str, str] = Field(default_factory=dict, description="Product specs as key-value pairs")
    seo_keywords: List[str] = Field(..., min_items=1, max_items=3, description="2–3 high-value keywords")
    original_url: str = Field(..., description="Original eBay product URL")


class SEOProductOutputList(BaseModel):
    products: List[SEOProductOutput] = Field(..., description="List of SEO-optimized products")
    
    def to_dict(self):
        return [product.dict() for product in self.products]