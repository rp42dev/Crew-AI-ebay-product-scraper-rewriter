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