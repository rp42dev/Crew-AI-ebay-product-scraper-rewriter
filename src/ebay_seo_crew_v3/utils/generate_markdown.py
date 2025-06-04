import json
import os

def product_to_markdown(product):
    sku = product.get("sku", "unknown-sku")
    title = product.get("rewritten_title", "No Title")
    subtitle = product.get("subtitle", "")
    description = product.get("rewritten_description", "")
    key_specs = product.get("key_specs", [])
    specs = product.get("specs", {})
    keywords = product.get("seo_keywords", [])
    meta_title = product.get("seo_title", "")
    meta_description = product.get("seo_description", "")
    url = product.get("original_url", "#")

    md = []
    md.append(f"# {title}\n")
    
    if subtitle:
        md.append(f"### {subtitle}\n")
    md.append(description + "\n")

    if sku:
        md.append(f"**SKU:** {sku}\n")
    
    if key_specs:
        md.append("**Key Features:**")
        for spec in key_specs:
            md.append(f"- {spec}")
        md.append("")

    if specs:
        md.append("**Full Specifications:**")
        for k, v in specs.items():
            md.append(f"- **{k}**: {v}")
        md.append("")
        
    if meta_title:
        md.append(f"**SEO Title:** {meta_title}\n")
        
    if meta_description:
        md.append(f"**SEO Description:** {meta_description}\n")

    if keywords:
        md.append(f"**SEO Keywords:** {', '.join(keywords)}\n")

    md.append(f"[🔗 View Original Product]({url})\n")

    return "\n".join(md), sku

def generate_markdown_files(json_path, output_dir="src/ebay_seo_crew_v3/output/markdown_products"):
    os.makedirs(output_dir, exist_ok=True)

    with open(json_path, "r", encoding="utf-8") as f:
        products = json.load(f)

    for product in products:
        markdown, sku = product_to_markdown(product)
        filename = f"{sku}.md"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w", encoding="utf-8") as out_file:
            out_file.write(markdown)

    print(f"✅ Generated {len(products)} Markdown files in '{output_dir}/'")

if __name__ == "__main__":
    generate_markdown_files("src/ebay_seo_crew_v3/output/products_with_sku.json", "src/ebay_seo_crew_v3/output/markdown_products")
