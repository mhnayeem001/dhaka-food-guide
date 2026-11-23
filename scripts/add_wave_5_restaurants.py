import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants.json")
JS_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants_data.js")

with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

existing_ids = {r["id"] for r in data}

wave_5 = [
    # 1. HELVETIA BANGLADESH (PIONEER FRIED CHICKEN CHAIN)
    {
        "id": "helvetia-bangladesh",
        "name": "Helvetia Bangladesh",
        "tagline": "Pioneer of Crispy Broast Chicken, Burgers & Chicken Rolls in Dhaka (Est. 1996)",
        "cuisine": ["Fried Chicken", "Fast Food", "Burgers"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.5,
        "review_count": "22K+",
        "logo": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01711-443322",
        "total_branches": 5,
        "branches": [
            {"branch_name": "Dhanmondi Satmasjid Road", "area": "Dhanmondi", "exact_address": "House 54, Road 8/A, Satmasjid Road, Dhanmondi, Dhaka", "phone": "01711-443322", "opening_hours": "10:30 AM - 11:00 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Banani Road 11", "area": "Banani", "exact_address": "Plot 54, Road 11, Block D, Banani, Dhaka", "phone": "01711-443322", "opening_hours": "11:00 AM - 11:30 PM", "map_location": "Banani, Dhaka"},
            {"branch_name": "Uttara Sector 3", "area": "Uttara", "exact_address": "Rabindra Sarani, Sector 3, Uttara, Dhaka", "phone": "01711-443322", "opening_hours": "11:00 AM - 11:00 PM", "map_location": "Uttara, Dhaka"},
            {"branch_name": "Mirpur 10 Circle", "area": "Mirpur", "exact_address": "Section 10 Circle, Near Fire Service, Mirpur, Dhaka", "phone": "01711-443322", "opening_hours": "11:00 AM - 11:00 PM", "map_location": "Mirpur 10, Dhaka"},
            {"branch_name": "Bailey Road", "area": "Bailey Road", "exact_address": "New Bailey Road Commercial Area, Dhaka", "phone": "01711-443322", "opening_hours": "11:00 AM - 11:00 PM", "map_location": "Bailey Road, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Crispy Broast & Fried Chicken",
                "items": [
                    {"name": "Helvetia Crispy Broast Chicken (2 Pcs)", "description": "Classic seasoned crispy broast chicken pieces with secret herb coating.", "price": 240, "currency": "BDT", "is_bestseller": True},
                    {"name": "Helvetia Crispy Broast Chicken (4 Pcs)", "description": "4 pieces of crunchy deep-fried chicken with garlic dip.", "price": 460, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chicken Drumstick Basket (3 Pcs)", "description": "3 crispy seasoned fried drumsticks.", "price": 310, "currency": "BDT", "is_bestseller": False},
                    {"name": "Spicy Hot Wings (6 Pcs)", "description": "Crispy fried wings tossed in sweet and spicy chili sauce.", "price": 220, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Burgers, Rolls & Sides",
                "items": [
                    {"name": "Helvetia Classic Chicken Burger", "description": "Juicy chicken patty with mayonnaise and crisp lettuce on sesame bun.", "price": 190, "currency": "BDT", "is_bestseller": True},
                    {"name": "Helvetia Super Cheese Burger", "description": "Crispy chicken patty with double cheddar cheese slice.", "price": 230, "currency": "BDT", "is_bestseller": True},
                    {"name": "Spicy Chicken Roll", "description": "Crispy fried chicken strips wrapped in flaky paratha.", "price": 160, "currency": "BDT", "is_bestseller": True},
                    {"name": "French Fries (Large)", "description": "Golden salted fries.", "price": 130, "currency": "BDT", "is_bestseller": False},
                    {"name": "Coleslaw Salad", "description": "Sweet creamy cabbage slaw.", "price": 60, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 2. CAPTAIN'S WORLD (BAILEY ROAD & UTTERA HERITAGE)
    {
        "id": "captains-world",
        "name": "Captain's World",
        "tagline": "Legendary Fast Food Hub — Crispy Chicken, Fish & Chips, Burgers & Soft Serves",
        "cuisine": ["Fast Food", "Fried Chicken", "Burgers"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.5,
        "review_count": "20K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01713-334455",
        "total_branches": 3,
        "branches": [
            {"branch_name": "Bailey Road Flagship", "area": "Bailey Road", "exact_address": "8 New Bailey Road (Opposite Natyashala), Dhaka", "phone": "01713-334455", "opening_hours": "11:00 AM - 11:30 PM", "map_location": "Bailey Road, Dhaka"},
            {"branch_name": "Uttara Sector 3", "area": "Uttara", "exact_address": "Rabindra Sarani, Sector 3, Uttara, Dhaka", "phone": "01713-334455", "opening_hours": "11:00 AM - 11:30 PM", "map_location": "Uttara, Dhaka"},
            {"branch_name": "Dhanmondi Satmasjid Road", "area": "Dhanmondi", "exact_address": "Satmasjid Road (Near Road 27 Old), Dhanmondi, Dhaka", "phone": "01713-334455", "opening_hours": "11:00 AM - 11:30 PM", "map_location": "Dhanmondi, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Crispy Chicken & Fish",
                "items": [
                    {"name": "Captain's Crispy Chicken (2 Pcs)", "description": "Golden battered spiced chicken with crunchy crust.", "price": 230, "currency": "BDT", "is_bestseller": True},
                    {"name": "Captain's Fish & Chips", "description": "Crispy fried dory fish fillet served with french fries and tartar sauce.", "price": 380, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chicken Nuggets (6 Pcs)", "description": "Tender battered chicken nuggets with sweet & sour dip.", "price": 180, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Burgers & Sundaes",
                "items": [
                    {"name": "Captain's Supreme Beef Burger", "description": "Beef patty, cheese, pickles and captain's special sauce.", "price": 240, "currency": "BDT", "is_bestseller": True},
                    {"name": "Crispy Chicken Fillet Burger", "description": "Battered chicken breast with lettuce and mayo.", "price": 210, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chocolate Sundae Cup", "description": "Soft serve vanilla ice cream with warm chocolate fudge.", "price": 120, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    },

    # 3. SECOND CUP COFFEE COMPANY (CANADIAN CHAIN)
    {
        "id": "second-cup-coffee",
        "name": "Second Cup Coffee Company",
        "tagline": "Canada's Premium Specialty Coffee Brand — Handcrafted Espresso, Frappes & Bakery",
        "cuisine": ["Specialty Coffee", "Bakery", "Breakfast & Brunch", "Continental"],
        "price_range": "৳৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.7,
        "review_count": "16K+",
        "logo": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01730-889900",
        "total_branches": 3,
        "branches": [
            {"branch_name": "Banani Road 11", "area": "Banani", "exact_address": "Plot 54, Road 11, Block D, Banani, Dhaka", "phone": "01730-889900", "opening_hours": "08:00 AM - 12:00 AM", "map_location": "Banani, Dhaka"},
            {"branch_name": "Dhanmondi Road 27", "area": "Dhanmondi", "exact_address": "House 27 (Old), Road 16 (New), Dhanmondi, Dhaka", "phone": "01730-889900", "opening_hours": "08:00 AM - 11:30 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Uttara Sector 11", "area": "Uttara", "exact_address": "Gareeb-e-Nawaz Avenue, Sector 11, Uttara, Dhaka", "phone": "01730-889900", "opening_hours": "08:00 AM - 11:30 PM", "map_location": "Uttara, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Artisan Hot & Iced Coffees",
                "items": [
                    {"name": "Signature Caramel Corretto", "description": "Espresso with steamed milk, Madagascar vanilla and rich caramel drizzle.", "price": 340, "currency": "BDT", "is_bestseller": True},
                    {"name": "Vanilla Bean Latte", "description": "Double espresso pulled over vanilla infused steamed milk.", "price": 310, "currency": "BDT", "is_bestseller": True},
                    {"name": "Iced Spanish Latte", "description": "Espresso on ice with condensed milk and creamy cold foam.", "price": 350, "currency": "BDT", "is_bestseller": True},
                    {"name": "Maple Pecan Cold Brew", "description": "Slow steeped cold brew topped with Canadian maple foam and crushed pecans.", "price": 360, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Fresh Pastries & Gourmet Sandwiches",
                "items": [
                    {"name": "Artisanal Smoked Turkey & Cheese Panini", "description": "Grilled panini bread filled with smoked turkey, cheddar and honey mustard.", "price": 420, "currency": "BDT", "is_bestseller": True},
                    {"name": "Butter Almond Croissant", "description": "Twice baked flaky French pastry with almond cream.", "price": 260, "currency": "BDT", "is_bestseller": True},
                    {"name": "Blueberry Crumble Muffin", "description": "Freshly baked muffin bursting with blueberries.", "price": 190, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 4. XINXIAN CHINESE RESTAURANT (DHAKA MEGA CHAIN)
    {
        "id": "xinxian-chinese",
        "name": "Xinxian Chinese Restaurant",
        "tagline": "Dhaka's Favorite Deshi-Chinese Family Dining — Chowmein, Wonton & Sizzling Dishes",
        "cuisine": ["Chinese", "Pan-Asian", "Continental"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.5,
        "review_count": "25K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01711-554433",
        "total_branches": 4,
        "branches": [
            {"branch_name": "Dhanmondi Satmasjid Road", "area": "Dhanmondi", "exact_address": "Plot 54, Road 8/A, Satmasjid Road, Dhanmondi, Dhaka", "phone": "01711-554433", "opening_hours": "12:00 PM - 11:00 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Mirpur 10 Circle", "area": "Mirpur", "exact_address": "Section 10 Circle, Mirpur, Dhaka", "phone": "01711-554433", "opening_hours": "12:00 PM - 11:00 PM", "map_location": "Mirpur 10, Dhaka"},
            {"branch_name": "Uttara Sector 3", "area": "Uttara", "exact_address": "Rabindra Sarani, Sector 3, Uttara, Dhaka", "phone": "01711-554433", "opening_hours": "12:00 PM - 11:00 PM", "map_location": "Uttara, Dhaka"},
            {"branch_name": "Mohammadpur Tajmahal Road", "area": "Mohammadpur", "exact_address": "Tajmahal Road, Block C, Mohammadpur, Dhaka", "phone": "01711-554433", "opening_hours": "12:00 PM - 11:00 PM", "map_location": "Mohammadpur, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Soups & Appetizers",
                "items": [
                    {"name": "Xinxian Special Corn Soup", "description": "Thick chicken and sweet corn soup with egg ribbons.", "price": 220, "currency": "BDT", "is_bestseller": True},
                    {"name": "Authentic Thai Clear Soup", "description": "Lemongrass and galangal broth loaded with king prawns.", "price": 280, "currency": "BDT", "is_bestseller": True},
                    {"name": "Crispy Fried Wonton (6 Pcs)", "description": "Crisp fried parcels with minced chicken filling and sweet chili dip.", "price": 200, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Rice, Chowmein & Sizzling Mains",
                "items": [
                    {"name": "Xinxian Special Mixed Fried Rice", "description": "Fragrant wok rice with prawns, chicken and scrambled eggs.", "price": 310, "currency": "BDT", "is_bestseller": True},
                    {"name": "Szechuan Chicken Chowmein", "description": "Spicy stir-fried noodles with chicken, cabbage and chilies.", "price": 290, "currency": "BDT", "is_bestseller": True},
                    {"name": "Sizzling Beef with Black Pepper", "description": "Tender beef slices on hot iron plate with bell peppers.", "price": 480, "currency": "BDT", "is_bestseller": True},
                    {"name": "Szechuan Chili Chicken (Dry)", "description": "Crispy diced chicken tossed with dry red chilies and garlic glaze.", "price": 360, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    },

    # 5. PEYALA CAFE (GULSHAN & BANANI)
    {
        "id": "peyala-cafe",
        "name": "Peyala Cafe",
        "tagline": "Modern Deshi Wraps, Rice Bowls, Cha & Fusion Street Food",
        "cuisine": ["Fast Food", "Tea", "Specialty Coffee", "Sandwiches"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.6,
        "review_count": "18K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01711-667788",
        "total_branches": 4,
        "branches": [
            {"branch_name": "Gulshan 1", "area": "Gulshan", "exact_address": "Navana Tower, Gulshan 1, Dhaka", "phone": "01711-667788", "opening_hours": "08:30 AM - 11:00 PM", "map_location": "Gulshan 1, Dhaka"},
            {"branch_name": "Banani Road 11", "area": "Banani", "exact_address": "Plot 54, Road 11, Banani, Dhaka", "phone": "01711-667788", "opening_hours": "08:30 AM - 11:00 PM", "map_location": "Banani, Dhaka"},
            {"branch_name": "Karwan Bazar", "area": "Panthapath", "exact_address": "BDBL Bhaban, Kazi Nazrul Islam Avenue, Karwan Bazar, Dhaka", "phone": "01711-667788", "opening_hours": "08:30 AM - 09:30 PM", "map_location": "Karwan Bazar, Dhaka"},
            {"branch_name": "Dhanmondi Satmasjid Road", "area": "Dhanmondi", "exact_address": "Satmasjid Road (Near Road 8/A), Dhanmondi, Dhaka", "phone": "01711-667788", "opening_hours": "09:00 AM - 11:00 PM", "map_location": "Dhanmondi, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Signature Wraps & Roll Bowls",
                "items": [
                    {"name": "Chittagong Beef Kala Bhuna Wrap", "description": "Authentic spicy beef kala bhuna with onions and mustard sauce wrapped in flaky paratha.", "price": 280, "currency": "BDT", "is_bestseller": True},
                    {"name": "Butter Chicken Tikka Wrap", "description": "Tandoori chicken tikka cubes in rich butter makhani gravy wrapped in rumali.", "price": 260, "currency": "BDT", "is_bestseller": True},
                    {"name": "Spicy Naga Chicken Wrap", "description": "Fiery naga marinated chicken with crisp cucumber and garlic mayo.", "price": 250, "currency": "BDT", "is_bestseller": True},
                    {"name": "Kala Bhuna Rice Bowl", "description": "Spiced butter rice topped with beef kala bhuna, boiled egg and salad.", "price": 340, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Signature Cha & Specialty Drinks",
                "items": [
                    {"name": "Peyala Special Masala Cha", "description": "Rich slow boiled milk tea infused with cardamom, cinnamon and ginger.", "price": 60, "currency": "BDT", "is_bestseller": True},
                    {"name": "Zafrani Kesar Malai Cha", "description": "Royal saffron and clotted cream infused milk tea in clay cup.", "price": 90, "currency": "BDT", "is_bestseller": True},
                    {"name": "Iced Tamarind Cooler", "description": "Tangy sweet tamarind beverage with rock salt and crushed mint.", "price": 140, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 6. NANDO'S BANGLADESH (PERI-PERI CHICKEN)
    {
        "id": "nandos-bangladesh",
        "name": "Nando's Bangladesh",
        "tagline": "World's Famous Flame-Grilled Afro-Portuguese Peri-Peri Chicken",
        "cuisine": ["Fried Chicken", "Continental", "Burgers"],
        "price_range": "৳৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.6,
        "review_count": "19K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01711-776655",
        "total_branches": 2,
        "branches": [
            {"branch_name": "Gulshan 1 Circle", "area": "Gulshan", "exact_address": "House 1, Road 138, Gulshan 1, Dhaka 1212", "phone": "01711-776655", "opening_hours": "12:00 PM - 11:30 PM", "map_location": "Gulshan 1, Dhaka"},
            {"branch_name": "Dhanmondi Road 27", "area": "Dhanmondi", "exact_address": "House 27 (Old), Road 16 (New), Dhanmondi, Dhaka", "phone": "01711-776655", "opening_hours": "12:00 PM - 11:30 PM", "map_location": "Dhanmondi, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Flame-Grilled Peri-Peri Chicken",
                "items": [
                    {"name": "1/4 Peri-Peri Chicken (Leg / Breast)", "description": "Flame-grilled chicken quarter basted in choice of Lemon & Herb, Mild, Hot or Extra Hot Peri-Peri sauce.", "price": 490, "currency": "BDT", "is_bestseller": True},
                    {"name": "1/2 Peri-Peri Chicken", "description": "Half chicken marinated 24 hours and flame-grilled to perfection.", "price": 890, "currency": "BDT", "is_bestseller": True},
                    {"name": "Whole Peri-Peri Chicken", "description": "Whole flame-grilled chicken for sharing.", "price": 1650, "currency": "BDT", "is_bestseller": True},
                    {"name": "Peri-Peri Chicken Butterfly", "description": "Two chicken breasts joined together, flame-grilled with crispy skin.", "price": 750, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Peri Sides & Beverages",
                "items": [
                    {"name": "Peri-Peri Seasoned Chips (Fries)", "description": "Crispy potato chips dusted with zesty peri-peri salt.", "price": 190, "currency": "BDT", "is_bestseller": True},
                    {"name": "Spicy Rice", "description": "Fragrant rice with spicy peppers and herbs.", "price": 190, "currency": "BDT", "is_bestseller": True},
                    {"name": "Bottomless Soft Drink (Refillable)", "description": "Unlimited refills of Coca-Cola, Sprite or Fanta.", "price": 180, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    },

    # 7. BURGER LAB (GOURMET CRAFT BURGERS)
    {
        "id": "burger-lab",
        "name": "Burger Lab",
        "tagline": "Dhaka's Experimental Gourmet Smashed Burgers, Animal Fries & Shakes",
        "cuisine": ["Burgers", "Fast Food", "American"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.6,
        "review_count": "17K+",
        "logo": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01720-998877",
        "total_branches": 3,
        "branches": [
            {"branch_name": "Dhanmondi Satmasjid Road", "area": "Dhanmondi", "exact_address": "Plot 52/1, Road 3/A, Satmasjid Road, Dhanmondi, Dhaka", "phone": "01720-998877", "opening_hours": "12:00 PM - 11:30 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Banani Road 11", "area": "Banani", "exact_address": "Plot 78, Road 11, Banani, Dhaka", "phone": "01720-998877", "opening_hours": "12:00 PM - 11:30 PM", "map_location": "Banani, Dhaka"},
            {"branch_name": "Mirpur 2 Stadium Road", "area": "Mirpur", "exact_address": "Section 2, Near Cricket Stadium Gate 2, Mirpur, Dhaka", "phone": "01720-998877", "opening_hours": "12:00 PM - 11:00 PM", "map_location": "Mirpur 2, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Craft Smashed Burgers",
                "items": [
                    {"name": "Lab Formula Beef Smasher", "description": "Double smashed beef patties, cheddar cheese, secret lab sauce and caramelized onions.", "price": 360, "currency": "BDT", "is_bestseller": True},
                    {"name": "The Nuclear Naga Burger", "description": "Fiery naga chili glazed beef patty, jalapeños and pepper jack cheese.", "price": 340, "currency": "BDT", "is_bestseller": True},
                    {"name": "Crispy Buttermilk Chicken Burger", "description": "Crunchy golden fried chicken breast with slaw and honey mustard.", "price": 310, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Animal Fries & Shakes",
                "items": [
                    {"name": "Animal Style Loaded Fries", "description": "Crispy fries topped with minced beef, molten cheese sauce and caramelized onions.", "price": 260, "currency": "BDT", "is_bestseller": True},
                    {"name": "Nutella KitKat Milkshake", "description": "Rich blended gelato shake with crushed KitKat bars and Italian Nutella.", "price": 240, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    },

    # 8. SKY ROOM DINING (PANTHAPATH SKYLINE)
    {
        "id": "sky-room-dining",
        "name": "Sky Room Dining",
        "tagline": "Dhaka's Historic Skyline Rooftop Dining — Sizzlers, Steaks & Continental Cuisine",
        "cuisine": ["Continental", "Steaks", "Chinese"],
        "price_range": "৳৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.5,
        "review_count": "15K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "02-9134455",
        "total_branches": 1,
        "branches": [
            {"branch_name": "Panthapath Rooftop", "area": "Panthapath", "exact_address": "Indira Road / Panthapath Crossing, Sky Bhaban (Top Floor), Dhaka", "phone": "02-9134455", "opening_hours": "12:30 PM - 11:30 PM", "map_location": "Panthapath, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Skyline Sizzling Steaks",
                "items": [
                    {"name": "Sky Room Special Beef Sirloin Steak", "description": "Prime grilled sirloin steak served on sizzling iron platter with mushroom sauce and french fries.", "price": 820, "currency": "BDT", "is_bestseller": True},
                    {"name": "Sizzling Pepper Chicken Steak", "description": "Charbroiled chicken breast tossed in black pepper gravy with mashed potatoes.", "price": 620, "currency": "BDT", "is_bestseller": True},
                    {"name": "Mixed Fried Rice with Szechuan Chicken", "description": "Egg fried rice served with spicy Szechuan chicken pieces.", "price": 380, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 9. ALAUDDIN SWEETMEAT (EST. 1894 - 130 YEARS OLD DHAKA HERITAGE)
    {
        "id": "alauddin-sweetmeat",
        "name": "Alauddin Sweetmeat (আলাউদ্দিন সুইটমিট)",
        "tagline": "130-Year-Old Historic Landmark (Est. 1894) — Shahi Halwa, Chomchom & Rosogolla",
        "cuisine": ["Bakery", "Desserts", "Old Dhaka Heritage"],
        "price_range": "৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.8,
        "review_count": "36K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "02-7312345",
        "total_branches": 3,
        "branches": [
            {"branch_name": "Chawkbazar Original (Est. 1894)", "area": "Old Dhaka", "exact_address": "Chawkbazar Chowrasta, Old Dhaka 1211", "phone": "02-7312345", "opening_hours": "07:00 AM - 11:00 PM", "map_location": "Chawkbazar, Dhaka"},
            {"branch_name": "Chamelibag / Shantinagar", "area": "Bailey Road", "exact_address": "Chamelibag Main Road, Shantinagar, Dhaka", "phone": "02-7312345", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Shantinagar, Dhaka"},
            {"branch_name": "Dhanmondi Road 2", "area": "Dhanmondi", "exact_address": "Near City College, Dhanmondi 2, Dhaka", "phone": "02-7312345", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Dhanmondi, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Historic Royal Sweets (Per Kg / Pc)",
                "items": [
                    {"name": "Traditional Porabari Style Chomchom (1 Kg)", "description": "Caramelized brown outer skin with soft succulent chenna core drenched in thick syrup.", "price": 650, "currency": "BDT", "is_bestseller": True},
                    {"name": "Spongy Pure White Rosogolla (1 Kg)", "description": "Authentic fresh cow milk chenna balls in light cardamom syrup.", "price": 550, "currency": "BDT", "is_bestseller": True},
                    {"name": "Shahi Habshi Halwa (1 Kg)", "description": "Alauddin's world famous caramelized milk and wheat halwa studded with almonds and pistachios.", "price": 950, "currency": "BDT", "is_bestseller": True},
                    {"name": "Kacha Golla (1 Kg)", "description": "Soft fresh unboiled sweet chenna sandesh.", "price": 700, "currency": "BDT", "is_bestseller": False},
                    {"name": "Special Motichur Laddu (1 Kg)", "description": "Ghee fried tiny gram flour pearls bound in saffron syrup.", "price": 500, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Breakfast & Savoury Snacks",
                "items": [
                    {"name": "Dhakaiya Shahi Halwa Puri", "description": "Hot puffed puris served with fragrant semolina halwa.", "price": 40, "currency": "BDT", "is_bestseller": True},
                    {"name": "Special Dahi Vada (2 Pcs)", "description": "Lentil fritters soaked in spiced curd with tamarind and mint chutney.", "price": 80, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    },

    # 10. PASTA FASTA (DHANMONDI & BANANI)
    {
        "id": "pasta-fasta",
        "name": "Pasta Fasta",
        "tagline": "Quick Fast Gourmet Pasta Bowls, Creamy Lasagna & Garlic Loaves",
        "cuisine": ["Pasta", "Italian", "Fast Food"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.5,
        "review_count": "16K+",
        "logo": "https://images.unsplash.com/photo-1551183053-bf91a1d81141?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01711-220033",
        "total_branches": 3,
        "branches": [
            {"branch_name": "Dhanmondi Satmasjid Road", "area": "Dhanmondi", "exact_address": "Road 11/A, Satmasjid Road, Dhanmondi, Dhaka", "phone": "01711-220033", "opening_hours": "12:00 PM - 11:00 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Banani Road 11", "area": "Banani", "exact_address": "Plot 64, Road 11, Banani, Dhaka", "phone": "01711-220033", "opening_hours": "12:00 PM - 11:00 PM", "map_location": "Banani, Dhaka"},
            {"branch_name": "Mirpur 10", "area": "Mirpur", "exact_address": "Section 10 Circle, Mirpur, Dhaka", "phone": "01711-220033", "opening_hours": "12:00 PM - 11:00 PM", "map_location": "Mirpur 10, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Signature Baked Pasta Bowls",
                "items": [
                    {"name": "Baked Chicken Alfredo Bowl", "description": "Penne pasta baked in rich mushroom cream sauce with chicken chunks and mozzarella topping.", "price": 340, "currency": "BDT", "is_bestseller": True},
                    {"name": "Naga Fiery Baked Beef Pasta", "description": "Spicy minced beef bolognese pasta with fiery naga kick and molten cheese crust.", "price": 360, "currency": "BDT", "is_bestseller": True},
                    {"name": "Four Cheese Baked Macaroni", "description": "Macaroni pasta in cheddar, gouda, parmesan and mozzarella cheese sauce.", "price": 330, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Garlic Breads & Shakes",
                "items": [
                    {"name": "Cheesy Garlic Loaf", "description": "Toasted baguette with garlic butter and melted mozzarella.", "price": 170, "currency": "BDT", "is_bestseller": True},
                    {"name": "Cold Chocolate Hazelnut Shake", "description": "Blended chocolate shake with hazelnut syrup.", "price": 210, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    }
]

added_count = 0
for r in wave_5:
    if r["id"] not in existing_ids:
        data.append(r)
        existing_ids.add(r["id"])
        added_count += 1

with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

with open(JS_FILE, "w", encoding="utf-8") as f:
    f.write("window.RESTAURANTS_DATA = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n")

print(f"Added {added_count} brand-new landmark restaurants! Total restaurants: {len(data)}")
