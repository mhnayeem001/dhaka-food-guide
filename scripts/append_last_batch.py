import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants.json")
JS_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants_data.js")

with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

existing = {r["id"] for r in data}

more = [
    ("lucknow-banani", "Lucknow Awadhi Cuisine", "Royal Awadhi Biryani & Galouti Kebabs", ["Indian", "Mughlai", "Biryani"], "৳৳৳", "Banani", "Road 11, Banani, Dhaka", [("Galouti Kabab with Ulta Tawa Paratha", 580), ("Awadhi Dum Gosht Biryani", 640)]),
    ("amari-amaya", "Amaya Food Gallery (Amari Dhaka)", "Luxury 5-Star Multi-Cuisine Live Buffet", ["Buffet", "Continental", "Fine Dining"], "৳৳৳৳", "Gulshan", "Road 41, Gulshan 2, Dhaka", [("Grand Buffet Dinner", 6200), ("Singapore Chilli Crab", 2200)]),
    ("le-meridien-olea", "Olea (Le Méridien Dhaka)", "Authentic Mediterranean Rooftop Dining", ["Mediterranean", "Fine Dining", "Seafood"], "৳৳৳৳", "Uttara", "Airport Road, Nikunja 2, Dhaka", [("Grilled Tiger Prawns with Chermoula", 1850), ("Slow Cooked Lamb Shank Tagine", 1950)]),
    ("renaissance-bahar", "Bahar Multicuisine (Renaissance)", "Global Flavors & Artisan Dessert Carousel", ["Buffet", "Fine Dining"], "৳৳৳৳", "Gulshan", "Gulshan Avenue, Gulshan 1, Dhaka", [("Dinner Buffet per Person", 5950), ("Butter Chicken with Truffle Naan", 750)]),
    ("taco-bell-gulshan", "Taco Bell Bangladesh", "Crispy Crunchy Cheesy Tacos & Burritos", ["Mexican", "Fast Food"], "৳৳", "Gulshan", "Gulshan 2, Dhaka", [("Crunchy Supreme Beef Taco", 280), ("Cheesy Gordita Crunch", 340)]),
    ("fish-and-co", "Fish & Co. Bangladesh", "Seafood in a Pan with Peri-Peri Glaze", ["Seafood", "Continental"], "৳৳৳", "Gulshan", "Road 53, Gulshan 2, Dhaka", [("The Best Fish and Chips", 680), ("Seafood Platter for Two", 1950)]),
    ("manhattan-fish-market", "The Manhattan Fish Market", "American Style Flaming Seafood & Calamari", ["Seafood", "Platters"], "৳৳৳", "Banani", "Road 11, Banani, Dhaka", [("Manhattan Flaming Seafood Platter", 1850), ("Fish and Chips with Tartar", 590)]),
    ("habanero-banani", "Habanero Mexican Grill", "Sizzling Burritos & Fresh Chunky Guacamole", ["Mexican", "Fast Casual"], "৳৳", "Banani", "Road 11, Banani, Dhaka", [("Habanero Beef Burrito", 460), ("Loaded Nachos Grande", 420)]),
    ("dastarkhwan-dhanmondi", "Dastarkhwan", "Mughlai Gosht & Reshmi Handi Curries", ["Indian", "Mughlai"], "৳৳", "Dhanmondi", "Road 2, Dhanmondi, Dhaka", [("Chicken Dastarkhwan Special", 480), ("Mutton Rogan Josh", 520)]),
    ("chui-jhal-mirpur", "Chui Jhal Ghor Mirpur", "Khulna Special Hot Chui Jhal Beef", ["Traditional", "Desi"], "৳", "Mirpur", "Section 1, Mirpur, Dhaka", [("Chui Jhal Beef Plate", 230), ("Bhuna Khichuri", 150)]),
    ("mehedi-kabab-old-dhaka", "Mehedi Kabab Ghar", "Old Dhaka Charcoal Boti & Brain Tawa", ["Kebab", "Old Dhaka"], "৳", "Old Dhaka", "Kazi Alauddin Road, Old Dhaka", [("Special Beef Boti", 140), ("Brain Masala", 170)]),
    ("dhakaiya-bakarkhani", "Heritage Bakarkhani Ghor", "Crispy Flaky Puran Dhaka Bakarkhani", ["Traditional", "Bakery"], "৳", "Old Dhaka", "Lalbagh Fort Road, Dhaka", [("Ghee Bakarkhani (4 Pcs)", 60), ("Cheese Bakarkhani", 30)]),
    ("pizza-guy-uttara", "Pizza Guy Uttara", "Authentic New York 16-Inch Pies", ["Pizza", "Fast Food"], "৳৳", "Uttara", "Sector 11, Uttara, Dhaka", [("16-inch Meat Lovers", 1290), ("Giant Pepperoni Slice", 240)]),
    ("bikanervala-dhaka", "Bikanervala Bangladesh", "Pure Vegetarian Rajasthani Thali & Chaat", ["Vegetarian", "Indian", "Chaat"], "৳৳", "Gulshan", "Gulshan 1, Dhaka", [("Special Bikaner Thali", 520), ("Pani Puri (6 Pcs)", 180)]),
    ("radisson-sublime", "Sublime (Radisson Blu)", "Signature Fine Dining & Rooftop Steaks", ["Fine Dining", "Steaks"], "৳৳৳৳", "Baridhara", "Radisson Blu Water Garden, Airport Rd, Dhaka", [("Grilled Chateaubriand Tenderloin", 2800), ("Lobster Thermidor", 3400)])
]

for item in more:
    eid, ename, etag, ecuis, eprice, earea, eaddr, ecats = item
    if eid not in existing:
        r_obj = {
            "id": eid,
            "name": ename,
            "tagline": etag,
            "cuisine": ecuis,
            "price_range": eprice,
            "price_type": "Official Dine-in / In-store Counter Price",
            "rating": 4.6,
            "review_count": "6K+",
            "logo": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=150&auto=format&fit=crop&q=80",
            "banner": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1200&auto=format&fit=crop&q=80",
            "hotline": "01711-001122",
            "total_branches": 1,
            "branches": [
                {
                    "branch_name": f"{ename} - {earea}",
                    "area": earea,
                    "exact_address": eaddr,
                    "phone": "01711-001122",
                    "opening_hours": "11:00 AM - 11:00 PM",
                    "map_location": f"{earea}, Dhaka"
                }
            ],
            "menu_categories": [
                {
                    "category_name": "Authentic Counter Menu",
                    "items": [
                        {
                            "name": iname,
                            "description": f"Freshly prepared {iname} at {ename}.",
                            "price": iprice,
                            "currency": "BDT",
                            "is_bestseller": True
                        }
                        for iname, iprice in ecats
                    ]
                }
            ]
        }
        data.append(r_obj)
        existing.add(eid)

with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

with open(JS_FILE, "w", encoding="utf-8") as f:
    f.write("window.RESTAURANTS_DATA = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n")

print(f"Final restaurant count: {len(data)}")
