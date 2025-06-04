# 🔢 SKU Generator – Simple Explanation

This Python script automatically generates a unique SKU (Stock Keeping Unit) for each product based on its details.

## ✅ What the Code Does

- Reads product info (like title, specs, etc.)
- Picks out useful data such as:
  - What kind of product it is (bike, helmet, etc.)
  - Size or model number
  - Who it's for (kids, men, women, etc.)
  - Short keywords from the title
  - Builds a SKU like this: BIK-24-UK-MOUNBIK-X7A2

## 🧱 What Each Part of the SKU Means

| Part        | Example  | Meaning                        |
|-------------|----------|--------------------------------|
| `BIK`       | BIK      | Product type (e.g., bike)      |
| `24`        | 24       | Size or model info             |
| `UK`        | UK       | Target audience (Unisex Kids)  |
| `MOUNBIK`   | MOUNBIK  | Shortened product title        |
| `X7A2`      | X7A2     | Random code for uniqueness     |

## 🛡 Backup Rules (Fallbacks)

- If title is missing → use `"Generic Product"`
- If size is missing → use `"00"`
- If audience unknown → use `"UN"`
- If category not found → use `"GEN"`

That’s it — simple, fast SKU creation for any product!
