import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants.json")
JS_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants_data.js")

with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

existing_ids = {r["id"] for r in data}

batch_4 = [
    # 1. DUNKIN' BANGLADESH
    {
        "id": "dunkin-bangladesh",
        "name": "Dunkin' Bangladesh",
        "tagline": "America's Favorite All-Day Coffee, Hot Brews, Iced Lattes & Classic Donuts",
        "cuisine": ["Desserts", "Bakery", "Specialty Coffee"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.6,
        "review_count": "14K+",
        "logo": "https://images.unsplash.com/photo-1527515862127-a4fc05baf7a5?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01711-889911",
        "total_branches": 2,
        "branches": [
            {"branch_name": "Gulshan 1", "area": "Gulshan", "exact_address": "House 1, Road 138, Gulshan 1, Dhaka", "phone": "01711-889911", "opening_hours": "08:00 AM - 11:30 PM", "map_location": "Gulshan 1, Dhaka"},
            {"branch_name": "Banani Road 11", "area": "Banani", "exact_address": "Road 11, Block D, Banani, Dhaka", "phone": "01711-889911", "opening_hours": "08:00 AM - 11:30 PM", "map_location": "Banani, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Signature Donuts",
                "items": [
                    {"name": "Boston Kreme Donut", "description": "Yeast-raised shell filled with Bavarian cream and topped with rich chocolate icing.", "price": 160, "currency": "BDT", "is_bestseller": True},
                    {"name": "Glazed Chocolate Cake Donut", "description": "Old-fashioned chocolate cake donut coated in sweet glaze.", "price": 150, "currency": "BDT", "is_bestseller": True},
                    {"name": "Strawberry Frosted with Sprinkles", "description": "Yeast ring frosted with sweet strawberry icing and rainbow sprinkles.", "price": 150, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Beverages & Cold Brew",
                "items": [
                    {"name": "Dunkin' Original Blend Iced Coffee", "description": "Double brewed signature Arabica coffee poured over ice.", "price": 240, "currency": "BDT", "is_bestseller": True},
                    {"name": "Caramel Iced Macchiato", "description": "Layered milk and espresso with buttery caramel syrup.", "price": 290, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    },

    # 2. PREGO AT THE WESTIN DHAKA
    {
        "id": "prego-the-westin",
        "name": "Prego (The Westin Dhaka)",
        "tagline": "Dhaka's 23rd Floor Skyline Italian Fine Dining — Hand-Rolled Pasta & Sourdough Pizza",
        "cuisine": ["Italian", "Fine Dining", "Pasta", "Pizza"],
        "price_range": "৳৳৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.8,
        "review_count": "8.5K+",
        "logo": "https://images.unsplash.com/photo-1551183053-bf91a1d81141?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "02-9891988",
        "total_branches": 1,
        "branches": [
            {"branch_name": "The Westin Gulshan 2 (Level 23)", "area": "Gulshan", "exact_address": "Main Gulshan Avenue, Plot 1, CWN(B), Gulshan 2, Dhaka 1212", "phone": "02-9891988", "opening_hours": "06:30 PM - 11:30 PM", "map_location": "Gulshan 2, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Handcrafted Artisanal Pasta",
                "items": [
                    {"name": "Handmade Tagliatelle al Tartufo", "description": "Fresh egg pasta tossed with winter black truffle paste, butter and 24-month aged Parmigiano Reggiano.", "price": 1850, "currency": "BDT", "is_bestseller": True},
                    {"name": "Lobster & Crab Ravioli", "description": "Stuffed pasta pillows in a saffron shellfish bisque with cherry tomatoes.", "price": 2200, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Woodfired Pizza & Dolci",
                "items": [
                    {"name": "Prego Signature Pizza Quattro Formaggi", "description": "Gorgonzola, mozzarella, taleggio and parmesan with drizzle of honey.", "price": 1650, "currency": "BDT", "is_bestseller": True},
                    {"name": "Traditional Venetian Tiramisu", "description": "Savoiardi ladyfingers soaked in espresso and layered with mascarpone cream.", "price": 750, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    },

    # 3. LATEST RECIPE (LE MÉRIDIEN DHAKA)
    {
        "id": "latest-recipe-le-meridien",
        "name": "Latest Recipe (Le Méridien Dhaka)",
        "tagline": "5-Star Global Culinary Theater Buffet — Live Woks, Sushi, French Pastries & Roasts",
        "cuisine": ["Continental", "Fine Dining", "Pan-Asian", "Buffet"],
        "price_range": "৳৳৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.8,
        "review_count": "11K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "02-8900089",
        "total_branches": 1,
        "branches": [
            {"branch_name": "Airport Road (Level 15)", "area": "Uttara", "exact_address": "79/A Commercial Area, Airport Road, Nikunjo 2 / Uttara, Dhaka", "phone": "02-8900089", "opening_hours": "06:30 AM - 11:30 PM", "map_location": "Airport Road, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Global Grand Buffet & Live Stations",
                "items": [
                    {"name": "Grand International Dinner Buffet (Per Person)", "description": "Over 120 global delicacies: live teppanyaki, carved Australian roast beef, dim sums, Mediterranean grills and French dessert salon.", "price": 5500, "currency": "BDT", "is_bestseller": True},
                    {"name": "Seafood Gala Weekend Lunch (Per Person)", "description": "Unlimited jumbo king prawns, crab thermidor, fresh sushi, sashimi and river hilsa.", "price": 4800, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    },

    # 4. THE CHOCOLATE ROOM (BANANI / UTTARA)
    {
        "id": "the-chocolate-room-dhaka",
        "name": "The Chocolate Room",
        "tagline": "Dhaka's Heaven for Chocolate Lovers — Belgian Fondues, Sizzling Brownies & Sundaes",
        "cuisine": ["Desserts", "Specialty Coffee", "Fast Food"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.5,
        "review_count": "13K+",
        "logo": "https://images.unsplash.com/photo-1511381939415-e44015466834?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01730-112233",
        "total_branches": 2,
        "branches": [
            {"branch_name": "Banani Road 11", "area": "Banani", "exact_address": "Plot 54, Road 11, Block D, Banani, Dhaka", "phone": "01730-112233", "opening_hours": "12:00 PM - 11:30 PM", "map_location": "Banani, Dhaka"},
            {"branch_name": "Uttara Sector 7", "area": "Uttara", "exact_address": "Rabindra Sarani, Sector 7, Uttara, Dhaka", "phone": "01730-112233", "opening_hours": "12:00 PM - 11:30 PM", "map_location": "Uttara, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Signature Chocolate Decadence",
                "items": [
                    {"name": "Sizzling Chocolate Brownie with Vanilla Ice Cream", "description": "Fudgy warm chocolate brownie served on sizzling hot plate drenched in melted Belgian dark chocolate sauce.", "price": 380, "currency": "BDT", "is_bestseller": True},
                    {"name": "Belgian Chocolate Fondue for Two", "description": "Pot of warm melted chocolate served with fresh strawberries, banana slices, brownie bites and marshmallows.", "price": 650, "currency": "BDT", "is_bestseller": True},
                    {"name": "Death by Chocolate Sundae", "description": "Layered chocolate gelato, brownie chunks, chocolate chips and hot fudge.", "price": 360, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 5. NIROB HOTEL (NAZIRA BAZAR HERITAGE)
    {
        "id": "nirob-hotel-nazira-bazar",
        "name": "Nirob Hotel & Restaurant (নীরব হোটেল)",
        "tagline": "Century Landmark of Old Dhaka — 30+ Traditional Bhortas, Rui Fish & Duck Bhuna",
        "cuisine": ["Bengali", "Old Dhaka Heritage", "Fish Curry", "Bhorta"],
        "price_range": "৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.7,
        "review_count": "34K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01712-113355",
        "total_branches": 1,
        "branches": [
            {"branch_name": "Nazira Bazar Chowrasta", "area": "Old Dhaka", "exact_address": "113/2 Nazira Bazar, Kazi Alauddin Road, Old Dhaka", "phone": "01712-113355", "opening_hours": "07:00 AM - 12:00 AM", "map_location": "Nazira Bazar, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Old Dhaka's Famous 30+ Bhortas",
                "items": [
                    {"name": "Ilish Maacher Dim Bhorta", "description": "Smoky mashed hilsa fish roe with roasted red chilies and mustard oil.", "price": 70, "currency": "BDT", "is_bestseller": True},
                    {"name": "Morog Bhorta (Shredded Chicken)", "description": "Hand shredded chicken mixed with fried onions, ginger and mustard oil.", "price": 60, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chepa Shutki Bhorta", "description": "Traditional pungent semi-fermented shutki paste with garlic and fiery chili.", "price": 40, "currency": "BDT", "is_bestseller": True},
                    {"name": "Badam Bhorta (Almond & Peanut)", "description": "Rich pounded roasted peanut and almond mash.", "price": 40, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Curries & Rice",
                "items": [
                    {"name": "Deshi Duck Bhuna (Hahsher Mangsho)", "description": "Slow cooked country duck curry with whole garlic cloves and black pepper.", "price": 280, "currency": "BDT", "is_bestseller": True},
                    {"name": "Kataribhog Chal er Bhaat (Unlimited)", "description": "Steaming hot fragrant rice.", "price": 35, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    },

    # 6. KOLKATA KACCHI GHOR (BAILEY ROAD & OLD DHAKA)
    {
        "id": "kolkata-kacchi-ghor-dhaka",
        "name": "Kolkata Kacchi Ghor",
        "tagline": "Authentic Kolkata Style Light Saffron Kacchi with Jumbo Potato & Tender Mutton",
        "cuisine": ["Biryani", "Old Dhaka Heritage", "Mughlai"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.5,
        "review_count": "19K+",
        "logo": "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01711-665544",
        "total_branches": 2,
        "branches": [
            {"branch_name": "Bailey Road", "area": "Bailey Road", "exact_address": "New Bailey Road (Opposite Baily Square), Dhaka", "phone": "01711-665544", "opening_hours": "11:30 AM - 11:00 PM", "map_location": "Bailey Road, Dhaka"},
            {"branch_name": "Old Dhaka Wari", "area": "Old Dhaka", "exact_address": "Rankin Street, Wari, Dhaka", "phone": "01711-665544", "opening_hours": "11:30 AM - 11:00 PM", "map_location": "Wari, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Kolkata Style Awadhi Biryani",
                "items": [
                    {"name": "Kolkata Special Mutton Biryani", "description": "Fragrant long grain basmati rice lightly scented with rose water and saffron, containing melt-in-mouth mutton and whole fried golden potato.", "price": 340, "currency": "BDT", "is_bestseller": True},
                    {"name": "Special Chicken Chaap", "description": "Slow cooked chicken leg in rich poppy seed, cashew and melon seed Mughlai paste.", "price": 220, "currency": "BDT", "is_bestseller": True},
                    {"name": "Spiced Cucumber Raita", "description": "Cooling curd with roasted cumin and diced cucumber.", "price": 40, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 7. CHILI HOT POT DHAKA
    {
        "id": "chili-hot-pot-dhaka",
        "name": "Chili Hot Pot & Chinese",
        "tagline": "Authentic Sichuan Spicy Hot Pot, Broths & Handcrafted Dumplings",
        "cuisine": ["Chinese", "Pan-Asian", "Continental"],
        "price_range": "৳৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.5,
        "review_count": "10K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01715-990011",
        "total_branches": 2,
        "branches": [
            {"branch_name": "Banani Road 11", "area": "Banani", "exact_address": "Plot 54, Road 11, Banani, Dhaka", "phone": "01715-990011", "opening_hours": "12:00 PM - 11:30 PM", "map_location": "Banani, Dhaka"},
            {"branch_name": "Dhanmondi Satmasjid Road", "area": "Dhanmondi", "exact_address": "Road 8/A, Satmasjid Road, Dhanmondi, Dhaka", "phone": "01715-990011", "opening_hours": "12:00 PM - 11:30 PM", "map_location": "Dhanmondi, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Sichuan Hot Pot & Broths",
                "items": [
                    {"name": "Twin Flavour Hot Pot Broth (Spicy Mala & Herbal Chicken)", "description": "Split pot with tongue-numbing Sichuan mala pepper broth on one side and collagen chicken broth on the other.", "price": 750, "currency": "BDT", "is_bestseller": True},
                    {"name": "Thin Sliced Beef Ribeye (For Hot Pot)", "description": "Paper thin rolled beef ribeye slices that cook in 10 seconds.", "price": 550, "currency": "BDT", "is_bestseller": True},
                    {"name": "Handmade Pork/Chicken Dumplings (8 Pcs)", "description": "Steamed dumplings ready to dip into hot broth.", "price": 420, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 8. PASTAO EXPRESS (MIRPUR & DHANMONDI)
    {
        "id": "pastao-express",
        "name": "Pastao Express",
        "tagline": "Budget Friendly Oven-Baked Pasta Bowls, Cheesy Garlic Loaf & Shakes",
        "cuisine": ["Pasta", "Italian", "Fast Food"],
        "price_range": "৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.4,
        "review_count": "12K+",
        "logo": "https://images.unsplash.com/photo-1551183053-bf91a1d81141?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01719-887766",
        "total_branches": 2,
        "branches": [
            {"branch_name": "Mirpur 10 Circle", "area": "Mirpur", "exact_address": "Near Mirpur 10 Roundabout, Section 10, Dhaka", "phone": "01719-887766", "opening_hours": "12:00 PM - 11:00 PM", "map_location": "Mirpur 10, Dhaka"},
            {"branch_name": "Dhanmondi Shankar", "area": "Dhanmondi", "exact_address": "Near Shankar Bus Stand, Dhanmondi, Dhaka", "phone": "01719-887766", "opening_hours": "12:00 PM - 11:00 PM", "map_location": "Dhanmondi, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Oven Baked Pastas",
                "items": [
                    {"name": "Pastao Signature Cheese Bomb Pasta", "description": "Penne pasta enveloped in molten cheese sauce with juicy chicken and capsicum.", "price": 280, "currency": "BDT", "is_bestseller": True},
                    {"name": "Spicy Naga Chicken Pasta", "description": "Loaded with fresh Sylheti naga chili pepper kick and cheese crust.", "price": 260, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    }
]

added_count = 0
for r in batch_4:
    if r["id"] not in existing_ids:
        data.append(r)
        existing_ids.add(r["id"])
        added_count += 1

with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

with open(JS_FILE, "w", encoding="utf-8") as f:
    f.write("window.RESTAURANTS_DATA = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n")

print(f"Added {added_count} batch-4 restaurants! Total restaurants: {len(data)}")
