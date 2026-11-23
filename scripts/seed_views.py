"""
Seed initial view counts across all 505 restaurants in data/restaurants.json:
- Neighborhood spots: 2 to 6 views
- Iconic top chains: 12 to 35 views
"""
import json
import os
import random

def seed_views():
    db_path = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants.json")
    with open(db_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for r in data:
        if "view_count" not in r or r["view_count"] < 2:
            raw_rev = str(r.get("review_count", 0)).replace(',', '').replace('+', '')
            try:
                reviews = int(raw_rev)
            except:
                reviews = 500
            if reviews > 5000:
                r["view_count"] = random.randint(15, 35)
            elif reviews > 2000:
                r["view_count"] = random.randint(8, 18)
            else:
                r["view_count"] = random.randint(2, 6)

    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    js_path = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants_data.js")
    with open(js_path, "w", encoding="utf-8") as f:
        f.write("window.RESTAURANTS_DATA = " + json.dumps(data, ensure_ascii=False, indent=2) + ";\n")

    print(f"Seeded initial view counts for all {len(data)} restaurants successfully!")

if __name__ == "__main__":
    seed_views()
