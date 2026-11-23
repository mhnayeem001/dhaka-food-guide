"""
Automated Dhaka Restaurant & Menu Adder
Allows scraping / adding new restaurants with full branch locations and dine-in menus into the database.
"""

import sys
import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants.json")

def add_or_update_restaurant(restaurant_obj):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Check if exists
    existing_idx = None
    for idx, r in enumerate(data):
        if r["id"] == restaurant_obj["id"] or r["name"].lower() == restaurant_obj["name"].lower():
            existing_idx = idx
            break
            
    if existing_idx is not None:
        data[existing_idx] = restaurant_obj
        print(f"Updated existing restaurant: {restaurant_obj['name']}")
    else:
        data.append(restaurant_obj)
        print(f"Added new restaurant: {restaurant_obj['name']}")
        
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    js_file = os.path.join(os.path.dirname(DATA_FILE), "restaurants_data.js")
    with open(js_file, "w", encoding="utf-8") as f:
        f.write("window.RESTAURANTS_DATA = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n")
        
    print(f"Database now has {len(data)} restaurants.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        json_path = sys.argv[1]
        with open(json_path, "r", encoding="utf-8") as f:
            new_r = json.load(f)
            add_or_update_restaurant(new_r)
    else:
        print("Usage: python scripts/add_restaurant.py <path_to_restaurant_json>")
