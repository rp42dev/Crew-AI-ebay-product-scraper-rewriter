# 📝 Product Markdown Generator

This tool converts structured product JSON data (with SEO-optimized fields) into clean, readable Markdown files — one per product.

## 💼 What It Does

- Reads a JSON file (`products.json`) with product listings.
- Each product includes fields like:
  - `rewritten_title`
  - `subtitle`
  - `rewritten_description`
  - `key_specs`
  - `specs`
  - `seo_keywords`
  - `original_url`
  - `sku`
- Generates one `.md` file per product (named with `sku.md`).
- Saves them in a folder named `markdown_products`.

## ▶️ How to Use

1. Place your scraped/rewritten product JSON in a file called `products.json`
2. Run the script:

```bash
python generate_markdown.py
```
Your Markdown files will be saved in the markdown_products/ folder.

✅ Example
If your JSON contains:

```json
{
  "rewritten_title": "Mountain Bike 2024",
  "subtitle": "Best for Off-Road Adventures",
  "rewritten_description": "This mountain bike is perfect for all terrains.",
  "key_specs": ["Lightweight", "Durable", "High Performance"],
  "specs": {"Color": "Red", "Size": "Medium"},
  "seo_keywords": ["mountain bike", "2024 model", "off-road"],
  "original_url": "https://example.com/mountain-bike-2024",
  "sku": "BIK-24-UK-MOUNBIK-X7A2"
}
```

It will create a file named `BIK-24-UK-MOUNBIK-X7A2.md` with the following content:

```markdown
# Mountain Bike 2024
Best for Off-Road Adventures
## Description
This mountain bike is perfect for all terrains. 
## Key Specifications
- Lightweight
- Durable
- High Performance
## Specifications
- Color: Red
- Size: Medium
## SEO Keywords
- mountain bike
- 2024 model
- off-road
## Original URL
[Mountain Bike 2024](https://example.com/mountain-bike-2024)
## SKU
BIK-24-UK-MOUNBIK-X7A2
```
