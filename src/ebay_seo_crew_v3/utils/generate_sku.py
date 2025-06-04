import json
import random
import string
import sys
import os

# --- SKU generator function ---
def generate_sku(data):
    title = data.get("rewritten_title", "Generic Product")
    specs = data.get("specs", {})

    title_lower = title.lower()
    known_categories = {
        "bike": "BIK",
        "helmet": "HLM",
        "scooter": "SCT",
        "jacket": "JKT",
        "lamp": "LMP",
        "watch": "WCH",
    }
    category = "GEN"
    for keyword, code in known_categories.items():
        if keyword in title_lower or keyword in specs.get("Type", "").lower():
            category = code
            break

    size = specs.get("Wheel Size") or specs.get("Size") or specs.get("Model") or "00"
    size = ''.join(filter(str.isalnum, size.upper()))[:6] or "00"

    dept = specs.get("Department", "").lower()
    if "kid" in dept:
        dept_code = "UK"
    elif "men" in dept:
        dept_code = "MA"
    elif "women" in dept:
        dept_code = "FA"
    else:
        dept_code = "UN"

    def short_token(text):
        words = text.split()
        if len(words) < 2:
            words.append("X")
        return ''.join(w[:3].upper() for w in words[:2])

    rand = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"{category}-{size}-{dept_code}-{short_token(title)}-{rand}"

# --- Main logic with CLI support ---
def main(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"❌ Input file not found: {input_file}")
        return

    with open(input_file, "r", encoding="utf-8") as f:
        products = json.load(f)

    for product in products:
        product["sku"] = generate_sku(product)
        print(f"{product['sku']} | {product['rewritten_title']}")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)

    print(f"\n✅ SKUs saved to: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_sku.py <input_file.json> <output_file.json>")
    else:
        main(sys.argv[1], sys.argv[2])

