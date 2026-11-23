"""
Master Audit of Dhaka Restaurant Prices
Inspects and compares dine-in counter pricing across iconic chains.
"""
import json

targets = [
    'sultans-dine', 'kacchi-bhai', 'star-kabab', 'kfc-bangladesh', 
    'takeout', 'chillox', 'pizzaburg', 'herfy-bangladesh', 'bfc', 
    'cp-five-star-mirpur', 'ghoroa-hotel', 'madchef', 'helvetia-bangladesh'
]

with open('data/restaurants.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for r in data:
    if r['id'] in targets:
        print(f"\n=== {r['name']} ({r['id']}) ===")
        for cat in r.get('menu_categories', []):
            cat_name = cat.get('category_name') or cat.get('category')
            print(f"  [{cat_name}]")
            for item in cat.get('items', [])[:4]:
                print(f"    - {item['name']}: ৳{item['price']}")
