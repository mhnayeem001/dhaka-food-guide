import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants.json")

with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

# Existing IDs
existing_ids = {r["id"] for r in data}

new_restaurants = [
    {
        "id": "kacchi-bhai",
        "name": "Kacchi Bhai",
        "tagline": "Pure Basmati & Traditional Dhakaiya Kacchi",
        "cuisine": ["Biryani", "Kacchi", "Traditional", "Desi"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.7,
        "review_count": "38K+",
        "logo": "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1589302168068-964664d93dc0?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01788-990011",
        "total_branches": 12,
        "branches": [
            {
                "branch_name": "Dhanmondi Branch",
                "area": "Dhanmondi",
                "exact_address": "House 49, Road 9/A, Satmasjid Road, Dhanmondi, Dhaka",
                "phone": "01788-990011",
                "opening_hours": "12:00 PM - 11:00 PM",
                "map_location": "Dhanmondi, Dhaka"
            },
            {
                "branch_name": "Banani 11",
                "area": "Banani",
                "exact_address": "House 104, Road 11, Block C, Banani, Dhaka",
                "phone": "01788-990011",
                "opening_hours": "12:00 PM - 11:00 PM",
                "map_location": "Banani, Dhaka"
            },
            {
                "branch_name": "Gulshan 1",
                "area": "Gulshan",
                "exact_address": "Circle 1, Road 134, Gulshan 1, Dhaka",
                "phone": "01788-990011",
                "opening_hours": "12:00 PM - 11:00 PM",
                "map_location": "Gulshan 1, Dhaka"
            },
            {
                "branch_name": "Uttara Sector 7",
                "area": "Uttara",
                "exact_address": "Plot 1, Road 1, Sector 7, Jashimuddin Avenue, Uttara, Dhaka",
                "phone": "01788-990011",
                "opening_hours": "12:00 PM - 11:00 PM",
                "map_location": "Uttara, Dhaka"
            },
            {
                "branch_name": "Mirpur 10 Circle",
                "area": "Mirpur",
                "exact_address": "Section 10, Mirpur Roundabout, Dhaka",
                "phone": "01788-990011",
                "opening_hours": "12:00 PM - 11:00 PM",
                "map_location": "Mirpur 10, Dhaka"
            },
            {
                "branch_name": "Bailey Road",
                "area": "Bailey Road",
                "exact_address": "Bailey Fiesta, New Bailey Road, Dhaka",
                "phone": "01788-990011",
                "opening_hours": "12:00 PM - 11:00 PM",
                "map_location": "Bailey Road, Dhaka"
            },
            {
                "branch_name": "Bashundhara R/A",
                "area": "Bashundhara",
                "exact_address": "Main Gate, Road 1, Bashundhara R/A, Dhaka",
                "phone": "01788-990011",
                "opening_hours": "12:00 PM - 11:00 PM",
                "map_location": "Bashundhara, Dhaka"
            },
            {
                "branch_name": "Puran Dhaka (Old Dhaka)",
                "area": "Old Dhaka",
                "exact_address": "Nazimuddin Road, Old Dhaka",
                "phone": "01788-990011",
                "opening_hours": "12:00 PM - 11:00 PM",
                "map_location": "Old Dhaka"
            }
        ],
        "menu_categories": [
            {
                "category_name": "Basmati Mutton Kacchi",
                "items": [
                    {"name": "Basmati Kacchi (Half)", "description": "Fragrant Basmati rice cooked in pure ghee with tender mutton piece and spiced potato.", "price": 320, "currency": "BDT", "is_bestseller": True},
                    {"name": "Basmati Kacchi (Full)", "description": "Full plate of signature Basmati Mutton Kacchi with extra mutton.", "price": 490, "currency": "BDT", "is_bestseller": True},
                    {"name": "Kacchi Bhai Special Combo Platter", "description": "Basmati Kacchi, Chicken Roast, Shahi Jali Kabab, Borhani and Salad.", "price": 599, "currency": "BDT", "is_bestseller": True},
                    {"name": "Family Feast Kacchi (1:3)", "description": "Sharing platter for 3 persons with 3 mutton pieces, 3 eggs and 3 potatoes.", "price": 1399, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Beef Kacchi & Tehari",
                "items": [
                    {"name": "Basmati Beef Kacchi (Half)", "description": "Aromatic Basmati rice slow-cooked with tender beef chunks and aloo.", "price": 290, "currency": "BDT", "is_bestseller": True},
                    {"name": "Basmati Beef Kacchi (Full)", "description": "Generous full serving of Basmati Beef Kacchi.", "price": 450, "currency": "BDT", "is_bestseller": False},
                    {"name": "Shahi Beef Tehari", "description": "Traditional mustard oil seasoned Chinigura rice with spicy tender beef chunks.", "price": 260, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Polao & Roast",
                "items": [
                    {"name": "Shahi Morog Polao", "description": "Chinigura rice polao cooked with whole quarter chicken in rich spices.", "price": 310, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chicken Roast (1 Pc)", "description": "Tender chicken leg quarter simmered in sweet-savory browned onion gravy.", "price": 140, "currency": "BDT", "is_bestseller": True},
                    {"name": "Shahi Jali Kabab (1 Pc)", "description": "Minced beef kabab enveloped in crisp egg netting.", "price": 60, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Beverages & Desserts",
                "items": [
                    {"name": "Special Shahi Borhani (250ml)", "description": "Chilled digestive spiced yogurt drink with roasted cumin and fresh mint.", "price": 70, "currency": "BDT", "is_bestseller": True},
                    {"name": "Special Shahi Borhani (1 Liter)", "description": "1 Liter family bottle of chilled Borhani.", "price": 250, "currency": "BDT", "is_bestseller": True},
                    {"name": "Shahi Jorda", "description": "Sweet saffron rice garnished with baby sweets and nuts.", "price": 70, "currency": "BDT", "is_bestseller": True},
                    {"name": "Shahi Firni (Clay Cup)", "description": "Traditional creamy cardamom rice pudding in clay cup.", "price": 70, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },
    {
        "id": "burger-king-bangladesh",
        "name": "Burger King Bangladesh",
        "tagline": "Taste is King • Home of the Whopper",
        "cuisine": ["Fast Food", "Burgers", "Wings", "Fries"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.5,
        "review_count": "22K+",
        "logo": "https://images.unsplash.com/photo-1550547660-d9450f859349?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=1200&auto=format&fit=crop&q=80",
        "hotline": "09606-224466",
        "total_branches": 10,
        "branches": [
            {
                "branch_name": "Banani Kemal Ataturk",
                "area": "Banani",
                "exact_address": "Plot 43, Kemal Ataturk Avenue, Banani, Dhaka 1213",
                "phone": "09606-224466",
                "opening_hours": "11:00 AM - 11:30 PM",
                "map_location": "Banani, Dhaka"
            },
            {
                "branch_name": "Gulshan 2 Circle",
                "area": "Gulshan",
                "exact_address": "House 18, Road 103, Gulshan 2, Dhaka 1212",
                "phone": "09606-224466",
                "opening_hours": "11:00 AM - 11:30 PM",
                "map_location": "Gulshan 2, Dhaka"
            },
            {
                "branch_name": "Dhanmondi Satmasjid Road",
                "area": "Dhanmondi",
                "exact_address": "House 750, Satmasjid Road, Dhanmondi, Dhaka 1205",
                "phone": "09606-224466",
                "opening_hours": "11:00 AM - 11:00 PM",
                "map_location": "Dhanmondi, Dhaka"
            },
            {
                "branch_name": "Uttara Sector 3",
                "area": "Uttara",
                "exact_address": "Plot 19, Jashimuddin Avenue, Sector 3, Uttara, Dhaka",
                "phone": "09606-224466",
                "opening_hours": "11:00 AM - 11:00 PM",
                "map_location": "Uttara, Dhaka"
            },
            {
                "branch_name": "Mirpur 1",
                "area": "Mirpur",
                "exact_address": "Plot 2, Block D, Sony Cinema Roundabout, Mirpur 1, Dhaka",
                "phone": "09606-224466",
                "opening_hours": "11:00 AM - 11:00 PM",
                "map_location": "Mirpur 1, Dhaka"
            },
            {
                "branch_name": "Bailey Road",
                "area": "Bailey Road",
                "exact_address": "Green Cozy Cottage, New Bailey Road, Dhaka",
                "phone": "09606-224466",
                "opening_hours": "11:00 AM - 11:00 PM",
                "map_location": "Bailey Road, Dhaka"
            }
        ],
        "menu_categories": [
            {
                "category_name": "Flame-Grilled Whopper & Beef Burgers",
                "items": [
                    {"name": "Whopper (Signature Flame-Grilled)", "description": "100% flame-grilled beef patty topped with juicy tomatoes, crisp lettuce, creamy mayo, pickles and sliced onions on a toasted sesame bun.", "price": 449, "currency": "BDT", "is_bestseller": True},
                    {"name": "Double Whopper", "description": "Two flame-grilled beef patties with all signature Whopper toppings.", "price": 649, "currency": "BDT", "is_bestseller": True},
                    {"name": "Whopper Jr.", "description": "A smaller portion of the iconic flame-grilled Whopper.", "price": 289, "currency": "BDT", "is_bestseller": False},
                    {"name": "BBQ Bacon Double Cheeseburger", "description": "Two flame-grilled patties topped with crispy beef bacon, melted cheese and smoky BBQ glaze.", "price": 499, "currency": "BDT", "is_bestseller": True},
                    {"name": "Single Beef Cheeseburger", "description": "Flame-grilled beef patty with yellow American cheese, pickles and mustard ketchup.", "price": 219, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Chicken Burgers & Sandwiches",
                "items": [
                    {"name": "Chicken Royale Burger", "description": "Crispy long chicken breast patty with shredded lettuce and creamy mayo on a sesame seed long bun.", "price": 389, "currency": "BDT", "is_bestseller": True},
                    {"name": "Crispy Chicken Cheeseburger", "description": "Golden fried chicken fillet layered with cheese, fresh lettuce and mayo.", "price": 269, "currency": "BDT", "is_bestseller": True},
                    {"name": "Spicy Crispy Chicken Burger", "description": "Spicy coated crispy chicken patty with fiery chili sauce.", "price": 289, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "King Sides & Fries",
                "items": [
                    {"name": "BK King French Fries (Large)", "description": "Thick-cut golden potato fries, crispy outside and fluffy inside.", "price": 169, "currency": "BDT", "is_bestseller": True},
                    {"name": "Onion Rings (8 Pcs)", "description": "Crispy golden battered whole onion rings with savory dipping sauce.", "price": 179, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chicken Tenders (4 Pcs)", "description": "Golden breaded white meat chicken tenders with BBQ sauce.", "price": 219, "currency": "BDT", "is_bestseller": False},
                    {"name": "Cheesy Fries", "description": "Fries drenched in warm velvety cheddar sauce.", "price": 229, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Beverages & Desserts",
                "items": [
                    {"name": "Chocolate Thick Shake", "description": "Creamy soft serve blended with chocolate syrup.", "price": 229, "currency": "BDT", "is_bestseller": True},
                    {"name": "Soft Drinks (Coca-Cola / Sprite)", "description": "Chilled carbonated beverage.", "price": 50, "currency": "BDT", "is_bestseller": False},
                    {"name": "Hot Chocolate Fudge Sundae", "description": "Creamy vanilla soft serve smothered in rich hot fudge sauce.", "price": 149, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    },
    {
        "id": "dominos-pizza-bangladesh",
        "name": "Domino's Pizza Bangladesh",
        "tagline": "It's All About the Crust & Cheese",
        "cuisine": ["Pizza", "Pasta", "Garlic Bread", "Fast Food"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.6,
        "review_count": "29K+",
        "logo": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=1200&auto=format&fit=crop&q=80",
        "hotline": "16656",
        "total_branches": 15,
        "branches": [
            {
                "branch_name": "Dhanmondi Satmasjid Road",
                "area": "Dhanmondi",
                "exact_address": "House 754, Satmasjid Road, Dhanmondi, Dhaka 1205",
                "phone": "16656",
                "opening_hours": "11:00 AM - 11:30 PM",
                "map_location": "Dhanmondi, Dhaka"
            },
            {
                "branch_name": "Banani Road 11",
                "area": "Banani",
                "exact_address": "House 27, Road 11, Block F, Banani, Dhaka",
                "phone": "16656",
                "opening_hours": "11:00 AM - 11:30 PM",
                "map_location": "Banani, Dhaka"
            },
            {
                "branch_name": "Gulshan 1 Circle",
                "area": "Gulshan",
                "exact_address": "Plot 1, Block NW(H), Gulshan 1, Dhaka",
                "phone": "16656",
                "opening_hours": "11:00 AM - 11:30 PM",
                "map_location": "Gulshan 1, Dhaka"
            },
            {
                "branch_name": "Uttara Sector 11",
                "area": "Uttara",
                "exact_address": "Plot 32, Gareeb-e-Nawaz Avenue, Sector 11, Uttara, Dhaka",
                "phone": "16656",
                "opening_hours": "11:00 AM - 11:30 PM",
                "map_location": "Uttara, Dhaka"
            },
            {
                "branch_name": "Mirpur 2",
                "area": "Mirpur",
                "exact_address": "Plot 1, Block D, Section 2, Mirpur, Dhaka",
                "phone": "16656",
                "opening_hours": "11:00 AM - 11:30 PM",
                "map_location": "Mirpur 2, Dhaka"
            },
            {
                "branch_name": "Khilgaon Taltola",
                "area": "Khilgaon",
                "exact_address": "383 Shahid Baki Road, Khilgaon, Dhaka",
                "phone": "16656",
                "opening_hours": "11:00 AM - 11:30 PM",
                "map_location": "Khilgaon, Dhaka"
            },
            {
                "branch_name": "Bashundhara R/A",
                "area": "Bashundhara",
                "exact_address": "Block C, Main Road, Bashundhara R/A, Dhaka",
                "phone": "16656",
                "opening_hours": "11:00 AM - 11:30 PM",
                "map_location": "Bashundhara, Dhaka"
            }
        ],
        "menu_categories": [
            {
                "category_name": "Non-Veg Pizzas (Regular, Medium, Large)",
                "items": [
                    {"name": "Chicken Dominator Pizza", "description": "Loaded with double peri-peri chicken, grilled chicken rashers, chicken tikka and double mozzarella.", "price": 499, "currency": "BDT", "sizes": [{"size": "Regular 7\"", "price": 499}, {"size": "Medium 10\"", "price": 899}, {"size": "Large 12\"", "price": 1299}], "is_bestseller": True},
                    {"name": "Pepperoni Feast Pizza", "description": "Generous layers of premium beef pepperoni and 100% genuine mozzarella cheese.", "price": 449, "currency": "BDT", "sizes": [{"size": "Regular 7\"", "price": 449}, {"size": "Medium 10\"", "price": 799}, {"size": "Large 12\"", "price": 1199}], "is_bestseller": True},
                    {"name": "Chicken Tikka Supreme Pizza", "description": "Tandoori chicken tikka, red paprika, mint drizzle, onions and mozzarella.", "price": 429, "currency": "BDT", "sizes": [{"size": "Regular 7\"", "price": 429}, {"size": "Medium 10\"", "price": 749}, {"size": "Large 12\"", "price": 1149}], "is_bestseller": True},
                    {"name": "BBQ Chicken Feast Pizza", "description": "Smoky BBQ chicken chunks, capsicum, red onion and mozzarella on fresh hand-tossed dough.", "price": 399, "currency": "BDT", "sizes": [{"size": "Regular 7\"", "price": 399}, {"size": "Medium 10\"", "price": 699}, {"size": "Large 12\"", "price": 1049}], "is_bestseller": False}
                ]
            },
            {
                "category_name": "Veg & Cheese Pizzas",
                "items": [
                    {"name": "Margherita Classic Pizza", "description": "Classic Italian pizza with double mozzarella cheese and herbed marinara.", "price": 299, "currency": "BDT", "sizes": [{"size": "Regular 7\"", "price": 299}, {"size": "Medium 10\"", "price": 549}], "is_bestseller": False},
                    {"name": "Farmhouse Veg Pizza", "description": "Crunchy bell peppers, sweet corn, button mushrooms, onions and cheese.", "price": 349, "currency": "BDT", "sizes": [{"size": "Regular 7\"", "price": 349}, {"size": "Medium 10\"", "price": 599}], "is_bestseller": False}
                ]
            },
            {
                "category_name": "Garlic Breads & Sides",
                "items": [
                    {"name": "Stuffed Garlic Bread with Cheese", "description": "Freshly baked garlic bread stuffed with melted mozzarella, sweet corn and jalapenos.", "price": 249, "currency": "BDT", "is_bestseller": True},
                    {"name": "Stuffed Garlic Bread with Chicken Tikka", "description": "Garlic bread stuffed with spicy chicken tikka and molten cheese.", "price": 289, "currency": "BDT", "is_bestseller": True},
                    {"name": "Roasted Chicken Wings (6 Pcs)", "description": "Tender oven-roasted chicken wings basted in peri-peri sauce.", "price": 269, "currency": "BDT", "is_bestseller": False},
                    {"name": "Cheesy Dip", "description": "Creamy jalapeno cheese dip.", "price": 49, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Desserts & Drinks",
                "items": [
                    {"name": "Choco Lava Cake", "description": "Warm chocolate sponge with rich melted liquid chocolate inside.", "price": 169, "currency": "BDT", "is_bestseller": True},
                    {"name": "Coca-Cola (500ml Bottle)", "description": "Chilled beverage bottle.", "price": 50, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    },
    {
        "id": "star-kabab",
        "name": "Star Kabab & Restaurant",
        "tagline": "Dhaka's Historic Culinary Heritage Since 1971",
        "cuisine": ["Kebab", "Traditional", "Desi", "Mutton"],
        "price_range": "৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.6,
        "review_count": "55K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01711-335577",
        "total_branches": 7,
        "branches": [
            {
                "branch_name": "Dhanmondi Satmasjid Road",
                "area": "Dhanmondi",
                "exact_address": "House 48, Road 2, Satmasjid Road, Dhanmondi, Dhaka 1205",
                "phone": "01711-335577",
                "opening_hours": "06:30 AM - 11:00 PM",
                "map_location": "Dhanmondi 2, Dhaka"
            },
            {
                "branch_name": "Dhanmondi 8/A",
                "area": "Dhanmondi",
                "exact_address": "Road 8/A, Satmasjid Road, Dhanmondi, Dhaka",
                "phone": "01711-335577",
                "opening_hours": "06:30 AM - 11:00 PM",
                "map_location": "Dhanmondi 8/A, Dhaka"
            },
            {
                "branch_name": "Banani Road 11",
                "area": "Banani",
                "exact_address": "House 100, Road 11, Block C, Banani, Dhaka",
                "phone": "01711-335577",
                "opening_hours": "06:30 AM - 11:00 PM",
                "map_location": "Banani Road 11, Dhaka"
            },
            {
                "branch_name": "Elephant Road",
                "area": "Dhanmondi",
                "exact_address": "Multiplan Center area, Elephant Road, Dhaka",
                "phone": "01711-335577",
                "opening_hours": "06:30 AM - 11:00 PM",
                "map_location": "Elephant Road, Dhaka"
            },
            {
                "branch_name": "Kawran Bazar",
                "area": "Panthapath",
                "exact_address": "Opposite BSEC Bhaban, Kazi Nazrul Islam Ave, Kawran Bazar, Dhaka",
                "phone": "01711-335577",
                "opening_hours": "06:30 AM - 11:00 PM",
                "map_location": "Kawran Bazar, Dhaka"
            }
        ],
        "menu_categories": [
            {
                "category_name": "Charcoal Kebabs & Tandoor",
                "items": [
                    {"name": "Star Mutton Boti Kabab", "description": "Tender charcoal-grilled marinated mutton boti skewers with mustard oil aroma.", "price": 180, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chicken Seekh Kabab", "description": "Spiced minced chicken skewered and roasted on charcoal embers.", "price": 130, "currency": "BDT", "is_bestseller": True},
                    {"name": "Mutton Seekh Kabab", "description": "Traditional minced mutton seekh kabab with coriander, cumin and chilies.", "price": 170, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chicken Tikka (1 Pc)", "description": "Spiced chicken breast roasted red in traditional clay tandoor.", "price": 140, "currency": "BDT", "is_bestseller": False},
                    {"name": "Butter Tandoori Naan", "description": "Freshly baked clay oven flatbread basted with pure butter.", "price": 40, "currency": "BDT", "is_bestseller": True},
                    {"name": "Garlic Naan", "description": "Tandoori naan topped with roasted chopped garlic and cilantro.", "price": 50, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Chaap, Fry & Curries",
                "items": [
                    {"name": "Star Chicken Chaap", "description": "Flattened chicken leg quarter marinated in rich spices and pan-fried in oil.", "price": 160, "currency": "BDT", "is_bestseller": True},
                    {"name": "Beef Chaap", "description": "Thin tender beef cutlet spiced and shallow fried on a giant tawa.", "price": 170, "currency": "BDT", "is_bestseller": True},
                    {"name": "Mutton Leg Roast (Quarter)", "description": "Slow braised mutton leg in rich spiced gravy.", "price": 320, "currency": "BDT", "is_bestseller": True},
                    {"name": "Dhakaiya Nehari (Morning Only)", "description": "Slow simmered bone marrow and shank stew served with naan.", "price": 190, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Biryani & Polao",
                "items": [
                    {"name": "Star Mutton Kacchi Biryani", "description": "Traditional Chinigura rice cooked with tender spiced mutton pieces.", "price": 270, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chicken Roast with Polao", "description": "Fragrant polao served with 1 pc chicken roast and boiled egg.", "price": 240, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Desserts & Traditional Drinks",
                "items": [
                    {"name": "Star Special Faluda", "description": "Creamy chilled dessert layered with vermicelli, basil seeds, jelly, fruits and rich ice cream.", "price": 130, "currency": "BDT", "is_bestseller": True},
                    {"name": "Borhani (Glass)", "description": "Refreshing traditional spiced yogurt drink.", "price": 50, "currency": "BDT", "is_bestseller": True},
                    {"name": "Special Doodh Cha (Milk Tea)", "description": "Dhaka's famous malai-topped boiled milk tea.", "price": 30, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    },
    {
        "id": "north-end-coffee",
        "name": "North End Coffee Roasters",
        "tagline": "Pioneers of Artisanal Specialty Coffee in Bangladesh",
        "cuisine": ["Specialty Coffee", "Cafe", "Bakery", "Desserts"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.8,
        "review_count": "16K+",
        "logo": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1498654896293-37aacf113fd9?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01777-744332",
        "total_branches": 9,
        "branches": [
            {
                "branch_name": "Banani Road 11 (Main)",
                "area": "Banani",
                "exact_address": "House 54, Road 11, Block D, Banani, Dhaka 1213",
                "phone": "01777-744332",
                "opening_hours": "07:30 AM - 11:30 PM",
                "map_location": "Banani, Dhaka"
            },
            {
                "branch_name": "Dhanmondi Satmasjid Road",
                "area": "Dhanmondi",
                "exact_address": "KB Square (Level 2), Road 9/A, Satmasjid Road, Dhanmondi, Dhaka",
                "phone": "01777-744332",
                "opening_hours": "08:00 AM - 11:00 PM",
                "map_location": "Dhanmondi, Dhaka"
            },
            {
                "branch_name": "Gulshan 2 Avenue",
                "area": "Gulshan",
                "exact_address": "Road 50, Gulshan 2 (Opposite American Club), Dhaka",
                "phone": "01777-744332",
                "opening_hours": "07:30 AM - 11:30 PM",
                "map_location": "Gulshan 2, Dhaka"
            },
            {
                "branch_name": "Uttara Sector 3",
                "area": "Uttara",
                "exact_address": "House 14, Sector 3, Rabindra Sarani, Uttara, Dhaka",
                "phone": "01777-744332",
                "opening_hours": "08:00 AM - 11:00 PM",
                "map_location": "Uttara, Dhaka"
            },
            {
                "branch_name": "Bashundhara R/A",
                "area": "Bashundhara",
                "exact_address": "Main Entrance, Bashundhara R/A, Dhaka",
                "phone": "01777-744332",
                "opening_hours": "08:00 AM - 11:00 PM",
                "map_location": "Bashundhara, Dhaka"
            }
        ],
        "menu_categories": [
            {
                "category_name": "Artisanal Hot & Cold Coffees",
                "items": [
                    {"name": "Espresso (Single / Double)", "description": "Freshly roasted single-origin Arabica espresso shot.", "price": 140, "currency": "BDT", "is_bestseller": False},
                    {"name": "Cafe Americano", "description": "Rich espresso topped with hot water for a smooth, deep coffee finish.", "price": 190, "currency": "BDT", "is_bestseller": True},
                    {"name": "Classic Cappuccino", "description": "Equal parts espresso, steamed milk and thick velvety microfoam.", "price": 240, "currency": "BDT", "is_bestseller": True},
                    {"name": "Caffe Latte", "description": "Rich espresso combined with steamed milk and a light foam layer.", "price": 250, "currency": "BDT", "is_bestseller": True},
                    {"name": "Spanish Latte (Condensed Milk)", "description": "Espresso paired with sweetened condensed milk and steamed textured milk.", "price": 290, "currency": "BDT", "is_bestseller": True},
                    {"name": "Iced Caramel Macchiato", "description": "Chilled milk, vanilla syrup, espresso shots and rich caramel drizzle.", "price": 310, "currency": "BDT", "is_bestseller": True},
                    {"name": "Cold Brew Coffee", "description": "Steeped for 18 hours in cold filtered water for ultra smooth, low-acid flavor.", "price": 240, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Bakery, Brownies & Cookies",
                "items": [
                    {"name": "Signature Chocolate Brownie", "description": "Dense, fudgy, decadent chocolate brownie with walnuts.", "price": 160, "currency": "BDT", "is_bestseller": True},
                    {"name": "New York Cheesecake Slice", "description": "Authentic rich cream cheese cake on graham cracker butter crust.", "price": 290, "currency": "BDT", "is_bestseller": True},
                    {"name": "Cinnamon Roll", "description": "Warm spiral pastry with cinnamon brown sugar and vanilla cream glaze.", "price": 180, "currency": "BDT", "is_bestseller": True},
                    {"name": "Butter Croissant", "description": "Flaky golden layered French butter croissant.", "price": 140, "currency": "BDT", "is_bestseller": False},
                    {"name": "Chocolate Chip Cookie (Giant)", "description": "Crisp edge, chewy center cookie packed with dark chocolate chips.", "price": 110, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Savories & Bagels",
                "items": [
                    {"name": "Smoked Chicken Bagel Sandwich", "description": "Freshly toasted sesame bagel with smoked chicken breast, cream cheese and gherkins.", "price": 340, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chicken Pesto Panini", "description": "Grilled Italian panini with chicken, basil pesto and melted mozzarella.", "price": 360, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    },
    {
        "id": "alfresco-dhaka",
        "name": "Alfresco",
        "tagline": "Italian Inspired Flavors & Continental Delights",
        "cuisine": ["Italian", "Pizza", "Pasta", "Platters"],
        "price_range": "৳৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.5,
        "review_count": "19K+",
        "logo": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01700-112233",
        "total_branches": 5,
        "branches": [
            {
                "branch_name": "Dhanmondi Satmasjid Road",
                "area": "Dhanmondi",
                "exact_address": "House 743, Satmasjid Road, Dhanmondi, Dhaka",
                "phone": "01700-112233",
                "opening_hours": "12:00 PM - 11:00 PM",
                "map_location": "Dhanmondi, Dhaka"
            },
            {
                "branch_name": "Khilgaon Taltola",
                "area": "Khilgaon",
                "exact_address": "Shahid Baki Road, Block C, Khilgaon, Dhaka",
                "phone": "01700-112233",
                "opening_hours": "12:00 PM - 11:00 PM",
                "map_location": "Khilgaon, Dhaka"
            },
            {
                "branch_name": "Uttara Sector 11",
                "area": "Uttara",
                "exact_address": "Gareeb-e-Nawaz Avenue, Sector 11, Uttara, Dhaka",
                "phone": "01700-112233",
                "opening_hours": "12:00 PM - 11:00 PM",
                "map_location": "Uttara, Dhaka"
            },
            {
                "branch_name": "Banani Road 11",
                "area": "Banani",
                "exact_address": "House 45, Road 11, Block E, Banani, Dhaka",
                "phone": "01700-112233",
                "opening_hours": "12:00 PM - 11:00 PM",
                "map_location": "Banani, Dhaka"
            }
        ],
        "menu_categories": [
            {
                "category_name": "Italian Pizzas (8\" / 12\")",
                "items": [
                    {"name": "Alfresco Special Meat Lovers Pizza", "description": "Loaded with seasoned beef, spicy chicken, sausage slices, capsicum and mozzarella.", "price": 420, "currency": "BDT", "sizes": [{"size": "8 inch", "price": 420}, {"size": "12 inch", "price": 720}], "is_bestseller": True},
                    {"name": "BBQ Chicken Pizza", "description": "Charbroiled BBQ chicken chunks, sweet onions, bell peppers and rich cheese layer.", "price": 390, "currency": "BDT", "sizes": [{"size": "8 inch", "price": 390}, {"size": "12 inch", "price": 680}], "is_bestseller": True},
                    {"name": "Four Cheese Pizza", "description": "Blend of mozzarella, parmesan, cheddar and gouda cheeses.", "price": 410, "currency": "BDT", "sizes": [{"size": "8 inch", "price": 410}, {"size": "12 inch", "price": 710}], "is_bestseller": False}
                ]
            },
            {
                "category_name": "Creamy & Baked Pastas",
                "items": [
                    {"name": "Oven Baked Fettuccine Alfredo", "description": "Fettuccine pasta in rich butter cream and parmesan sauce with chicken, baked golden.", "price": 380, "currency": "BDT", "is_bestseller": True},
                    {"name": "Baked Spicy Penne Arabbiata", "description": "Penne pasta in fiery garlic tomato sauce with chicken sausages and cheese crust.", "price": 360, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Set Meals & Platters",
                "items": [
                    {"name": "Alfresco Chicken Steak Platter", "description": "Pan-grilled chicken breast in mushroom gravy served with herb rice and sautéed veggies.", "price": 460, "currency": "BDT", "is_bestseller": True},
                    {"name": "Crispy Fish & Chips", "description": "Golden battered fish fillet with tartar sauce and hand-cut fries.", "price": 420, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]
    }
]

# Append only if not already present
for nr in new_restaurants:
    if nr["id"] not in existing_ids:
        data.append(nr)
        existing_ids.add(nr["id"])

with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

js_file = os.path.join(os.path.dirname(DATA_FILE), "restaurants_data.js")
with open(js_file, "w", encoding="utf-8") as f:
    f.write("window.RESTAURANTS_DATA = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n")

print(f"Total restaurants in database now: {len(data)}")
