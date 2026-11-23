import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants.json")
JS_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants_data.js")

with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

for r in data:
    rid = r["id"]

    # 1. STAR KABAB & RESTAURANT (2026 Verified Counter Menu)
    if rid == "star-kabab":
        r["menu_categories"] = [
            {
                "category_name": "Signature Kacchi, Biryani & Khichuri",
                "items": [
                    {"name": "Star Special Mutton Kacchi Biryani", "description": "Authentic Dhakaiya style mutton kacchi biryani cooked with chinigura rice, potato and tender mutton.", "price": 260, "currency": "BDT", "is_bestseller": True},
                    {"name": "Mutton Kacchi with Kebab", "description": "Mutton kacchi served with signature chicken jali kebab.", "price": 290, "currency": "BDT", "is_bestseller": True},
                    {"name": "Mutton Kacchi with Kebab & Egg", "description": "Complete meal with mutton kacchi, jali kebab and boiled egg.", "price": 320, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chicken Bhuna Khichuri", "description": "Rich deep-flavored moong dal khichuri served with spiced chicken quarter.", "price": 230, "currency": "BDT", "is_bestseller": True},
                    {"name": "Mutton Bhuna Khichuri", "description": "Slow cooked yellow khichuri served with soft tender mutton.", "price": 270, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chicken Biryani / Shahi Polao", "description": "Aromatic ghee rice served with chicken roast and gravy.", "price": 230, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Famous Curries & Breakfast Delights",
                "items": [
                    {"name": "Special Beef Nehari (With Bone Marrow)", "description": "Star Kabab's legendary slow-simmered bone marrow stew with ginger and green chilies.", "price": 190, "currency": "BDT", "is_bestseller": True},
                    {"name": "Mutton Rezala", "description": "Tender goat meat pieces cooked in rich yogurt, poppy seed and cashew gravy.", "price": 280, "currency": "BDT", "is_bestseller": True},
                    {"name": "Mutton Kala Bhuna", "description": "Caramelized dark spiced mutton curry.", "price": 320, "currency": "BDT", "is_bestseller": True},
                    {"name": "Broiler Chicken Jhal Fry", "description": "Spicy chicken pieces tossed with green chilies, onions and rich red gravy.", "price": 170, "currency": "BDT", "is_bestseller": True},
                    {"name": "Single Chicken Roast", "description": "Quarter leg chicken roast in onion barista gravy.", "price": 160, "currency": "BDT", "is_bestseller": False},
                    {"name": "Mutton Dal Gosht", "description": "Chana dal cooked with spiced mutton cubes.", "price": 220, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Breads, Desserts & Drinks",
                "items": [
                    {"name": "Special Butter Naan", "description": "Fluffy tandoor-baked bread glazed with cow butter.", "price": 45, "currency": "BDT", "is_bestseller": True},
                    {"name": "Plain Tandoori Naan", "description": "Traditional tandoor baked leavened bread.", "price": 25, "currency": "BDT", "is_bestseller": False},
                    {"name": "Special Faluda (Glass)", "description": "Chilled rose milk, vermicelli, sabja seeds, jelly and kulfi ice cream.", "price": 150, "currency": "BDT", "is_bestseller": True},
                    {"name": "Sweet Curd Lassi", "description": "Hand-churned yogurt lassi.", "price": 90, "currency": "BDT", "is_bestseller": True},
                    {"name": "Star Special Borhani", "description": "Spiced mint and black salt yogurt drink.", "price": 60, "currency": "BDT", "is_bestseller": True},
                    {"name": "Shahi Firni (Clay Pot)", "description": "Ground rice sweet pudding with pistachios.", "price": 40, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]

    # 2. TASTY TREAT (2026 Official Retail & Bakery Menu)
    elif rid == "tasty-treat":
        r["menu_categories"] = [
            {
                "category_name": "Hot Fast Food & Savouries",
                "items": [
                    {"name": "Crispy Chicken Burger", "description": "Golden battered crispy chicken patty with cheese and mayo on soft sesame bun.", "price": 170, "currency": "BDT", "is_bestseller": True},
                    {"name": "Fried Rice with Spicy Chicken Drumstick (1:1)", "description": "Egg fried rice served with crispy spicy fried drumstick and coleslaw.", "price": 180, "currency": "BDT", "is_bestseller": True},
                    {"name": "Steamed Chicken Momo (5 Pcs)", "description": "Delicate steamed handmade dumplings with spicy garlic chili dipping sauce.", "price": 150, "currency": "BDT", "is_bestseller": True},
                    {"name": "Fried Chicken Shawarma Roll", "description": "Crispy chicken strips with garlic sauce and vegetables wrapped in tortilla.", "price": 150, "currency": "BDT", "is_bestseller": True},
                    {"name": "Sausage Delight Mini Pizza", "description": "Loaded with sliced chicken sausage, bell pepper and mozzarella.", "price": 100, "currency": "BDT", "is_bestseller": True},
                    {"name": "Creamy Chicken & Mushroom Pie", "description": "Flaky puff pastry stuffed with creamy mushroom chicken filling.", "price": 90, "currency": "BDT", "is_bestseller": False},
                    {"name": "Chicken Bao (75g)", "description": "Soft pillowy steamed Asian bun with seasoned chicken filling.", "price": 50, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Fresh Breads & Daily Buns",
                "items": [
                    {"name": "Fresh Butter Bun (100g)", "description": "Sweet soft pillowy baked bun glazed with pure butter.", "price": 40, "currency": "BDT", "is_bestseller": True},
                    {"name": "Fresh Milk Bread Loaf (350g)", "description": "Daily baked fresh sandwich bread.", "price": 80, "currency": "BDT", "is_bestseller": True},
                    {"name": "Family Milk Bread (700g)", "description": "Large family loaf of soft milk bread.", "price": 150, "currency": "BDT", "is_bestseller": False},
                    {"name": "Special Fruit Bun", "description": "Sweet bun studded with raisins and tutti-frutti.", "price": 50, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Pastry Slices & Whole Celebration Cakes",
                "items": [
                    {"name": "Chocolate Triangle Pastry (60g)", "description": "Decadent dark chocolate sponge layered with cocoa cream.", "price": 120, "currency": "BDT", "is_bestseller": True},
                    {"name": "Red Velvet Heart Pastry (80g)", "description": "Crimson sponge with creamy vanilla frosting.", "price": 170, "currency": "BDT", "is_bestseller": True},
                    {"name": "Mini Black Forest Cake (100g)", "description": "Layered cherry and chocolate mini cake.", "price": 160, "currency": "BDT", "is_bestseller": True},
                    {"name": "Vanilla Triangle Pastry", "description": "Light vanilla sponge with butter cream layer.", "price": 110, "currency": "BDT", "is_bestseller": False},
                    {"name": "Standard Chocolate Celebration Cake (500g)", "description": "1/2 kg freshly baked celebration cake for birthdays.", "price": 650, "currency": "BDT", "is_bestseller": True},
                    {"name": "Premium Black Forest Cake (1 kg)", "description": "1 kg full celebration cake loaded with chocolate flakes and cherries.", "price": 1200, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]

    # 3. HERFY BANGLADESH (2026 Official Counter Menu)
    elif rid == "herfy-bangladesh":
        r["menu_categories"] = [
            {
                "category_name": "Famous Big Herfy & Classic Burgers",
                "items": [
                    {"name": "Big Herfy Beef Burger", "description": "Quarter pound 100% pure beef patty, sesame seed bun, cheddar cheese, pickles and Herfy special sauce.", "price": 399, "currency": "BDT", "is_bestseller": True},
                    {"name": "Big Herfy Beef Combo Meal", "description": "Big Herfy burger served with golden french fries and soft drink.", "price": 598, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chicken Cheese Burger", "description": "Tender chicken patty topped with melted cheddar and fresh lettuce.", "price": 379, "currency": "BDT", "is_bestseller": True},
                    {"name": "Grilled Chicken Burger", "description": "Flame-grilled chicken breast with herb sauce and tomatoes.", "price": 389, "currency": "BDT", "is_bestseller": True},
                    {"name": "Angus Beef Burger (Premium)", "description": "Gourmet black Angus beef patty with caramelized onions and gourmet sauce.", "price": 679, "currency": "BDT", "is_bestseller": True},
                    {"name": "Double Herfy Beef Burger", "description": "Double pure beef patties, double cheese slices and signature relish.", "price": 639, "currency": "BDT", "is_bestseller": True},
                    {"name": "Mini Beef Cheese Burger", "description": "Single small beef slider with cheese.", "price": 259, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Crispy & Broasted Chicken Buckets",
                "items": [
                    {"name": "Herfy Fried Chicken (1 Pc)", "description": "Golden battered spiced fried chicken.", "price": 169, "currency": "BDT", "is_bestseller": False},
                    {"name": "Herfy Fried Chicken (2 Pcs)", "description": "2 pieces of crunchy fried chicken with dipping sauce.", "price": 319, "currency": "BDT", "is_bestseller": True},
                    {"name": "Herfy Fried Chicken (4 Pcs)", "description": "4 pieces of hot & crispy chicken.", "price": 599, "currency": "BDT", "is_bestseller": True},
                    {"name": "Herfy Chicken Bucket (8 Pcs)", "description": "Family sharing bucket of 8 pieces crispy chicken.", "price": 1179, "currency": "BDT", "is_bestseller": True},
                    {"name": "Crispy Chicken Wings (6 Pcs)", "description": "Golden battered wings with sweet chili dip.", "price": 299, "currency": "BDT", "is_bestseller": False},
                    {"name": "Crispy Chicken Strips (6 Pcs)", "description": "100% chicken breast boneless tenders.", "price": 489, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Sides, Soft Serves & Beverages",
                "items": [
                    {"name": "Herfy French Fries (Regular)", "description": "Crispy golden salted fries.", "price": 159, "currency": "BDT", "is_bestseller": True},
                    {"name": "Herfy French Fries (Large)", "description": "Large portion of golden fries.", "price": 189, "currency": "BDT", "is_bestseller": False},
                    {"name": "Soft Serve Ice Cream Cone", "description": "Creamy dairy vanilla soft serve in wafer cone.", "price": 119, "currency": "BDT", "is_bestseller": True},
                    {"name": "Herfy Cold Coffee (12 oz)", "description": "Chilled blended espresso with creamy milk.", "price": 269, "currency": "BDT", "is_bestseller": True},
                    {"name": "Virgin Mojito Fizz", "description": "Refreshing fresh mint and lime sparkling cooler.", "price": 189, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]

    # 4. BFC (BEST FRIED CHICKEN - 2026 Official Counter Menu)
    elif rid == "bfc-bangladesh":
        r["menu_categories"] = [
            {
                "category_name": "Crispy Fried Chicken (Portions & Buckets)",
                "items": [
                    {"name": "2 Pcs Fried Chicken (1 Thigh, 1 Leg)", "description": "Classic recipe crispy golden fried chicken with savory dipping sauce.", "price": 220, "currency": "BDT", "is_bestseller": True},
                    {"name": "3 Pcs Fried Chicken (1 Rib, 1 Thigh, 1 Leg)", "description": "3 pieces of crunchy deep-fried chicken.", "price": 330, "currency": "BDT", "is_bestseller": True},
                    {"name": "5 Pcs Fried Chicken Feast", "description": "5 pieces of signature crispy fried chicken.", "price": 550, "currency": "BDT", "is_bestseller": True},
                    {"name": "9 Pcs Midi Bucket", "description": "Sharing bucket of 9 pieces crispy chicken.", "price": 980, "currency": "BDT", "is_bestseller": True},
                    {"name": "12 Pcs Family Bucket", "description": "Generous 12 pieces crispy chicken bucket for the whole family.", "price": 1300, "currency": "BDT", "is_bestseller": True},
                    {"name": "15 Pcs Maxi Bucket", "description": "Large 15 pieces fried chicken barrel.", "price": 1620, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Wings, Pops & Chicken Burgers",
                "items": [
                    {"name": "BFC Hot Wings (8 Pcs)", "description": "Spicy seasoned chicken wings with crisp coating.", "price": 250, "currency": "BDT", "is_bestseller": True},
                    {"name": "Naga Chicken Pops (30 Pcs)", "description": "Bite-sized chicken popcorn tossed in fiery naga chili seasoning.", "price": 205, "currency": "BDT", "is_bestseller": True},
                    {"name": "Crispy Chicken Strips (6 Pcs)", "description": "Boneless chicken breast tenders with honey mustard.", "price": 300, "currency": "BDT", "is_bestseller": False},
                    {"name": "BFC Supreme Chicken Burger", "description": "Crunchy chicken breast patty with cheese, fresh lettuce and mayo.", "price": 260, "currency": "BDT", "is_bestseller": True},
                    {"name": "BFC Classic Chicken Burger", "description": "Seasoned chicken patty with special sauce.", "price": 220, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Sides & Soft Drinks",
                "items": [
                    {"name": "BFC French Fries (Large)", "description": "Golden crisp salted potato fries.", "price": 140, "currency": "BDT", "is_bestseller": True},
                    {"name": "Fresh Coleslaw Salad", "description": "Shredded cabbage and carrots in sweet creamy mayo dressing.", "price": 60, "currency": "BDT", "is_bestseller": True},
                    {"name": "Dinner Roll Bun", "description": "Soft butter bun.", "price": 30, "currency": "BDT", "is_bestseller": False},
                    {"name": "Chilled Soft Drink (500ml)", "description": "Choice of Coke, Sprite, or Fanta.", "price": 50, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]

    # 5. KACCHI BHAI (2026 Updated Rates)
    elif rid == "kacchi-bhai":
        for cat in r.get("menu_categories", []):
            for item in cat.get("items", []):
                if item["name"] == "Basmati Kacchi Biryani (1:1)":
                    item["price"] = 350
                elif item["name"] == "Kacchi Khadok (1:1 - 4 Pcs Mutton)":
                    item["price"] = 530
                elif item["name"] == "Special Borhani (Glass)":
                    item["price"] = 70
                elif item["name"] == "Shahi Firni (Clay Pot)":
                    item["price"] = 70

    # 6. SULTAN'S DINE (2026 Updated Rates)
    elif rid == "sultans-dine":
        for cat in r.get("menu_categories", []):
            for item in cat.get("items", []):
                if item["name"] == "Basmati Kacchi Biryani (Half - 1:1)":
                    item["price"] = 350
                elif item["name"] == "Basmati Kacchi Biryani (Full - 1:2)":
                    item["price"] = 650
                elif item["name"] == "Sultan's Special Borhani (Glass 250ml)":
                    item["price"] = 60
                elif item["name"] == "Shahi Firni (Clay Pot)":
                    item["price"] = 70

    # 7. KFC BANGLADESH (2026 Updated Rates)
    elif rid == "kfc-bangladesh":
        for cat in r.get("menu_categories", []):
            for item in cat.get("items", []):
                if item["name"] == "1 Pc Hot & Crispy Chicken":
                    item["price"] = 169
                elif item["name"] == "2 Pcs Hot & Crispy Chicken":
                    item["price"] = 329
                elif item["name"] == "KFC Classic Zinger Burger":
                    item["price"] = 359
                elif item["name"] == "Potato Wedges":
                    item["price"] = 169

with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

with open(JS_FILE, "w", encoding="utf-8") as f:
    f.write("window.RESTAURANTS_DATA = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n")

print("2026 Real-Time Inflation & Official Counter Price Alignment Complete!")
