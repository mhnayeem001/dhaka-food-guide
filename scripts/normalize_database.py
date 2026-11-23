"""
Normalize and standardize all restaurants in data/restaurants.json:
- Converts any 'menu' list with 'category' fields into standard 'menu_categories'
- Ensures all fields (tagline, price_range, price_type, hotline, total_branches) exist
- Syncs data/restaurants.json and data/restaurants_data.js
"""
import json
import os
from collections import defaultdict

def normalize_database():
    db_path = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants.json")
    with open(db_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    normalized_count = 0
    total_items_count = 0
    total_branches_count = 0

    for r in data:
        # 1. Normalize menu -> menu_categories
        if "menu_categories" not in r or not r["menu_categories"]:
            if "menu" in r and r["menu"]:
                cat_dict = defaultdict(list)
                for item in r["menu"]:
                    cat_name = item.get("category", "Popular Items")
                    cat_dict[cat_name].append({
                        "id": item.get("id", f"{r['id']}-{len(cat_dict[cat_name])+1}"),
                        "name": item.get("name", ""),
                        "price": item.get("price", 0),
                        "description": item.get("description", ""),
                        "category": cat_name,
                        "popular": item.get("popular", False),
                        "is_veg": item.get("is_veg", False)
                    })
                r["menu_categories"] = [
                    {"category": cat, "items": items}
                    for cat, items in cat_dict.items()
                ]
                normalized_count += 1
            else:
                r["menu_categories"] = []

        # Standardize helper fields
        if "total_branches" not in r or r["total_branches"] != len(r.get("branches", [])):
            r["total_branches"] = len(r.get("branches", []))
        total_branches_count += r["total_branches"]

        if "price_type" not in r:
            r["price_type"] = "Counter / Dine-In (No Markup)"
        
        if "price_range" not in r and "price_tier" in r:
            r["price_range"] = r["price_tier"]
        elif "price_range" not in r:
            r["price_range"] = "৳৳"

        if "tagline" not in r:
            cuisine_str = ", ".join(r.get("cuisine", ["Authentic Dhaka Food"]))
            r["tagline"] = f"Authentic {cuisine_str} across Dhaka"

        if "hotline" not in r:
            branches = r.get("branches", [])
            r["hotline"] = branches[0].get("phone", "+880 1700-000000") if branches else "+880 1700-000000"

        # Count items
        items_in_r = sum(len(c.get("items", [])) for c in r.get("menu_categories", []))
        total_items_count += items_in_r

    # Save to restaurants.json
    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Save to restaurants_data.js
    js_path = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants_data.js")
    with open(js_path, "w", encoding="utf-8") as f:
        f.write("window.RESTAURANTS_DATA = " + json.dumps(data, ensure_ascii=False, indent=2) + ";\n")

    print(f"Database Normalization Complete!")
    print(f"Total Restaurants: {len(data)}")
    print(f"Total Outlets: {total_branches_count}")
    print(f"Total Categorized Menu Items: {total_items_count}")
    print(f"Restaurants newly structured into categories: {normalized_count}")

if __name__ == "__main__":
    normalize_database()
