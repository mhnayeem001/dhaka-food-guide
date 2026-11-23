import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants.json")
JS_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants_data.js")

with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

existing_ids = {r["id"] for r in data}

batch_3 = [
    # 1. FARMHOUSE BURGER
    {
        "id": "farmhouse-burger",
        "name": "Farmhouse Burger",
        "tagline": "Dhaka's Premier Gourmet Craft Burger House — Brioche Buns & Smashed Beef",
        "cuisine": ["Burgers", "American", "Fast Food"],
        "price_range": "৳৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.7,
        "review_count": "15K+",
        "logo": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01729-112233",
        "total_branches": 2,
        "branches": [
            {"branch_name": "Gulshan 2 Flagship", "area": "Gulshan", "exact_address": "House 14, Road 53, Gulshan 2, Dhaka 1212", "phone": "01729-112233", "opening_hours": "12:00 PM - 11:30 PM", "map_location": "Gulshan 2, Dhaka"},
            {"branch_name": "Banani Road 11", "area": "Banani", "exact_address": "Plot 74, Road 11, Banani, Dhaka", "phone": "01729-112233", "opening_hours": "12:00 PM - 11:30 PM", "map_location": "Banani, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Craft Gourmet Burgers",
                "items": [
                    {"name": "The Farmhouse Truffle Smasher", "description": "Double smashed beef patties, black truffle garlic mayo, aged cheddar and caramelized shallots on toasted butter brioche.", "price": 620, "currency": "BDT", "is_bestseller": True},
                    {"name": "Classic Bacon Cheeseburger", "description": "Prime beef patty, crispy beef bacon strips, sharp cheddar, dill pickles and signature house relish.", "price": 540, "currency": "BDT", "is_bestseller": True},
                    {"name": "Nashville Hot Fried Chicken Burger", "description": "Jumbo chicken thigh dipped in cayenne spiced oil, slaw and dill pickles.", "price": 480, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Sides & Thick Shakes",
                "items": [
                    {"name": "Truffle Parmesan Hand-cut Fries", "description": "Skin-on potatoes tossed with white truffle oil and grated aged parmesan.", "price": 280, "currency": "BDT", "is_bestseller": True},
                    {"name": "Salted Caramel Shake", "description": "Vanilla bean gelato blended with homemade sea salted caramel drizzle.", "price": 340, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 2. GONG CHA BANGLADESH
    {
        "id": "gong-cha-bangladesh",
        "name": "Gong Cha Bangladesh",
        "tagline": "World's Premium Royal Taiwanese Bubble Tea & Milk Foam Specialty",
        "cuisine": ["Bubble Tea", "Tea", "Specialty Coffee"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.6,
        "review_count": "10K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01711-445588",
        "total_branches": 2,
        "branches": [
            {"branch_name": "Banani Road 11", "area": "Banani", "exact_address": "House 52, Road 11, Block D, Banani, Dhaka", "phone": "01711-445588", "opening_hours": "11:00 AM - 11:30 PM", "map_location": "Banani, Dhaka"},
            {"branch_name": "Gulshan 1", "area": "Gulshan", "exact_address": "Navana Tower, Gulshan 1, Dhaka", "phone": "01711-445588", "opening_hours": "11:00 AM - 11:30 PM", "map_location": "Gulshan 1, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Signature Milk Foam & Pearl Teas",
                "items": [
                    {"name": "Gong Cha Signature Black Tea with Milk Foam", "description": "Fresh brewed Alishan black tea topped with thick salted savory creamy milk foam.", "price": 290, "currency": "BDT", "is_bestseller": True},
                    {"name": "Brown Sugar Oolong Milk Tea with Pearls", "description": "Caramelized brown sugar glaze, roasted oolong and slow-cooked chewy pearls.", "price": 320, "currency": "BDT", "is_bestseller": True},
                    {"name": "Mango Green Tea with Coconut Jelly", "description": "Crisp green tea shaken with sweet mango juice and chewy coconut jelly.", "price": 280, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 3. DECK 13 (UTTARA ROOFTOP PIRATE RESTAURANT)
    {
        "id": "deck-13-uttara",
        "name": "Deck 13 (Uttara)",
        "tagline": "Uttara's Iconic Pirate Ship Themed Rooftop Lounge, Sizzlers & Grills",
        "cuisine": ["Continental", "Steaks", "Chinese", "Platters"],
        "price_range": "৳৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.5,
        "review_count": "14K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01755-998877",
        "total_branches": 1,
        "branches": [
            {"branch_name": "Uttara Sector 13 Rooftop", "area": "Uttara", "exact_address": "Plot 13, Gausul Azam Avenue, Sector 13, Uttara, Dhaka", "phone": "01755-998877", "opening_hours": "12:00 PM - 11:30 PM", "map_location": "Uttara, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Captain's Sizzlers & Grills",
                "items": [
                    {"name": "Black Pearl Sizzling Beef Steak", "description": "Prime grilled beef steak served on hot iron sizzler with black pepper sauce and wedges.", "price": 790, "currency": "BDT", "is_bestseller": True},
                    {"name": "Pirate's BBQ Chicken Platter", "description": "Smoky charbroiled chicken, spicy fried rice, buttered vegetables and chili garlic dip.", "price": 420, "currency": "BDT", "is_bestseller": True},
                    {"name": "Crispy Prawn Tempura (6 Pcs)", "description": "Golden battered king prawns with sweet chili dip.", "price": 450, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 4. AL KADERIA RESTAURANT (RAMPURA)
    {
        "id": "al-kaderia-restaurant",
        "name": "Al Kaderia Restaurant (আল কাদেরিয়া)",
        "tagline": "Rampura & Banasree's Famous Heritage Shahi Kacchi, Morog Polao & Tawa Chaap",
        "cuisine": ["Biryani", "Bengali", "Mughlai", "Old Dhaka Heritage"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.5,
        "review_count": "23K+",
        "logo": "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01712-998877",
        "total_branches": 2,
        "branches": [
            {"branch_name": "Rampura DIT Road", "area": "Khilgaon", "exact_address": "456 DIT Road, Rampura (Near Rampura Bridge), Dhaka", "phone": "01712-998877", "opening_hours": "10:30 AM - 11:30 PM", "map_location": "Rampura, Dhaka"},
            {"branch_name": "Banasree Main Road", "area": "Khilgaon", "exact_address": "Block B, Main Road, Banasree, Dhaka", "phone": "01712-998877", "opening_hours": "11:00 AM - 11:00 PM", "map_location": "Banasree, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Shahi Biryani & Polao",
                "items": [
                    {"name": "Al Kaderia Special Mutton Kacchi", "description": "Long-grain basmati rice cooked in dum with marinated tender mutton and potato.", "price": 310, "currency": "BDT", "is_bestseller": True},
                    {"name": "Special Shahi Morog Polao", "description": "Fragrant chinigura rice with whole chicken leg roast and egg in rich shahi gravy.", "price": 250, "currency": "BDT", "is_bestseller": True},
                    {"name": "Beef Chaap with Luchi", "description": "Spicy beaten beef fried on iron tawa served with 2 crispy luchis.", "price": 170, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    },

    # 5. HANIF BIRYANI (NAZIRA BAZAR)
    {
        "id": "hanif-biryani",
        "name": "Hanif Biryani (হানিফ বিরিয়ানি)",
        "tagline": "Nazira Bazar's Legendary Mustard Oil Beef Tehari Landmark",
        "cuisine": ["Biryani", "Old Dhaka Heritage"],
        "price_range": "৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.6,
        "review_count": "26K+",
        "logo": "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01711-224466",
        "total_branches": 1,
        "branches": [
            {"branch_name": "Nazira Bazar Main", "area": "Old Dhaka", "exact_address": "30 Kazi Alauddin Road, Nazira Bazar, Old Dhaka", "phone": "01711-224466", "opening_hours": "11:00 AM - 12:30 AM", "map_location": "Nazira Bazar, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Legendary Tehari",
                "items": [
                    {"name": "Hanif Special Beef Tehari (Full)", "description": "Aromatic rice prepared with pure cold-pressed mustard oil, green chilies and generous soft beef cubes.", "price": 180, "currency": "BDT", "is_bestseller": True},
                    {"name": "Hanif Special Beef Tehari (Half)", "description": "Single portion authentic mustard beef tehari.", "price": 110, "currency": "BDT", "is_bestseller": True},
                    {"name": "Dhakaiya Shahi Borhani", "description": "Fresh spicy curd drink with black pepper and mint.", "price": 40, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    },

    # 6. GLAZED DONUTS
    {
        "id": "glazed-donuts-dhaka",
        "name": "Glazed Donuts & Coffee",
        "tagline": "Dhaka's Favorite Artisanal Melt-in-Mouth Glazed Donuts & Handcrafted Coffee",
        "cuisine": ["Desserts", "Bakery", "Specialty Coffee"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.6,
        "review_count": "16K+",
        "logo": "https://images.unsplash.com/photo-1527515862127-a4fc05baf7a5?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01700-112244",
        "total_branches": 3,
        "branches": [
            {"branch_name": "Gulshan 1", "area": "Gulshan", "exact_address": "House 1, Road 138, Gulshan 1, Dhaka", "phone": "01700-112244", "opening_hours": "09:00 AM - 11:30 PM", "map_location": "Gulshan 1, Dhaka"},
            {"branch_name": "Banani Road 11", "area": "Banani", "exact_address": "Plot 67, Road 11, Block D, Banani, Dhaka", "phone": "01700-112244", "opening_hours": "09:00 AM - 11:30 PM", "map_location": "Banani, Dhaka"},
            {"branch_name": "Dhanmondi Satmasjid Road", "area": "Dhanmondi", "exact_address": "Satmasjid Road (Near Road 8/A), Dhanmondi, Dhaka", "phone": "01700-112244", "opening_hours": "09:00 AM - 11:30 PM", "map_location": "Dhanmondi, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Artisanal Fresh Glazed Donuts",
                "items": [
                    {"name": "Classic Original Glazed Donut", "description": "Ultra-light yeast raised donut dipped in signature sweet sugar honey glaze.", "price": 140, "currency": "BDT", "is_bestseller": True},
                    {"name": "Nutella Chocolate Hazelnut Donut", "description": "Glazed ring coated in creamy Nutella and toasted hazelnut bits.", "price": 180, "currency": "BDT", "is_bestseller": True},
                    {"name": "Boston Cream Filled Donut", "description": "Custard filled donut topped with rich dark chocolate ganache.", "price": 180, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Handcrafted Coffee",
                "items": [
                    {"name": "Iced Vanilla Latte", "description": "Double shot espresso with cold milk and sweet Madagascar vanilla syrup.", "price": 280, "currency": "BDT", "is_bestseller": True},
                    {"name": "Americano", "description": "Rich espresso topped with hot water.", "price": 190, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 7. KASTURI HERITAGE (PURANA PALTAN)
    {
        "id": "kasturi-heritage-paltan",
        "name": "Kasturi Heritage (পুরানা পল্টন)",
        "tagline": "Dhaka's Most Historic Authentic Bengali Feast — Deshi Shorisha Ilish, Rui, Chitol & 20+ Bhortas",
        "cuisine": ["Bengali", "Fish Curry", "Traditional", "Bhorta"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.6,
        "review_count": "28K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "02-9562233",
        "total_branches": 2,
        "branches": [
            {"branch_name": "Purana Paltan (Historic)", "area": "Old Dhaka", "exact_address": "8 Purana Paltan Lane, Motijheel / Paltan, Dhaka", "phone": "02-9562233", "opening_hours": "11:30 AM - 10:30 PM", "map_location": "Purana Paltan, Dhaka"},
            {"branch_name": "Dhanmondi Satmasjid Road", "area": "Dhanmondi", "exact_address": "Road 8/A, Satmasjid Road, Dhanmondi, Dhaka", "phone": "02-9562233", "opening_hours": "12:00 PM - 10:30 PM", "map_location": "Dhanmondi, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Traditional Bengali Fish Curries",
                "items": [
                    {"name": "Deshi Shorisha Ilish (Pet / Gada)", "description": "Padma hilsa cooked in pungent mustard gravy with green chilies.", "price": 320, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chitol Maacher Muitha", "description": "Spiced chitol fish dumplings simmered in aromatic onion-ginger curry.", "price": 280, "currency": "BDT", "is_bestseller": True},
                    {"name": "Boal Maach Jhol", "description": "Freshwater boal fish curry with potatoes and cauliflower.", "price": 260, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Bhorta & Steamed Rice",
                "items": [
                    {"name": "Chingri Shutki Bhorta", "description": "Pounded sun-dried prawns with roasted garlic and spicy red chilies.", "price": 50, "currency": "BDT", "is_bestseller": True},
                    {"name": "Kalojeera Bhorta", "description": "Medicinal roasted black seed paste with garlic and mustard oil.", "price": 30, "currency": "BDT", "is_bestseller": False},
                    {"name": "Steamed White Rice (Kataribhog Chal)", "description": "Steaming bowl of fragrant fine rice.", "price": 40, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    },

    # 8. BHOOTER ADDA (KHILGAON TALTOLA)
    {
        "id": "bhooter-adda-khilgaon",
        "name": "Bhooter Adda (ভূতের আড্ডা)",
        "tagline": "Khilgaon's Signature Spooky Themed Rooftop Eatery — Sizzling Platters & Naga Burgers",
        "cuisine": ["Continental", "Fast Food", "Burgers", "Chinese"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.4,
        "review_count": "17K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01733-556677",
        "total_branches": 1,
        "branches": [
            {"branch_name": "Khilgaon Taltola", "area": "Khilgaon", "exact_address": "Shahid Baki Road, Taltola, Khilgaon, Dhaka", "phone": "01733-556677", "opening_hours": "12:00 PM - 11:30 PM", "map_location": "Khilgaon, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Spooky Platters & Sizzlers",
                "items": [
                    {"name": "Bhooter Sizzling Chicken Platter", "description": "BBQ chicken breast on hot sizzler iron with egg fried rice, wedges and spicy vegetable.", "price": 340, "currency": "BDT", "is_bestseller": True},
                    {"name": "Spooky Naga Beef Burger", "description": "Fiery beef patty loaded with real Sylheti naga chili paste and molten cheese.", "price": 260, "currency": "BDT", "is_bestseller": True},
                    {"name": "Oven Baked Cheese Pasta", "description": "Penne pasta baked with chicken chunks and mozzarella mantle.", "price": 280, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 9. CHITTAGONG BULL (GULSHAN / DHANMONDI)
    {
        "id": "chittagong-bull",
        "name": "Chittagong Bull (চিটাগাং বুল)",
        "tagline": "Authentic Chittagong Kala Bhuna, Mezbani Gosht & Akhni Biryani",
        "cuisine": ["Bengali", "Beef", "Curry", "Traditional"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.6,
        "review_count": "18K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01711-335577",
        "total_branches": 2,
        "branches": [
            {"branch_name": "Gulshan 1", "area": "Gulshan", "exact_address": "House 12, Road 138, Gulshan 1, Dhaka", "phone": "01711-335577", "opening_hours": "11:30 AM - 11:00 PM", "map_location": "Gulshan 1, Dhaka"},
            {"branch_name": "Dhanmondi Satmasjid Road", "area": "Dhanmondi", "exact_address": "Road 11/A, Satmasjid Road, Dhanmondi, Dhaka", "phone": "01711-335577", "opening_hours": "11:30 AM - 11:00 PM", "map_location": "Dhanmondi, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Signature Chittagong Beef Delights",
                "items": [
                    {"name": "Chittagonian Special Kala Bhuna", "description": "Authentic black beef curry cooked for hours with roasted spices and fried onions.", "price": 360, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chittagong Mezbani Gosht", "description": "Spicy beef curry prepared with special radhuni spice mix.", "price": 290, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chonar Daal with Bone Marrow", "description": "Bengal gram lentils simmered with beef bone marrow fat.", "price": 140, "currency": "BDT", "is_bestseller": True},
                    {"name": "Special Chittagong Akhni Biryani", "description": "Fragrant rice cooked with rich beef stock and tender meat pieces.", "price": 280, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 10. THE STAGE MUSIC CAFE (DHANMONDI)
    {
        "id": "the-stage-music-cafe",
        "name": "The Stage Music Cafe",
        "tagline": "Dhanmondi's Legendary Live Acoustic Music Hub, Juicy Burgers & Pastas",
        "cuisine": ["Burgers", "Pasta", "Continental", "Specialty Coffee"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.5,
        "review_count": "16K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01712-667788",
        "total_branches": 1,
        "branches": [
            {"branch_name": "Dhanmondi Road 4", "area": "Dhanmondi", "exact_address": "House 18, Road 4, Dhanmondi, Dhaka 1205", "phone": "01712-667788", "opening_hours": "12:00 PM - 11:30 PM", "map_location": "Dhanmondi, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Acoustic Stage Burgers & Pasta",
                "items": [
                    {"name": "The Stage Monster Beef Burger", "description": "Double grilled beef patty, double cheese, caramelized mushrooms and BBQ glaze.", "price": 380, "currency": "BDT", "is_bestseller": True},
                    {"name": "Creamy Fettuccine Carbonara", "description": "Fettuccine pasta in rich egg-parmesan cream sauce with smoked beef bits.", "price": 420, "currency": "BDT", "is_bestseller": True},
                    {"name": "Spicy Peri Peri Chicken Wings (6 Pcs)", "description": "Crispy fried wings tossed in hot African bird's eye chili sauce.", "price": 240, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 11. CAFE DARBAR (DHANMONDI / MIRPUR)
    {
        "id": "cafe-darbar",
        "name": "Cafe Darbar (ক্যাফে দরবার)",
        "tagline": "Traditional Deshi-Chinese Chowmein, Crispy Fried Chicken & Sizzling Platters",
        "cuisine": ["Chinese", "Continental", "Fast Food"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.4,
        "review_count": "13K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01711-778899",
        "total_branches": 2,
        "branches": [
            {"branch_name": "Dhanmondi Road 27", "area": "Dhanmondi", "exact_address": "House 27 (Old), Road 16 (New), Dhanmondi, Dhaka", "phone": "01711-778899", "opening_hours": "12:00 PM - 11:00 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Mirpur 1 Sony Cinema area", "area": "Mirpur", "exact_address": "Section 1, Near Sony Square, Mirpur, Dhaka", "phone": "01711-778899", "opening_hours": "12:00 PM - 11:00 PM", "map_location": "Mirpur 1, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Deshi Chinese Favorites",
                "items": [
                    {"name": "Special Mixed Chowmein", "description": "Wok tossed noodles with shredded chicken, prawns, egg and crunchy vegetables.", "price": 320, "currency": "BDT", "is_bestseller": True},
                    {"name": "Szechuan Chicken (Dry Chili)", "description": "Crispy chicken tossed in spicy garlic ginger soy glaze.", "price": 380, "currency": "BDT", "is_bestseller": True},
                    {"name": "Crispy Fried Chicken (4 Pcs)", "description": "Bangladeshi style deep-fried spiced chicken.", "price": 280, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 12. SHAWARMA STREET (MIRPUR / DHANMONDI)
    {
        "id": "shawarma-street-dhaka",
        "name": "Shawarma Street",
        "tagline": "Authentic Arabian Garlic Toum, Pickles & Rotisserie Spiced Chicken Shawarma",
        "cuisine": ["Sandwiches", "Fast Food", "Street Food"],
        "price_range": "৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.6,
        "review_count": "15K+",
        "logo": "https://images.unsplash.com/photo-1529006557810-274b9b2fc783?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01720-445566",
        "total_branches": 3,
        "branches": [
            {"branch_name": "Mirpur 2 Stadium Road", "area": "Mirpur", "exact_address": "Section 2, Mirpur Cricket Stadium Gate 2, Dhaka", "phone": "01720-445566", "opening_hours": "02:00 PM - 11:30 PM", "map_location": "Mirpur 2, Dhaka"},
            {"branch_name": "Dhanmondi Satmasjid Road", "area": "Dhanmondi", "exact_address": "Near Road 7/A, Satmasjid Road, Dhanmondi, Dhaka", "phone": "01720-445566", "opening_hours": "02:00 PM - 11:30 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Bailey Road", "area": "Bailey Road", "exact_address": "New Bailey Road, Dhaka", "phone": "01720-445566", "opening_hours": "02:00 PM - 11:30 PM", "map_location": "Bailey Road, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Authentic Arabian Shawarma Rolls",
                "items": [
                    {"name": "Arabian Chicken Shawarma (Large)", "description": "Thin khubz flatbread wrapped with marinated spit-roasted chicken, thick garlic toum, french fries and pickled gherkins.", "price": 160, "currency": "BDT", "is_bestseller": True},
                    {"name": "Cheese Loaded Chicken Shawarma", "description": "Rotisserie chicken with melted mozzarella and cheddar cheese sauce.", "price": 200, "currency": "BDT", "is_bestseller": True},
                    {"name": "Shawarma Rice Bowl", "description": "Spiced butter rice topped with sliced shawarma chicken and garlic sauce.", "price": 220, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 13. RABINDRA SAROBAR FUCHKA & CHOTPOTI (DHANMONDI LAKE HERITAGE)
    {
        "id": "rabindra-sarobar-fuchka",
        "name": "Rabindra Sarobar Fuchka & Chotpoti",
        "tagline": "Dhaka's #1 Most Famous Open-Air Lakeside Fuchka, Dahi Fuchka & Special Chotpoti",
        "cuisine": ["Street Food", "Old Dhaka Heritage", "Desserts"],
        "price_range": "৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.7,
        "review_count": "45K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01711-000000",
        "total_branches": 2,
        "branches": [
            {"branch_name": "Rabindra Sarobar Open-Air Amphitheatre", "area": "Dhanmondi", "exact_address": "Rabindra Sarobar, Dhanmondi Lake, Road 8/A, Dhaka 1209", "phone": "01711-000000", "opening_hours": "03:00 PM - 10:30 PM", "map_location": "Dhanmondi Lake, Dhaka"},
            {"branch_name": "Dhanmondi Road 32 Lake Bridge", "area": "Dhanmondi", "exact_address": "Road 32 Lake Walkway, Dhanmondi, Dhaka", "phone": "01711-000000", "opening_hours": "03:00 PM - 10:30 PM", "map_location": "Dhanmondi, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Lakeside Fuchka & Chotpoti",
                "items": [
                    {"name": "Special Tok Fuchka (10 Pcs)", "description": "Ultra crispy puffed puris stuffed with spicy mashed potato and chickpeas, topped with boiled egg shreds and tangy tamarind water.", "price": 80, "currency": "BDT", "is_bestseller": True},
                    {"name": "Creamy Dahi Fuchka (10 Pcs)", "description": "Stuffed puris drenched in sweet spiced yogurt, mint chutney, tamarind sauce and crunchy sev.", "price": 120, "currency": "BDT", "is_bestseller": True},
                    {"name": "Special Dimer Chotpoti (Plate)", "description": "Warm spiced yellow pea curry topped with crushed fuchka, grated hard-boiled egg and fresh green chilies.", "price": 80, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    },

    # 14. TIKKA TREAT (MOHAMMADPUR TOWN HALL)
    {
        "id": "tikka-treat-mohammadpur",
        "name": "Tikka Treat (Mohammadpur)",
        "tagline": "Mohammadpur Town Hall's Legendary Charcoal Chicken Tikka, Beef Chaap & Parata",
        "cuisine": ["Kebabs", "Fast Food", "Mughlai", "Street Food"],
        "price_range": "৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.5,
        "review_count": "18K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01715-667788",
        "total_branches": 1,
        "branches": [
            {"branch_name": "Town Hall Market", "area": "Mohammadpur", "exact_address": "Mohammadpur Town Hall Super Market, Dhaka", "phone": "01715-667788", "opening_hours": "04:00 PM - 01:00 AM", "map_location": "Mohammadpur, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Charcoal Tikkas & Chaap",
                "items": [
                    {"name": "Chicken Tikka (Quarter Leg)", "description": "Spiced chicken leg quarter charred over burning coal with mustard oil glaze.", "price": 140, "currency": "BDT", "is_bestseller": True},
                    {"name": "Beef Tawa Chaap", "description": "Tender beaten beef fillet fried with red chili spices on flat tawa.", "price": 150, "currency": "BDT", "is_bestseller": True},
                    {"name": "Special Crispy Paratha (Per Pc)", "description": "Multi-layer flaky fried paratha.", "price": 20, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    },

    # 15. CHUI JHAL EXPRESS (KHULNA STYLE BEEF IN DHAKA)
    {
        "id": "chui-jhal-express",
        "name": "Chui Jhal Express (চুইঝাল এক্সপ্রেস)",
        "tagline": "Khulna & Satkhira's Authentic Piper Chaba (Chui Jhal) Beef, Mutton & Steamed Rice",
        "cuisine": ["Bengali", "Beef", "Curry", "Traditional"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.6,
        "review_count": "20K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01718-223344",
        "total_branches": 2,
        "branches": [
            {"branch_name": "Dhanmondi Satmasjid Road", "area": "Dhanmondi", "exact_address": "Near Road 7/A, Satmasjid Road, Dhanmondi, Dhaka", "phone": "01718-223344", "opening_hours": "11:30 AM - 11:00 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Khilgaon Taltola", "area": "Khilgaon", "exact_address": "Shahid Baki Road, Khilgaon, Dhaka", "phone": "01718-223344", "opening_hours": "12:00 PM - 11:00 PM", "map_location": "Khilgaon, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Khulna Authentic Chui Jhal Curries",
                "items": [
                    {"name": "Special Chui Jhal Beef Gosht", "description": "Tender beef pieces slow-cooked with aromatic Piper Chaba (Chui Jhal) tree stems giving deep herbal heat.", "price": 290, "currency": "BDT", "is_bestseller": True},
                    {"name": "Special Chui Jhal Mutton Curry", "description": "Goat meat infused with authentic Satkhira chui jhal bark and whole garlic pods.", "price": 380, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chui Jhal Duck Curry (Hahsher Mangsho)", "description": "Country duck cooked in fiery chui jhal gravy.", "price": 320, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 16. THE PIT STOP RESTAURANT (UTTARA)
    {
        "id": "pit-stop-uttara",
        "name": "The Pit Stop Restaurant (Uttara)",
        "tagline": "Highway-Style Sizzlers, Continental Platters & Chinese Dining",
        "cuisine": ["Continental", "Chinese", "Steaks"],
        "price_range": "৳৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.4,
        "review_count": "11K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01711-123456",
        "total_branches": 1,
        "branches": [
            {"branch_name": "Uttara Sector 1 (Airport Road)", "area": "Uttara", "exact_address": "House 1, Road 1, Sector 1 (Beside Dhaka-Mymensingh Highway), Uttara, Dhaka", "phone": "01711-123456", "opening_hours": "11:00 AM - 11:30 PM", "map_location": "Uttara, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Highway Sizzlers & Platters",
                "items": [
                    {"name": "Pit Stop Special Beef Steak", "description": "Prime grilled beef steak served on sizzling platter with mashed potato and peppercorn gravy.", "price": 750, "currency": "BDT", "is_bestseller": True},
                    {"name": "Mixed Chowmein with Crispy Chicken", "description": "Stir-fried noodles with vegetable, chicken and golden fried chicken.", "price": 380, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 17. SUSHI SAMURAI (BANANI)
    {
        "id": "sushi-samurai-banani",
        "name": "Sushi Samurai",
        "tagline": "Banani's Authentic Japanese Sushi Boats, Ramen & Tempura",
        "cuisine": ["Japanese", "Sushi", "Ramen", "Pan-Asian"],
        "price_range": "৳৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.6,
        "review_count": "10K+",
        "logo": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1611143669185-af224c5e3252?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01726-554433",
        "total_branches": 1,
        "branches": [
            {"branch_name": "Banani Road 11", "area": "Banani", "exact_address": "Plot 78, Road 11, Block D, Banani, Dhaka", "phone": "01726-554433", "opening_hours": "12:00 PM - 11:00 PM", "map_location": "Banani, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Authentic Sushi & Ramen",
                "items": [
                    {"name": "Samurai Sushi Platter (12 Pcs)", "description": "Assorted fresh salmon nigiri, tuna nigiri and California roll.", "price": 1450, "currency": "BDT", "is_bestseller": True},
                    {"name": "Rich Chicken Paitan Ramen", "description": "Silky slow-boiled chicken broth, ramen noodles, soft ajitsuke tamago egg and nori.", "price": 680, "currency": "BDT", "is_bestseller": True},
                    {"name": "Crispy Prawn Tempura (4 Pcs)", "description": "Light airy Japanese batter fried king prawns.", "price": 490, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },

    # 18. BUNKA (GULSHAN 2 ROOFTOP)
    {
        "id": "bunka-pan-asian",
        "name": "Bunka Pan-Asian (Gulshan 2)",
        "tagline": "Upscale Rooftop Teppanyaki, Dim Sum & Pan-Asian Dining",
        "cuisine": ["Pan-Asian", "Japanese", "Dim Sum", "Fine Dining"],
        "price_range": "৳৳৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.7,
        "review_count": "9K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01713-221100",
        "total_branches": 1,
        "branches": [
            {"branch_name": "Gulshan 2 Rooftop", "area": "Gulshan", "exact_address": "House 1, Road 96, Gulshan 2, Dhaka 1212", "phone": "01713-221100", "opening_hours": "12:30 PM - 11:30 PM", "map_location": "Gulshan 2, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Teppanyaki & Dim Sum",
                "items": [
                    {"name": "Teppanyaki Black Angus Beef", "description": "Iron griddle grilled prime beef cubes with garlic soy glaze and fried garlic chips.", "price": 1850, "currency": "BDT", "is_bestseller": True},
                    {"name": "Truffle Prawn Har Gow (4 Pcs)", "description": "Translucent steamed dumplings stuffed with king prawns and black truffle oil.", "price": 620, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    },

    # 19. STAR KABAB (THATARI BAZAR - ORIGINAL CENTURY OLD FLAGSHIP)
    {
        "id": "star-kabab-thatari-bazar",
        "name": "Star Kabab (Thatari Bazar Heritage)",
        "tagline": "The Original Century Landmark of Star Kabab — Khasir Leg Roast, Nehari & Jali Kabab",
        "cuisine": ["Biryani", "Old Dhaka Heritage", "Mughlai", "Kebabs"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.7,
        "review_count": "42K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "02-7112345",
        "total_branches": 1,
        "branches": [
            {"branch_name": "Thatari Bazar Original", "area": "Old Dhaka", "exact_address": "45 Thatari Bazar Road, Nawabpur / Wari area, Old Dhaka", "phone": "02-7112345", "opening_hours": "06:00 AM - 12:00 AM", "map_location": "Thatari Bazar, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Historic Star Kabab Specialties",
                "items": [
                    {"name": "Khasir Leg Roast (Full Mutton Shahi Roast)", "description": "Whole tender mutton leg roasted in rich almond-poppy seed gravy served with polao.", "price": 550, "currency": "BDT", "is_bestseller": True},
                    {"name": "Special Beef Nehari (Bone Marrow)", "description": "Old Dhaka's famous morning bone marrow stew with ginger and green chilies.", "price": 180, "currency": "BDT", "is_bestseller": True},
                    {"name": "Star Special Mutton Kacchi Biryani", "description": "Dhakaiya style saffron scented mutton biryani.", "price": 300, "currency": "BDT", "is_bestseller": True},
                    {"name": "Special Chicken Jali Kabab", "description": "Minced chicken patty coated in fried egg net.", "price": 40, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    },

    # 20. MADHUR CANTEEN & DU CAMPUS HERITAGE
    {
        "id": "madhur-canteen-du",
        "name": "Madhur Canteen (মধুর ক্যান্টিন)",
        "tagline": "Century-Old Historic Landmark of Dhaka University — Famous Dudh Cha, Singara & Toast",
        "cuisine": ["Tea", "Snacks", "Old Dhaka Heritage"],
        "price_range": "৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.8,
        "review_count": "50K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01711-999999",
        "total_branches": 1,
        "branches": [
            {"branch_name": "Dhaka University Campus", "area": "Old Dhaka", "exact_address": "Beside Institute of Business Administration (IBA), Dhaka University, Dhaka 1000", "phone": "01711-999999", "opening_hours": "07:30 AM - 08:30 PM", "map_location": "Dhaka University, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Heritage Campus Snacks & Tea",
                "items": [
                    {"name": "Special Madhur Dudh Cha (Glass)", "description": "Classic boiled condensed milk tea.", "price": 15, "currency": "BDT", "is_bestseller": True},
                    {"name": "Classic Shingara (Per Pc)", "description": "Crispy fried pastry stuffed with spiced potatoes and peanuts.", "price": 10, "currency": "BDT", "is_bestseller": True},
                    {"name": "Butter Egg Toast", "description": "Pan toasted milk bread dipped in seasoned beaten egg with butter.", "price": 30, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    }
]

added_count = 0
for r in batch_3:
    if r["id"] not in existing_ids:
        data.append(r)
        existing_ids.add(r["id"])
        added_count += 1

with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

with open(JS_FILE, "w", encoding="utf-8") as f:
    f.write("window.RESTAURANTS_DATA = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n")

print(f"Added {added_count} batch-3 restaurants! Total restaurants: {len(data)}")
