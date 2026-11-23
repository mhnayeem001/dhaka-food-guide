import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants.json")
JS_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants_data.js")

with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

existing_ids = {r["id"] for r in data}

new_restaurants = [
    # 1. BHOOT GRILL
    {
        "id": "bhoot-grill",
        "name": "Bhoot Grill",
        "tagline": "Iconic Spooky Themed Multi-Cuisine, Sizzling Steaks & Platters",
        "cuisine": ["Steaks", "Grill", "Continental", "Chinese"],
        "price_range": "৳৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.4,
        "review_count": "14K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01711-223344",
        "total_branches": 3,
        "branches": [
            {"branch_name": "Dhanmondi Road 2", "area": "Dhanmondi", "exact_address": "House 21, Road 2, Dhanmondi, Dhaka 1205", "phone": "01711-223344", "opening_hours": "12:00 PM - 11:00 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Gulshan 1", "area": "Gulshan", "exact_address": "Navana Tower, Gulshan 1 Circle, Dhaka", "phone": "01711-223344", "opening_hours": "12:00 PM - 11:00 PM", "map_location": "Gulshan 1, Dhaka"},
            {"branch_name": "Uttara Sector 3", "area": "Uttara", "exact_address": "Rabindra Sarani, Sector 3, Uttara, Dhaka", "phone": "01711-223344", "opening_hours": "12:00 PM - 11:00 PM", "map_location": "Uttara, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Signature Sizzlers & Steaks",
                "items": [
                    {"name": "Bhoot Special Sizzling Beef Steak", "description": "Tender cut beef steak served on sizzling iron platter with mushroom sauce, sauteed vegetables and wedges.", "price": 850, "currency": "BDT", "is_bestseller": True},
                    {"name": "Sizzling Garlic Chicken Steak", "description": "Charbroiled chicken breast tossed with roasted garlic pepper glaze and mashed potatoes.", "price": 680, "currency": "BDT", "is_bestseller": True},
                    {"name": "Sizzling T-Bone Steak (300g)", "description": "Prime grilled T-bone steak with peppercorn reduction.", "price": 1250, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Grilled Platters & Mains",
                "items": [
                    {"name": "Bhoot Monster Platter (For 2)", "description": "BBQ chicken quarter, beef kebab skewers, grilled prawn, mexican rice and onion rings.", "price": 1450, "currency": "BDT", "is_bestseller": True},
                    {"name": "Crispy Calamari Rings", "description": "Golden battered squid rings served with spicy tartar dip.", "price": 420, "currency": "BDT", "is_bestseller": False},
                    {"name": "Cream of Wild Mushroom Soup", "description": "Rich velvety fresh mushroom broth with herbs.", "price": 280, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 2. IZUMI JAPANESE KITCHEN
    {
        "id": "izumi-japanese",
        "name": "Izumi Courtyard Japanese",
        "tagline": "Dhaka's Most Prestigious Authentic Japanese Fine Dining & Courtyard Lounge",
        "cuisine": ["Japanese", "Sushi", "Sashimi", "Fine Dining"],
        "price_range": "৳৳৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.8,
        "review_count": "9.5K+",
        "logo": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1611143669185-af224c5e3252?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01726-112233",
        "total_branches": 1,
        "branches": [
            {"branch_name": "Gulshan 2 Courtyard", "area": "Gulshan", "exact_address": "House 24/C, Road 113, Gulshan 2, Dhaka 1212", "phone": "01726-112233", "opening_hours": "12:30 PM - 03:00 PM, 06:30 PM - 11:00 PM", "map_location": "Gulshan 2, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Signature Sushi & Maki Rolls",
                "items": [
                    {"name": "Izumi Special Dragon Roll (8 Pcs)", "description": "Eel, tempura prawn, avocado roll wrapped with tobiko and sweet unagi drizzle.", "price": 1650, "currency": "BDT", "is_bestseller": True},
                    {"name": "Salmon Nigiri (4 Pcs)", "description": "Air-flown Norwegian salmon laid over seasoned Japanese sushi rice.", "price": 1150, "currency": "BDT", "is_bestseller": True},
                    {"name": "Spicy Tuna Maki (8 Pcs)", "description": "Yellowfin tuna with spicy Japanese mayo, sriracha and spring onion.", "price": 1350, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Robatayaki & Hot Kitchen",
                "items": [
                    {"name": "Black Cod Saikyo Miso", "description": "Alaskan black cod marinated 72 hours in Kyoto sweet saikyo miso glaze.", "price": 2850, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chicken Yakitori Skewers (3 Pcs)", "description": "Charcoal grilled glazed chicken thighs with tare glaze.", "price": 680, "currency": "BDT", "is_bestseller": False},
                    {"name": "Wagyu Beef Ribeye (Grade A4 200g)", "description": "Melt-in-mouth Japanese Wagyu grilled on lava rock.", "price": 4900, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    },

    # 3. HOLEY ARTISAN BAKERY
    {
        "id": "holey-artisan-bakery",
        "name": "Holey Artisan Bakery",
        "tagline": "Artisanal Sourdough, French Croissants, Brunch & Gourmet Woodfired Pizzas",
        "cuisine": ["Bakery", "Breakfast & Brunch", "Specialty Coffee", "Pizza"],
        "price_range": "৳৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.7,
        "review_count": "16K+",
        "logo": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01777-779944",
        "total_branches": 2,
        "branches": [
            {"branch_name": "Gulshan Avenue Flagship", "area": "Gulshan", "exact_address": "House 82, Road 11, Gulshan Avenue (Opposite South Breeze Square), Dhaka", "phone": "01777-779944", "opening_hours": "07:30 AM - 10:30 PM", "map_location": "Gulshan Avenue, Dhaka"},
            {"branch_name": "Dhanmondi Satmasjid Road", "area": "Dhanmondi", "exact_address": "Plot 43, Satmasjid Road (Near Road 8/A), Dhanmondi, Dhaka", "phone": "01777-779944", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Dhanmondi, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Artisanal Pastries & Viennoiserie",
                "items": [
                    {"name": "Traditional French Butter Croissant", "description": "Laminated 100% Normandy butter flaky croissant baked fresh morning and afternoon.", "price": 240, "currency": "BDT", "is_bestseller": True},
                    {"name": "Almond Frangipane Croissant", "description": "Twice baked butter croissant filled and topped with toasted almond cream.", "price": 320, "currency": "BDT", "is_bestseller": True},
                    {"name": "Pain au Chocolat", "description": "Crisp flaky pastry roll stuffed with two batons of Belgian dark chocolate.", "price": 280, "currency": "BDT", "is_bestseller": False},
                    {"name": "Wild Berry Danish", "description": "Vanilla bean custard pastry topped with fresh raspberries and blueberries.", "price": 310, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Woodfired Artisan Pizza & Gourmet Brunch",
                "items": [
                    {"name": "Classic Margherita Neapolitan (12 Inch)", "description": "San Marzano tomato base, fresh buffalo mozzarella, fresh basil, extra virgin olive oil.", "price": 950, "currency": "BDT", "is_bestseller": True},
                    {"name": "Truffle Prosciutto Crudo (12 Inch)", "description": "Woodfired crust with fior di latte, black truffle oil, beef prosciutto and arugula.", "price": 1450, "currency": "BDT", "is_bestseller": True},
                    {"name": "Avocado Tartine with Poached Eggs", "description": "Crusty country sourdough topped with smashed Hass avocado, feta cheese and organic eggs.", "price": 680, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    },

    # 4. CHATIME BANGLADESH
    {
        "id": "chatime-bangladesh",
        "name": "Chatime Bangladesh",
        "tagline": "World's Famous Taiwanese Bubble Tea & Fruit Tea Specialty",
        "cuisine": ["Bubble Tea", "Tea", "Specialty Coffee", "Desserts"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.6,
        "review_count": "11K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01755-667788",
        "total_branches": 4,
        "branches": [
            {"branch_name": "Banani Road 11", "area": "Banani", "exact_address": "Plot 54, Road 11, Block D, Banani, Dhaka", "phone": "01755-667788", "opening_hours": "11:00 AM - 11:30 PM", "map_location": "Banani, Dhaka"},
            {"branch_name": "Dhanmondi Satmasjid Road", "area": "Dhanmondi", "exact_address": "House 52/1, Road 3/A, Satmasjid Road, Dhanmondi, Dhaka", "phone": "01755-667788", "opening_hours": "11:00 AM - 11:30 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Uttara Sector 11", "area": "Uttara", "exact_address": "Gareeb-e-Nawaz Avenue, Sector 11, Uttara, Dhaka", "phone": "01755-667788", "opening_hours": "11:00 AM - 11:30 PM", "map_location": "Uttara, Dhaka"},
            {"branch_name": "Jamuna Future Park", "area": "Bashundhara", "exact_address": "Level 5, Food Zone, Jamuna Future Park, Kuril, Dhaka", "phone": "01755-667788", "opening_hours": "11:00 AM - 10:30 PM", "map_location": "Jamuna Future Park, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Signature Milk Tea & Pearls",
                "items": [
                    {"name": "Chatime Roasted Milk Tea with Pearls (L)", "description": "Rich roasted oolong tea infused with milk and fresh black tapioca pearls.", "price": 280, "currency": "BDT", "is_bestseller": True},
                    {"name": "Brown Sugar Pearl Fresh Milk (L)", "description": "Creamy farm fresh milk swirled with caramelized brown sugar syrup and warm boba.", "price": 310, "currency": "BDT", "is_bestseller": True},
                    {"name": "Taro Milk Tea with Coconut Jelly (L)", "description": "Creamy purple taro sweet milk tea with chewy coconut nata de coco.", "price": 290, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Refreshing Fruit Teas & Coolers",
                "items": [
                    {"name": "Mango Green Tea with Rainbow Jelly", "description": "Jasmine green tea shaken with real alphonso mango juice and popping jellies.", "price": 270, "currency": "BDT", "is_bestseller": True},
                    {"name": "Passion Fruit QQ (Pearls & Coconut Jelly)", "description": "Tangy passion fruit iced black tea loaded with boba and coconut jelly.", "price": 290, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 5. BEAUTY LASSI & FALUDA (CENTURY-OLD OLD DHAKA HERITAGE)
    {
        "id": "beauty-lassi-faluda",
        "name": "Beauty Lassi & Faluda (বিউটি লাচ্ছি)",
        "tagline": "Century-Old Heritage (Est. 1922) — Dhaka's Most Legendary Sweet Lassi, Faluda & Lemon Sherbet",
        "cuisine": ["Desserts", "Juices", "Old Dhaka Heritage"],
        "price_range": "৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.8,
        "review_count": "38K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01715-445566",
        "total_branches": 2,
        "branches": [
            {"branch_name": "Nazira Bazar Flagship (Est. 1922)", "area": "Old Dhaka", "exact_address": "30/A Johnson Road, Nazira Bazar, Old Dhaka 1100", "phone": "01715-445566", "opening_hours": "09:00 AM - 12:00 AM", "map_location": "Nazira Bazar, Dhaka"},
            {"branch_name": "Lalbagh Fort Road", "area": "Old Dhaka", "exact_address": "Near Lalbagh Fort Main Gate, Old Dhaka", "phone": "01715-445566", "opening_hours": "10:00 AM - 11:30 PM", "map_location": "Lalbagh, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Legendary Lassi & Sherbet",
                "items": [
                    {"name": "Beauty Special Sweet Lassi", "description": "Hand-churned rich curd lassi flavored with crushed ice, rose essence and sugar syrup.", "price": 60, "currency": "BDT", "is_bestseller": True},
                    {"name": "Beauty Special Malai Lassi", "description": "Signature yogurt lassi crowned with a thick golden layer of fresh clotted malai.", "price": 80, "currency": "BDT", "is_bestseller": True},
                    {"name": "Lebur Shorbot (Special Lemon Sherbet)", "description": "Refreshing chilled lemon cooler mixed with secret spiced syrup.", "price": 30, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Royal Faluda & Kulfi",
                "items": [
                    {"name": "Royal Special Faluda", "description": "Chilled sweetened milk, noodles, sabja seeds, jelly cubes, topped with rich malai kulfi and raisins.", "price": 120, "currency": "BDT", "is_bestseller": True},
                    {"name": "Pista Kulfi Malai (Matka)", "description": "Traditional slow-boiled dense milk kulfi loaded with pistachios and saffron.", "price": 70, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    },

    # 6. BISMILLAH KABAB GHOR (NAZIRA BAZAR)
    {
        "id": "bismillah-kabab-ghor",
        "name": "Bismillah Kabab Ghor (বিসমিল্লাহ কাবাব ঘর)",
        "tagline": "Old Dhaka's Holy Grail of Beef Boti, Khiri, Gurda, Chaap & Crispy Luchi",
        "cuisine": ["Kebabs", "Old Dhaka Heritage", "Mughlai", "Street Food"],
        "price_range": "৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.7,
        "review_count": "29K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01720-334455",
        "total_branches": 1,
        "branches": [
            {"branch_name": "Nazira Bazar Main", "area": "Old Dhaka", "exact_address": "Nazira Bazar Chowrasta, Kazi Alauddin Road, Old Dhaka", "phone": "01720-334455", "opening_hours": "04:30 PM - 02:00 AM", "map_location": "Nazira Bazar, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Charcoal Grilled Kebabs & Chaap",
                "items": [
                    {"name": "Special Beef Boti Kabab", "description": "Tenderized beef chunks marinated in mustard oil, raw papaya and roasted spices grilled on skewer.", "price": 140, "currency": "BDT", "is_bestseller": True},
                    {"name": "Special Beef Khiri Kabab", "description": "Old Dhaka's famous spicy charcoal grilled udder kebab.", "price": 150, "currency": "BDT", "is_bestseller": True},
                    {"name": "Beef Gurda Kabab (Kidney)", "description": "Charcoal grilled spiced kidney skewers.", "price": 140, "currency": "BDT", "is_bestseller": False},
                    {"name": "Beef Chaap (Tawa Fried)", "description": "Beaten beef slice shallow-fried on heavy iron tawa with crushed chilies and garam masala.", "price": 160, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chicken Chaap", "description": "Spiced chicken leg quarter shallow-fried until golden and crispy.", "price": 150, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Paratha & Luchi",
                "items": [
                    {"name": "Special Crispy Luchi (Per Pc)", "description": "Hot puffed flaky deep fried luchi paratha.", "price": 15, "currency": "BDT", "is_bestseller": True},
                    {"name": "Dhakaiya Butter Naan", "description": "Tandoor baked soft fluffy bread glazed with butter.", "price": 40, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 7. NANNA BIRYANI (BECHARAM DEURI)
    {
        "id": "nanna-biryani",
        "name": "Nanna Biryani (নান্না বিরিয়ানি)",
        "tagline": "The Undisputed King of Dhakaiya Shahi Morog Polao & Borhani",
        "cuisine": ["Biryani", "Old Dhaka Heritage", "Mughlai"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.6,
        "review_count": "32K+",
        "logo": "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01712-889900",
        "total_branches": 3,
        "branches": [
            {"branch_name": "Becharam Deuri (Original)", "area": "Old Dhaka", "exact_address": "42 Becharam Deuri, Chawkbazar, Old Dhaka", "phone": "01712-889900", "opening_hours": "11:00 AM - 11:30 PM", "map_location": "Chawkbazar, Dhaka"},
            {"branch_name": "Nazira Bazar Branch", "area": "Old Dhaka", "exact_address": "Kazi Alauddin Road, Nazira Bazar, Old Dhaka", "phone": "01712-889900", "opening_hours": "11:00 AM - 11:30 PM", "map_location": "Nazira Bazar, Dhaka"},
            {"branch_name": "Dhanmondi Satmasjid Road", "area": "Dhanmondi", "exact_address": "Satmasjid Road (Near Road 7/A), Dhanmondi, Dhaka", "phone": "01712-889900", "opening_hours": "12:00 PM - 11:00 PM", "map_location": "Dhanmondi, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Legendary Morog Polao & Kacchi",
                "items": [
                    {"name": "Nanna Shahi Morog Polao", "description": "Authentic fragrant chinigura rice cooked in ghee with whole tender spiced chicken quarter, egg and secret shahi gravy.", "price": 260, "currency": "BDT", "is_bestseller": True},
                    {"name": "Special Shahi Mutton Kacchi Biryani", "description": "Basmati rice layered with juicy mutton marinated in raw papaya and nutmeg ghee.", "price": 320, "currency": "BDT", "is_bestseller": True},
                    {"name": "Special Beef Tehari", "description": "Mustard oil cooked chinigura rice loaded with soft tender beef chunks and green chilies.", "price": 200, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Side Dishes & Traditional Borhani",
                "items": [
                    {"name": "Traditional Spicy Borhani (Glass)", "description": "Fresh curd blended with mustard, mint, roasted cumin and black salt.", "price": 50, "currency": "BDT", "is_bestseller": True},
                    {"name": "Shahi Chicken Jali Kabab", "description": "Egg-lace wrapped deep fried spiced minced chicken patty.", "price": 45, "currency": "BDT", "is_bestseller": True},
                    {"name": "Zarda with Mini Gulab Jamun", "description": "Sweet fragrant saffron rice topped with morobba, nuts and baby sweets.", "price": 70, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 8. AL RAZZAK RESTAURANT (BANGSHAL)
    {
        "id": "al-razzak-restaurant",
        "name": "Al Razzak Restaurant (আল রাজ্জাক)",
        "tagline": "Historic Dhakaiya Dining: Haji Glachee, Morog Polao, Beef Nehari & Mutton Kacchi",
        "cuisine": ["Biryani", "Old Dhaka Heritage", "Mughlai", "Bengali"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.6,
        "review_count": "27K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01711-556677",
        "total_branches": 1,
        "branches": [
            {"branch_name": "Bangshal Road Flagship", "area": "Old Dhaka", "exact_address": "29/1 Kazi Nazrul Islam Sarani / North South Road, Bangshal, Old Dhaka", "phone": "01711-556677", "opening_hours": "06:00 AM - 12:00 AM", "map_location": "Bangshal, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Signature Curries & Breakfast Nehari",
                "items": [
                    {"name": "Special Beef Nehari (With Bone Marrow)", "description": "Overnight slow-cooked rich bone marrow beef stew topped with ginger shreds and chilies.", "price": 220, "currency": "BDT", "is_bestseller": True},
                    {"name": "Signature Mutton Glachee", "description": "Old Dhaka's legendary thick spiced mutton curry cooked with bone marrow ghee.", "price": 280, "currency": "BDT", "is_bestseller": True},
                    {"name": "Special Mutton Brain Masala", "description": "Spiced pan-tossed tender goat brain fry.", "price": 240, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Biryani & Breads",
                "items": [
                    {"name": "Al Razzak Shahi Morog Polao", "description": "Signature whole chicken leg roast on fragrant saffron ghee rice.", "price": 270, "currency": "BDT", "is_bestseller": True},
                    {"name": "Special Mutton Kacchi Biryani", "description": "Basmati rice cooked in dum with succulent mutton and potato.", "price": 320, "currency": "BDT", "is_bestseller": True},
                    {"name": "Special Tandoori Butter Naan", "description": "Fluffy tandoor baked bread with pure cow ghee.", "price": 40, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 9. SHAD TEHARI GHOR (LALMATIA)
    {
        "id": "shad-tehari-ghor",
        "name": "Shad Tehari Ghor (স্বাদ তেহারী ঘর)",
        "tagline": "Dhanmondi & Lalmatia's Most Beloved Beef Tehari & Borhani",
        "cuisine": ["Biryani", "Old Dhaka Heritage", "Fast Food"],
        "price_range": "৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.6,
        "review_count": "21K+",
        "logo": "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01911-332211",
        "total_branches": 2,
        "branches": [
            {"branch_name": "Lalmatia Block C (Flagship)", "area": "Mohammadpur", "exact_address": "Plot 2/1, Block C, Lalmatia (Near Minabazar / Satmasjid Road), Dhaka", "phone": "01911-332211", "opening_hours": "11:30 AM - 11:30 PM", "map_location": "Lalmatia, Dhaka"},
            {"branch_name": "Dhanmondi 27", "area": "Dhanmondi", "exact_address": "Road 27 (Old), Dhanmondi, Dhaka", "phone": "01911-332211", "opening_hours": "12:00 PM - 11:00 PM", "map_location": "Dhanmondi, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Signature Beef Tehari",
                "items": [
                    {"name": "Special Beef Tehari (Full)", "description": "Aromatic chinigura rice cooked in pure mustard oil packed with tender boneless beef pieces and hot green chilies.", "price": 180, "currency": "BDT", "is_bestseller": True},
                    {"name": "Special Beef Tehari (Half)", "description": "Generous single portion authentic mustard beef tehari.", "price": 120, "currency": "BDT", "is_bestseller": True},
                    {"name": "Special Chicken Jali Kabab", "description": "Crispy egg lace coated minced chicken patty.", "price": 40, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Drinks & Desserts",
                "items": [
                    {"name": "Special Spiced Borhani (Bottle)", "description": "Rich savory yogurt drink with black salt, mint and coriander.", "price": 50, "currency": "BDT", "is_bestseller": True},
                    {"name": "Royal Shahi Phirni (Clay Pot)", "description": "Creamy slow-boiled rice pudding topped with almonds in a traditional clay cup.", "price": 50, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 10. GEORGE'S BISTRO & CAFE (UTTARA)
    {
        "id": "georges-cafe-uttara",
        "name": "George's Cafe & Bistro",
        "tagline": "Uttara's Most Famous Cozy Artisan Cafe, Burgers, Pasta & Cheesecake",
        "cuisine": ["Specialty Coffee", "Burgers", "Continental", "Desserts"],
        "price_range": "৳৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.6,
        "review_count": "13K+",
        "logo": "https://images.unsplash.com/photo-1554118811-1e0d58224f24?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01713-445588",
        "total_branches": 2,
        "branches": [
            {"branch_name": "Uttara Sector 11 (Flagship)", "area": "Uttara", "exact_address": "House 2, Road 2, Sector 11, Uttara, Dhaka", "phone": "01713-445588", "opening_hours": "11:00 AM - 11:00 PM", "map_location": "Uttara, Dhaka"},
            {"branch_name": "Uttara Sector 3 (Rabindra Sarani)", "area": "Uttara", "exact_address": "Rabindra Sarani, Sector 3, Uttara, Dhaka", "phone": "01713-445588", "opening_hours": "11:00 AM - 11:00 PM", "map_location": "Uttara, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Gourmet Burgers & Pasta",
                "items": [
                    {"name": "George's Classic Smash Cheeseburger", "description": "Double smashed beef patties, sharp cheddar cheese, caramelized onions and secret house sauce.", "price": 380, "currency": "BDT", "is_bestseller": True},
                    {"name": "Creamy Fettuccine Alfredo with Grilled Chicken", "description": "Tender fettuccine tossed in rich parmesan garlic cream sauce topped with charbroiled chicken.", "price": 520, "currency": "BDT", "is_bestseller": True},
                    {"name": "Spicy Cajun Chicken Tenders", "description": "Buttermilk marinated crisp tenders with honey mustard sauce.", "price": 340, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Specialty Coffee & Desserts",
                "items": [
                    {"name": "Spanish Latte (Iced)", "description": "Espresso poured over condensed milk and textured cold foam.", "price": 310, "currency": "BDT", "is_bestseller": True},
                    {"name": "New York Baked Cheesecake Slice", "description": "Classic dense creamy cheesecake with strawberry coulis.", "price": 380, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    },

    # 11. SUBWAY BANGLADESH
    {
        "id": "subway-bangladesh",
        "name": "Subway Bangladesh",
        "tagline": "World's Largest Fresh Submarine Sandwich & Salad Chain",
        "cuisine": ["Sandwiches", "Fast Food", "Healthy Food"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.5,
        "review_count": "15K+",
        "logo": "https://images.unsplash.com/photo-1509722747041-616f39b57569?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01819-223344",
        "total_branches": 2,
        "branches": [
            {"branch_name": "Gulshan 2 Circle", "area": "Gulshan", "exact_address": "Plot 15, Road 53, Gulshan 2, Dhaka 1212", "phone": "01819-223344", "opening_hours": "08:00 AM - 11:30 PM", "map_location": "Gulshan 2, Dhaka"},
            {"branch_name": "Banani Road 11", "area": "Banani", "exact_address": "House 45, Road 11, Block C, Banani, Dhaka", "phone": "01819-223344", "opening_hours": "08:00 AM - 11:30 PM", "map_location": "Banani, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Signature Subs (6-Inch / Footlong)",
                "items": [
                    {"name": "Chicken Teriyaki Sub (6-Inch)", "description": "Tender chicken strips glazed in sweet teriyaki sauce with fresh veggies on freshly baked bread.", "price": 420, "currency": "BDT", "is_bestseller": True},
                    {"name": "Italian B.M.T. Sub (6-Inch)", "description": "Slices of beef pepperoni, beef salami and smoked chicken with choice of crisp vegetables and dressings.", "price": 480, "currency": "BDT", "is_bestseller": True},
                    {"name": "Roasted Chicken Breast Sub (6-Inch)", "description": "Lean roasted tender chicken breast on wheat bread.", "price": 390, "currency": "BDT", "is_bestseller": False},
                    {"name": "Tuna & Mayo Sub (6-Inch)", "description": "Flaked light tuna blended with creamy mayonnaise.", "price": 440, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Fresh Baked Cookies & Drinks",
                "items": [
                    {"name": "Double Chocolate Chip Cookie", "description": "Soft freshly baked cookie loaded with cocoa and chocolate chips.", "price": 95, "currency": "BDT", "is_bestseller": True},
                    {"name": "Subway Fountain Drink Refill", "description": "Ice chilled fountain beverage.", "price": 70, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 12. BAR-B-Q TONIGHT DHAKA
    {
        "id": "bar-b-q-tonight",
        "name": "Bar-B-Q Tonight Dhaka",
        "tagline": "Karachi's Renowned Authentic Pakistani Barbecue, Handi & Mutton Chops",
        "cuisine": ["Kebabs", "Grill", "Mughlai", "Indian"],
        "price_range": "৳৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.5,
        "review_count": "17K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01711-889955",
        "total_branches": 2,
        "branches": [
            {"branch_name": "Dhanmondi Satmasjid Road", "area": "Dhanmondi", "exact_address": "House 54, Road 8/A, Satmasjid Road, Dhanmondi, Dhaka", "phone": "01711-889955", "opening_hours": "12:00 PM - 11:30 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Gulshan 1", "area": "Gulshan", "exact_address": "South Avenue Tower, Gulshan 1, Dhaka", "phone": "01711-889955", "opening_hours": "12:00 PM - 11:30 PM", "map_location": "Gulshan 1, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Pakistani Charcoal Grills & Kebabs",
                "items": [
                    {"name": "Signature Mutton Ribs (4 Pcs)", "description": "Succulent mutton ribs marinated in raw papaya and traditional spices grilled over open charcoal.", "price": 950, "currency": "BDT", "is_bestseller": True},
                    {"name": "Reshmi Chicken Kebab Skewer", "description": "Tender minced chicken blended with almond cream, cheese and mild spices.", "price": 540, "currency": "BDT", "is_bestseller": True},
                    {"name": "Beef Seekh Kebab (4 Pcs)", "description": "Spiced beef mince skewers with mint coriander chutney.", "price": 580, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Clay Pot Handi & Roghni Naan",
                "items": [
                    {"name": "Chicken Boneless Handi", "description": "Tender chicken cooked in rich cashew and tomato gravy in clay pot.", "price": 680, "currency": "BDT", "is_bestseller": True},
                    {"name": "Roghni Sesame Naan", "description": "Tandoor baked bread glazed with ghee and white sesame seeds.", "price": 75, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    },

    # 13. SBARRO BANGLADESH
    {
        "id": "sbarro-bangladesh",
        "name": "Sbarro Bangladesh",
        "tagline": "Authentic XL New York Style Pizza Slices, Stuffed Pizza & Pasta",
        "cuisine": ["Pizza", "Pasta", "Fast Food"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.4,
        "review_count": "10K+",
        "logo": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01700-708090",
        "total_branches": 3,
        "branches": [
            {"branch_name": "Gulshan 1 Circle", "area": "Gulshan", "exact_address": "Avenue Tower, Gulshan 1, Dhaka", "phone": "01700-708090", "opening_hours": "11:00 AM - 11:00 PM", "map_location": "Gulshan 1, Dhaka"},
            {"branch_name": "Bailey Road", "area": "Bailey Road", "exact_address": "Green Cozy Cottage, New Bailey Road, Dhaka", "phone": "01700-708090", "opening_hours": "11:00 AM - 11:00 PM", "map_location": "Bailey Road, Dhaka"},
            {"branch_name": "Dhanmondi Satmasjid Road", "area": "Dhanmondi", "exact_address": "Satmasjid Road (Near Road 11/A), Dhanmondi, Dhaka", "phone": "01700-708090", "opening_hours": "11:00 AM - 11:00 PM", "map_location": "Dhanmondi, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "NY Style XL Pizza Slices",
                "items": [
                    {"name": "XL NY Beef Pepperoni Slice", "description": "Giant folding New York slice loaded with beef pepperoni, mozzarella and tomato sauce.", "price": 280, "currency": "BDT", "is_bestseller": True},
                    {"name": "XL Four Cheese Slice", "description": "Generous blend of mozzarella, cheddar, parmesan and ricotta on crispy thin crust.", "price": 250, "currency": "BDT", "is_bestseller": True},
                    {"name": "Stuffed Meat Pizza Slice", "description": "Double crust pizza packed with minced meat, cheese and savory sauce.", "price": 340, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Pasta & Italian Sides",
                "items": [
                    {"name": "Baked Beef Ziti Pasta", "description": "Tubular pasta baked with minced beef bolognese and melted mozzarella crust.", "price": 420, "currency": "BDT", "is_bestseller": True},
                    {"name": "Garlic Breadsticks with Marinara (4 Pcs)", "description": "Warm buttery garlic sticks served with herb tomato dip.", "price": 160, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 14. PASTA STATE
    {
        "id": "pasta-state",
        "name": "Pasta State",
        "tagline": "Dhaka's Most Popular Budget Gourmet Pasta & Creamy Lasagna Bowls",
        "cuisine": ["Pasta", "Italian", "Fast Food"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.5,
        "review_count": "19K+",
        "logo": "https://images.unsplash.com/photo-1551183053-bf91a1d81141?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01711-001122",
        "total_branches": 4,
        "branches": [
            {"branch_name": "Banani Road 11", "area": "Banani", "exact_address": "Plot 78, Road 11, Block D, Banani, Dhaka", "phone": "01711-001122", "opening_hours": "12:00 PM - 11:00 PM", "map_location": "Banani, Dhaka"},
            {"branch_name": "Dhanmondi Satmasjid Road", "area": "Dhanmondi", "exact_address": "Green Akshay Plaza, Satmasjid Road, Dhanmondi, Dhaka", "phone": "01711-001122", "opening_hours": "12:00 PM - 11:00 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Mirpur 10", "area": "Mirpur", "exact_address": "Section 10 Circle (Near Fire Service), Mirpur, Dhaka", "phone": "01711-001122", "opening_hours": "12:00 PM - 11:00 PM", "map_location": "Mirpur 10, Dhaka"},
            {"branch_name": "Uttara Sector 11", "area": "Uttara", "exact_address": "Gareeb-e-Nawaz Avenue, Sector 11, Uttara, Dhaka", "phone": "01711-001122", "opening_hours": "12:00 PM - 11:00 PM", "map_location": "Uttara, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Signature Baked Pasta Bowls",
                "items": [
                    {"name": "Baked Chicken Alfredo Pasta", "description": "Penne pasta baked in thick creamy mushroom parmesan sauce with chicken chunks and mozzarella layer.", "price": 360, "currency": "BDT", "is_bestseller": True},
                    {"name": "Naga Fiesta Baked Beef Pasta", "description": "Fiery Sylheti naga chili infused bolognese pasta baked under molten cheese.", "price": 380, "currency": "BDT", "is_bestseller": True},
                    {"name": "Four Cheese Mac & Cheese", "description": "Macaroni coated with rich cheddar, gouda, mozzarella and parmesan sauce.", "price": 340, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Appetizers & Shakes",
                "items": [
                    {"name": "Cheesy Garlic Toast (4 Pcs)", "description": "Crunchy baguette slices brushed with garlic herb butter and melted mozzarella.", "price": 180, "currency": "BDT", "is_bestseller": False},
                    {"name": "Nutella Chocolate Shake", "description": "Rich blended milkshake made with Italian Nutella and dairy ice cream.", "price": 220, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    },

    # 15. MEZZAN HAILE AAIUN (CHITTAGONG MEZBANI IN DHAKA)
    {
        "id": "mezzan-haile-aaiun",
        "name": "Mezzan Haile Aaiun (মেজবান খাইলে আইয়ুন)",
        "tagline": "Dhaka's Most Authentic Chittagonian Mezbani Beef, Chonar Daal & Nola",
        "cuisine": ["Bengali", "Beef", "Curry", "Traditional"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.6,
        "review_count": "24K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01811-998877",
        "total_branches": 3,
        "branches": [
            {"branch_name": "Dhanmondi Satmasjid Road", "area": "Dhanmondi", "exact_address": "House 45, Road 9/A, Satmasjid Road, Dhanmondi, Dhaka", "phone": "01811-998877", "opening_hours": "11:30 AM - 11:00 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Mirpur 2 Stadium Road", "area": "Mirpur", "exact_address": "Near National Cricket Stadium Gate 2, Section 2, Mirpur, Dhaka", "phone": "01811-998877", "opening_hours": "11:30 AM - 11:00 PM", "map_location": "Mirpur 2, Dhaka"},
            {"branch_name": "Uttara Sector 3", "area": "Uttara", "exact_address": "Jashimuddin Avenue, Sector 3, Uttara, Dhaka", "phone": "01811-998877", "opening_hours": "11:30 AM - 11:00 PM", "map_location": "Uttara, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Authentic Chittagong Mezbani Specialties",
                "items": [
                    {"name": "Chittagonian Mezbani Beef Gosht", "description": "Authentic spicy beef curry slow-cooked with special Chittagong radhuni spices and mustard oil.", "price": 280, "currency": "BDT", "is_bestseller": True},
                    {"name": "Mezbani Chonar Daal with Beef", "description": "Bengal gram lentils cooked with beef fat, bone marrow and aromatic spices.", "price": 140, "currency": "BDT", "is_bestseller": True},
                    {"name": "Mezbani Nola (Beef Bone Marrow Stew)", "description": "Rich bone marrow stew served in traditional clay bowl.", "price": 320, "currency": "BDT", "is_bestseller": True},
                    {"name": "Kala Bhuna (Chittagong Style)", "description": "Tender beef pieces slow-caramelized in dark spices and fried onions.", "price": 340, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Rice & Desserts",
                "items": [
                    {"name": "Plain Aromatic White Rice (Per Plate)", "description": "Steamed fresh fragrant rice.", "price": 40, "currency": "BDT", "is_bestseller": False},
                    {"name": "Traditional Chittagong Firni", "description": "Slow-cooked saffron rice pudding.", "price": 60, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 16. SWISS BAKERY (BAILEY ROAD HERITAGE)
    {
        "id": "swiss-bakery-bailey-road",
        "name": "Swiss Bakery (সুইস বেকারি)",
        "tagline": "Bailey Road's Legendary 1980s Heritage Bakery — Hot Patties, Swiss Rolls & Cream Buns",
        "cuisine": ["Bakery", "Desserts", "Snacks"],
        "price_range": "৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.6,
        "review_count": "18K+",
        "logo": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "02-9334455",
        "total_branches": 2,
        "branches": [
            {"branch_name": "Bailey Road (Original)", "area": "Bailey Road", "exact_address": "8 New Bailey Road (Opposite Natyashala), Dhaka", "phone": "02-9334455", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Bailey Road, Dhaka"},
            {"branch_name": "Shantinagar", "area": "Bailey Road", "exact_address": "Shantinagar Chowrasta, Dhaka", "phone": "02-9334455", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Shantinagar, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Fresh Baked Savory Snacks",
                "items": [
                    {"name": "Swiss Special Chicken Patty", "description": "Flaky golden multi-layered puff pastry filled with spiced shredded chicken.", "price": 60, "currency": "BDT", "is_bestseller": True},
                    {"name": "Swiss Special Beef Patty", "description": "Crisp flaky pastry packed with seasoned minced beef filling.", "price": 65, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chicken Curry Puff", "description": "Curried chicken and peas encased in crisp puff crust.", "price": 55, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Cakes & Sweet Delights",
                "items": [
                    {"name": "Signature Chocolate Swiss Roll", "description": "Moist cocoa sponge rolled with creamy vanilla frosting.", "price": 85, "currency": "BDT", "is_bestseller": True},
                    {"name": "Traditional Cream Horn", "description": "Crispy cone pastry piped with light whipped cream.", "price": 50, "currency": "BDT", "is_bestseller": True},
                    {"name": "Fruit Pound Cake (Full)", "description": "Classic butter pound loaf with raisins and tutti-frutti.", "price": 240, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 17. TRADITION BD (KHILGAON FOOD STREET)
    {
        "id": "tradition-bd-khilgaon",
        "name": "Tradition BD (Khilgaon)",
        "tagline": "The Pioneer Rooftop Cafe of Khilgaon Food Street — Platters, Pasta & Chaap",
        "cuisine": ["Continental", "Fast Food", "Chinese", "Platters"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.5,
        "review_count": "15K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01720-112233",
        "total_branches": 1,
        "branches": [
            {"branch_name": "Khilgaon Taltola Rooftop", "area": "Khilgaon", "exact_address": "Holding 561/A, Shahid Baki Road, Taltola, Khilgaon, Dhaka", "phone": "01720-112233", "opening_hours": "12:00 PM - 11:30 PM", "map_location": "Khilgaon, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Popular Rice Platters",
                "items": [
                    {"name": "Tradition Special BBQ Chicken Platter", "description": "Egg fried rice served with glazed BBQ chicken quarter, sauteed vegetables and coleslaw.", "price": 320, "currency": "BDT", "is_bestseller": True},
                    {"name": "Crispy Crispy Prawn Platter", "description": "Fried rice with crispy golden tempura prawns and chili garlic sauce.", "price": 360, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Pasta & Street Bites",
                "items": [
                    {"name": "Oven Baked Naga Pasta", "description": "Spicy pasta with chicken, capsicum and melted cheddar cheese topping.", "price": 290, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chicken Chaap with Luchi (4 Pcs)", "description": "Traditional tawa fried chicken chaap served with puffed luchis.", "price": 220, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 18. BHORTA BHAAT GHOR (KAWRAN BAZAR / PANTHAPATH)
    {
        "id": "bhorta-bhaat-ghor",
        "name": "Bhorta Bhaat Ghor (ভর্তা ভাত ঘর)",
        "tagline": "30+ Varieties of Authentic Bengali Bhorta, Fresh Fish Curry & Steaming Rice",
        "cuisine": ["Bengali", "Traditional", "Fish Curry", "Bhorta"],
        "price_range": "৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.6,
        "review_count": "19K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01712-445566",
        "total_branches": 2,
        "branches": [
            {"branch_name": "Panthapath / Kawran Bazar", "area": "Panthapath", "exact_address": "Green Road, Opposite Square Hospital, Panthapath, Dhaka", "phone": "01712-445566", "opening_hours": "11:00 AM - 11:00 PM", "map_location": "Panthapath, Dhaka"},
            {"branch_name": "Dhanmondi Road 2", "area": "Dhanmondi", "exact_address": "Near City College, Dhanmondi 2, Dhaka", "phone": "01712-445566", "opening_hours": "11:30 AM - 10:30 PM", "map_location": "Dhanmondi, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Traditional Bengali Bhorta (Per Bowl)",
                "items": [
                    {"name": "Chitol Maacher Kofta Bhorta", "description": "Smoky mashed chitol fish with mustard oil and charred dry chili.", "price": 50, "currency": "BDT", "is_bestseller": True},
                    {"name": "Special Ilish Maach Bhorta", "description": "Boneless hilsa fish mashed with fried onions and green chilies.", "price": 60, "currency": "BDT", "is_bestseller": True},
                    {"name": "Sheem & Sorisha Bhorta", "description": "Boiled flat beans pounded with pungent black mustard paste.", "price": 30, "currency": "BDT", "is_bestseller": False},
                    {"name": "Begun Pora Bhorta", "description": "Clay charcoal roasted smoky eggplant mashed with onions and cold pressed mustard oil.", "price": 35, "currency": "BDT", "is_bestseller": True},
                    {"name": "Kalojeera Bhorta", "description": "Medicinal roasted black seed paste with garlic and green chili.", "price": 30, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Fresh River Fish Curries & Bhaat",
                "items": [
                    {"name": "Padma Ilish Bhaja (With Mustard Oil Gravy)", "description": "Thick round cut hilsa fish shallow fried in mustard oil.", "price": 280, "currency": "BDT", "is_bestseller": True},
                    {"name": "Rui Maach Dum Curry", "description": "Fresh rui fish steak in onion tomato cumin gravy.", "price": 180, "currency": "BDT", "is_bestseller": False},
                    {"name": "Deshi Shorisha Ilish", "description": "Hilsa cooked in rich mustard gravy.", "price": 300, "currency": "BDT", "is_bestseller": True},
                    {"name": "Bashmati Chal er Bhaat (Unlimited)", "description": "Steaming hot fragrant rice.", "price": 40, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    },

    # 19. PAPPAROTI BANGLADESH
    {
        "id": "papparoti-bangladesh",
        "name": "PappaRoti Bangladesh",
        "tagline": "The Father of All Buns — Warm Caramelized Coffee Coated Butter Buns",
        "cuisine": ["Bakery", "Specialty Coffee", "Desserts"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.6,
        "review_count": "11K+",
        "logo": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01733-445566",
        "total_branches": 2,
        "branches": [
            {"branch_name": "Gulshan 2", "area": "Gulshan", "exact_address": "House 10, Road 53, Gulshan 2, Dhaka", "phone": "01733-445566", "opening_hours": "09:00 AM - 11:30 PM", "map_location": "Gulshan 2, Dhaka"},
            {"branch_name": "Banani Road 11", "area": "Banani", "exact_address": "Plot 64, Road 11, Banani, Dhaka", "phone": "01733-445566", "opening_hours": "09:00 AM - 11:30 PM", "map_location": "Banani, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Signature Coffee Buns",
                "items": [
                    {"name": "Original PappaRoti Coffee Bun", "description": "Freshly baked warm bun with crispy coffee-caramel crust and molten salted butter core.", "price": 220, "currency": "BDT", "is_bestseller": True},
                    {"name": "PappaRoti Nutella Bun", "description": "Signature warm coffee bun smothered in rich Italian Nutella hazelnut spread.", "price": 290, "currency": "BDT", "is_bestseller": True},
                    {"name": "Lotus Biscoff Bun", "description": "Topped with warm Belgian Biscoff speculoos spread and biscuit crumbs.", "price": 320, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Beverages",
                "items": [
                    {"name": "Pappa Milk Tea (Karak Style)", "description": "Strong spiced evaporated milk tea.", "price": 140, "currency": "BDT", "is_bestseller": True},
                    {"name": "Iced Caramel Macchiato", "description": "Double espresso, cold milk and vanilla with caramel drizzle.", "price": 280, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 20. CHILI'S AMERICAN GRILL & BAR BANGLADESH
    {
        "id": "chilis-bangladesh",
        "name": "Chili's American Grill & Bar",
        "tagline": "World-Famous American Southwestern Ribs, Sizzling Fajitas & Big Mouth Burgers",
        "cuisine": ["American", "Steaks", "Burgers", "Mexican"],
        "price_range": "৳৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.6,
        "review_count": "12K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01788-112233",
        "total_branches": 1,
        "branches": [
            {"branch_name": "Gulshan 2 Flagship", "area": "Gulshan", "exact_address": "Gulshan Avenue, Road 57 (Near Gulshan 2 Circle), Dhaka 1212", "phone": "01788-112233", "opening_hours": "12:00 PM - 11:30 PM", "map_location": "Gulshan 2, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Sizzling Fajitas & Big Mouth Burgers",
                "items": [
                    {"name": "Sizzling Grilled Chicken Fajitas", "description": "Served on sizzling iron skillet with bell peppers, onions, warm flour tortillas, pico de gallo, cheese and sour cream.", "price": 950, "currency": "BDT", "is_bestseller": True},
                    {"name": "Oldtimer Big Mouth Burger with Cheese", "description": "Thick hand-crafted beef patty, cheddar cheese, pickles, lettuce, tomato and red onion on toasted brioche.", "price": 720, "currency": "BDT", "is_bestseller": True},
                    {"name": "Texas Cheese Fries", "description": "Crisp french fries smothered in melted colby jack cheese, beef bacon bits and jalapenos.", "price": 480, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Desserts & Mocktails",
                "items": [
                    {"name": "Molten Chocolate Lava Cake", "description": "Warm chocolate cake with molten core topped with vanilla ice cream and caramel drizzle.", "price": 490, "currency": "BDT", "is_bestseller": True},
                    {"name": "Presidente Classic Margarita (Non-Alcoholic)", "description": "Refreshing fresh lime, orange curacao syrup and agave nectar on ice.", "price": 310, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    }
]

added_count = 0
for r in new_restaurants:
    if r["id"] not in existing_ids:
        data.append(r)
        existing_ids.add(r["id"])
        added_count += 1

with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

with open(JS_FILE, "w", encoding="utf-8") as f:
    f.write("window.RESTAURANTS_DATA = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n")

print(f"Added {added_count} brand new iconic restaurants! Total: {len(data)}")
