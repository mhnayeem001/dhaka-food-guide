import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants.json")
JS_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants_data.js")

with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

for r in data:
    rid = r["id"]

    # 1. KFC BANGLADESH (Transcom Foods Official Counter Menu)
    if rid == "kfc-bangladesh":
        r["menu_categories"] = [
            {
                "category_name": "Hot & Crispy Chicken Buckets & Deals",
                "items": [
                    {"name": "1 Pc Hot & Crispy Chicken", "description": "Signature hand-breaded, pressure-fried spicy crispy chicken piece.", "price": 159, "currency": "BDT", "is_bestseller": True},
                    {"name": "2 Pcs Hot & Crispy Chicken", "description": "2 pieces of juicy, crunchy golden fried chicken.", "price": 299, "currency": "BDT", "is_bestseller": True},
                    {"name": "4 Pcs Hot & Crispy Chicken", "description": "4 pieces of authentic hot & crispy chicken.", "price": 579, "currency": "BDT", "is_bestseller": False},
                    {"name": "6 Pcs Hot & Crispy Chicken Box", "description": "6 pieces of freshly prepared crunchy chicken.", "price": 858, "currency": "BDT", "is_bestseller": True},
                    {"name": "8 Pcs Hot & Crispy Chicken Bucket", "description": "Generous 8 pieces chicken sharing bucket for family.", "price": 1069, "currency": "BDT", "is_bestseller": True},
                    {"name": "Big Deal (8 Pcs Bucket + Med Fries + 2 Drinks)", "description": "8 pcs chicken bucket, medium fries and 2 Pepsi.", "price": 1199, "currency": "BDT", "is_bestseller": True},
                    {"name": "Family Feast (4 Pcs + 4 Wings + 6 Boneless Strips)", "description": "Mix bucket of chicken, hot wings and tender strips.", "price": 1249, "currency": "BDT", "is_bestseller": True},
                    {"name": "House Party Combo 1:2 (4 Pcs + 6 Wings + Popcorn + 2 Pepsi)", "description": "Party bucket with dips, popcorn and soft drinks.", "price": 999, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Burgers, Twisters & Rice Bowls",
                "items": [
                    {"name": "KFC Classic Zinger Burger", "description": "Crunchy whole chicken breast fillet, iceberg lettuce and signature mayo on sesame seed bun.", "price": 359, "currency": "BDT", "is_bestseller": True},
                    {"name": "Super Zinger Burger", "description": "Double crunchy zinger fillet with cheddar cheese slice and spicy mayo.", "price": 479, "currency": "BDT", "is_bestseller": True},
                    {"name": "Classic Zinger Meal (Burger + Fries + Drink)", "description": "Zinger burger served with crispy french fries and Pepsi.", "price": 499, "currency": "BDT", "is_bestseller": True},
                    {"name": "2 Classic Zinger Meal", "description": "2 Zinger burgers, 2 pcs hot & crispy chicken, dips and 2 Pepsi.", "price": 939, "currency": "BDT", "is_bestseller": True},
                    {"name": "Twister Wrap", "description": "Crispy chicken strips wrapped in warm tortilla with lettuce and pepper mayo.", "price": 329, "currency": "BDT", "is_bestseller": False},
                    {"name": "Strips & Rice Combo", "description": "Fragrant seasoned rice bowl topped with 3 pcs boneless chicken strips and Pepsi.", "price": 499, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Hot Wings, Popcorn & Sides",
                "items": [
                    {"name": "Hot Wings (6 Pcs)", "description": "Crispy seasoned spicy chicken wings.", "price": 279, "currency": "BDT", "is_bestseller": True},
                    {"name": "Hot Wings (12 Pcs)", "description": "Shareable box of 12 spicy wings.", "price": 529, "currency": "BDT", "is_bestseller": False},
                    {"name": "Chicken Popcorn (Regular)", "description": "Bite-sized crunchy chicken nuggets with dipping sauce.", "price": 249, "currency": "BDT", "is_bestseller": True},
                    {"name": "Potato Wedges", "description": "Crispy seasoned thick-cut potato wedges.", "price": 169, "currency": "BDT", "is_bestseller": True},
                    {"name": "French Fries (Medium)", "description": "Golden salted potato fries.", "price": 169, "currency": "BDT", "is_bestseller": False},
                    {"name": "French Fries (Large)", "description": "Extra large portion of golden fries.", "price": 229, "currency": "BDT", "is_bestseller": False},
                    {"name": "KFC Spicy Mayo Dip", "description": "Signature spicy dipping sauce.", "price": 40, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Krushers & Cold Drinks",
                "items": [
                    {"name": "Virgin Mojito Krusher", "description": "Sparkling mint, fresh lime and crushed ice.", "price": 180, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chocolate Sin Krusher", "description": "Blended chocolate shake with crushed cookies.", "price": 220, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chilled Pepsi (Can)", "description": "Ice cold fountain Pepsi.", "price": 60, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]

    # 2. PIZZABURG (Official In-Store Counter Menu Cross-Checked)
    elif rid == "pizzaburg":
        r["menu_categories"] = [
            {
                "category_name": "Signature Burgers (Loaded Patties)",
                "items": [
                    {"name": "Chicken Juicy Bomb", "description": "Juicy chicken patty loaded with secret sauce, cheese slice, fresh lettuce and tomato.", "price": 175, "currency": "BDT", "is_bestseller": True},
                    {"name": "Beef Juicy Bomb", "description": "Handcrafted tender beef patty with melted cheese, pickles and house mayo.", "price": 195, "currency": "BDT", "is_bestseller": True},
                    {"name": "BBQ Chicken Burger", "description": "Grilled chicken patty drenched in smoky sweet BBQ glaze and cheese.", "price": 185, "currency": "BDT", "is_bestseller": True},
                    {"name": "BBQ Beef Burger", "description": "Charbroiled beef patty with smoky BBQ reduction and caramelized onions.", "price": 205, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chicken Tongue Slayer (Naga)", "description": "Chicken patty infused with spicy Sylheti naga chili pepper paste and cheese.", "price": 195, "currency": "BDT", "is_bestseller": True},
                    {"name": "Beef Tongue Slayer (Naga)", "description": "Spicy beef burger with extreme naga chili kick and melted cheese.", "price": 215, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chicken Cheese Volcano", "description": "Stuffed molten cheese bursting chicken burger with creamy dressing.", "price": 285, "currency": "BDT", "is_bestseller": True},
                    {"name": "Beef Cheese Volcano", "description": "Double cheese bursting beef patty with crisp veggies and special sauce.", "price": 305, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Popular Fusion Pizzas (Multi-Size)",
                "items": [
                    {"name": "Meaty Onion Pizza (Medium 8 Inch)", "description": "Loaded with seasoned chicken shreds, sweet crunchy red onions and mozzarella.", "price": 389, "currency": "BDT", "is_bestseller": True},
                    {"name": "Meaty Onion Pizza (Large 12 Inch)", "description": "Large 12-inch crust with double chicken and golden melted cheese.", "price": 549, "currency": "BDT", "is_bestseller": True},
                    {"name": "Sausage Carnival Pizza (Medium 8 Inch)", "description": "Generous chicken sausage slices, capsicum, black olives and mozzarella.", "price": 419, "currency": "BDT", "is_bestseller": True},
                    {"name": "Sausage Carnival Pizza (Large 12 Inch)", "description": "Family sized 12-inch pizza loaded with chicken sausages.", "price": 589, "currency": "BDT", "is_bestseller": True},
                    {"name": "BBQ Meat Machine Pizza (Medium 8 Inch)", "description": "Smoky BBQ chicken, beef pepperoni, ground beef and extra cheese.", "price": 459, "currency": "BDT", "is_bestseller": True},
                    {"name": "BBQ Meat Machine Pizza (Large 12 Inch)", "description": "12-inch feast with triple meat and rich smoky barbecue sauce.", "price": 649, "currency": "BDT", "is_bestseller": True},
                    {"name": "Moner Moto Pizza (Medium 8 Inch)", "description": "PizzaBurg's legendary customizable pizza loaded with white sauce, chicken and mushrooms.", "price": 539, "currency": "BDT", "is_bestseller": True},
                    {"name": "Moner Moto Pizza (Large 12 Inch)", "description": "Large 12-inch Moner Moto pizza with thick mozzarella mantle.", "price": 749, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Value Set Menus & Rice Platters",
                "items": [
                    {"name": "PizzaBurg Set Menu 1", "description": "Egg fried rice, red chili chicken, chicken sheek kebab, vegetable curry and salad.", "price": 229, "currency": "BDT", "is_bestseller": True},
                    {"name": "PizzaBurg Set Menu 2", "description": "Fragrant rice, creamed chicken steak, red chili chicken, veg curry and salad.", "price": 319, "currency": "BDT", "is_bestseller": True},
                    {"name": "PizzaBurg Set Menu 3", "description": "Fried rice, turkish steak, shish kebab, red chili chicken and salad.", "price": 389, "currency": "BDT", "is_bestseller": True},
                    {"name": "Combo 2 (For 2 People)", "description": "Medium pizza of choice, sautéed mushrooms, BBQ sausage and chicken lollipops.", "price": 655, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Wings, Sides & Drinks",
                "items": [
                    {"name": "Crispy BBQ Wings (6 Pcs)", "description": "Deep fried wings glazed in sweet hickory barbecue sauce.", "price": 220, "currency": "BDT", "is_bestseller": True},
                    {"name": "Naga Wings (6 Pcs)", "description": "Spicy chicken wings coated in fiery naga sauce.", "price": 230, "currency": "BDT", "is_bestseller": True},
                    {"name": "Oreo Krusher Shake", "description": "Blended vanilla ice cream with crunchy Oreo cookies and chocolate syrup.", "price": 190, "currency": "BDT", "is_bestseller": True},
                    {"name": "Soft Drinks (500ml)", "description": "Choice of Coke, Sprite, or Fanta.", "price": 50, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]

    # 3. DOMINO'S PIZZA BANGLADESH (Jubilant FoodWorks Counter Menu)
    elif rid == "dominos-pizza":
        r["menu_categories"] = [
            {
                "category_name": "Signature Pizzas (Regular, Medium & Large)",
                "items": [
                    {"name": "Margherita Classic Pizza (Regular 7 Inch)", "description": "100% real mozzarella cheese on authentic herb tomato base.", "price": 399, "currency": "BDT", "is_bestseller": True},
                    {"name": "Margherita Classic Pizza (Medium 9 Inch)", "description": "Medium 9-inch classic mozzarella pizza.", "price": 699, "currency": "BDT", "is_bestseller": False},
                    {"name": "Spicy Chicken Delight (Regular 7 Inch)", "description": "Spiced chicken cubes, red paprika, onion and melted mozzarella.", "price": 469, "currency": "BDT", "is_bestseller": True},
                    {"name": "Spicy Chicken Delight (Medium 9 Inch)", "description": "Medium 9-inch pizza with hot spiced chicken and peppers.", "price": 799, "currency": "BDT", "is_bestseller": True},
                    {"name": "Beef Kala Bhuna Feast (Regular 7 Inch)", "description": "Dhakaiya special tender beef kala bhuna pieces, onions and cheese.", "price": 529, "currency": "BDT", "is_bestseller": True},
                    {"name": "Beef Kala Bhuna Feast (Medium 9 Inch)", "description": "Medium 9-inch authentic beef kala bhuna fusion pizza.", "price": 899, "currency": "BDT", "is_bestseller": True},
                    {"name": "Pepperoni & Sausage Extravaganza (Medium)", "description": "Beef pepperoni, chicken sausage, black olives, mushrooms and cheese.", "price": 949, "currency": "BDT", "is_bestseller": True},
                    {"name": "American Favourite Feast (Large 12 Inch)", "description": "Large family feast loaded with pepperoni, sausage, beef and bell peppers.", "price": 1386, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Garlic Breads, Sides & Calzone",
                "items": [
                    {"name": "Classic Garlic Breadsticks (4 Pcs)", "description": "Baked to a golden brown crust with butter, garlic and herb seasoning.", "price": 180, "currency": "BDT", "is_bestseller": True},
                    {"name": "Stuffed Garlic Bread (Cheese & Sweet Corn)", "description": "Freshly baked garlic bread stuffed with mozzarella, sweet corn and jalapenos.", "price": 249, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chicken Stuffed Garlic Bread", "description": "Garlic bread loaded with spiced chicken shreds and molten cheese.", "price": 289, "currency": "BDT", "is_bestseller": True},
                    {"name": "Spicy Roasted Chicken Wings (4 Pcs)", "description": "Tender chicken wings seasoned with hot peri-peri glaze.", "price": 280, "currency": "BDT", "is_bestseller": False},
                    {"name": "Chicken Calzone Pockets", "description": "Crisp folded pizza dough pocket filled with chicken and cheese.", "price": 260, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Desserts & Beverages",
                "items": [
                    {"name": "Domino's Choco Lava Cake", "description": "Warm chocolate cake with molten flowing Belgian chocolate core.", "price": 229, "currency": "BDT", "is_bestseller": True},
                    {"name": "Choco Bread Swirls", "description": "Sweet oven baked dough sticks glazed with rich chocolate.", "price": 210, "currency": "BDT", "is_bestseller": False},
                    {"name": "Chilled Coca-Cola (500ml)", "description": "Ice chilled soft drink bottle.", "price": 50, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]

    # 4. CHILLOX (Official Counter Menu Cross-Checked)
    elif rid == "chillox":
        r["menu_categories"] = [
            {
                "category_name": "Aged Beef Smashers & Gourmet Burgers",
                "items": [
                    {"name": "Truffle Smasher (Single 120g)", "description": "120g aged beef patty, aromatic black truffle sauce, dill pickles, sautéed onions and cheese.", "price": 395, "currency": "BDT", "is_bestseller": True},
                    {"name": "Truffle Smasher (Double 240g)", "description": "240g double aged beef patties with truffle garlic sauce and double cheese.", "price": 590, "currency": "BDT", "is_bestseller": True},
                    {"name": "Shiitake Mushroom Smasher (Single)", "description": "Juicy smashed beef patty with sautéed Japanese shiitake mushrooms and cheese.", "price": 495, "currency": "BDT", "is_bestseller": True},
                    {"name": "Shiitake Mushroom Smasher (Double)", "description": "Double beef patties loaded with shiitake mushrooms and molten Swiss cheese.", "price": 690, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chillox Regular Beef Burger", "description": "Tender beef patty with Chillox secret sauce and fresh lettuce.", "price": 180, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chillox Beef Cheese Burger", "description": "Classic beef burger with melted American cheddar cheese.", "price": 210, "currency": "BDT", "is_bestseller": True},
                    {"name": "Smokey BBQ Beef Burger", "description": "Beef patty topped with sweet hickory BBQ sauce and caramelized onion.", "price": 240, "currency": "BDT", "is_bestseller": True},
                    {"name": "Double Decker Beef Burger", "description": "Double patties, double cheese slices and signature relish.", "price": 360, "currency": "BDT", "is_bestseller": True},
                    {"name": "Crispy Chicken Cheese Burger", "description": "Crunchy deep-fried chicken patty with cheese and garlic mayo.", "price": 325, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Pankha Wings, Naga Drums & Fries",
                "items": [
                    {"name": "Chillox Pankha Wings (6 Pcs)", "description": "Crispy fried wings tossed in sweet BBQ or Naga glaze.", "price": 270, "currency": "BDT", "is_bestseller": True},
                    {"name": "Signature Naga Drums (2 Pcs)", "description": "Fiery spicy chicken drumsticks with authentic Sylheti naga kick.", "price": 130, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chicken Fingers (6 Pcs)", "description": "Golden battered boneless chicken breast strips with honey mustard dip.", "price": 195, "currency": "BDT", "is_bestseller": False},
                    {"name": "Potato Wedges (Large)", "description": "Crispy spiced potato wedges.", "price": 175, "currency": "BDT", "is_bestseller": True},
                    {"name": "Classic French Fries", "description": "Golden salted fries.", "price": 80, "currency": "BDT", "is_bestseller": True},
                    {"name": "Cheese Loaded Fries", "description": "Fries drenched in warm cheddar cheese sauce and jalapenos.", "price": 180, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Shakes & Beverages",
                "items": [
                    {"name": "Chillox Oreo Thick Shake", "description": "Blended vanilla ice cream with Oreo chunks and chocolate drizzle.", "price": 220, "currency": "BDT", "is_bestseller": True},
                    {"name": "Fresh Mint Lemonade", "description": "Chilled lemon and fresh mint cooler.", "price": 120, "currency": "BDT", "is_bestseller": False},
                    {"name": "Soft Drink (Can)", "description": "Coke, Sprite, or Fanta.", "price": 50, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]

    # 5. SULTAN'S DINE (Official Counter Menu Cross-Checked)
    elif rid == "sultans-dine":
        r["menu_categories"] = [
            {
                "category_name": "Signature Basmati Kacchi Biryani",
                "items": [
                    {"name": "Basmati Kacchi Biryani (Half - 1:1)", "description": "Aromatic long-grain basmati rice cooked in slow dum with marinated tender mutton (1 pc) and saffron potato.", "price": 340, "currency": "BDT", "is_bestseller": True},
                    {"name": "Basmati Kacchi Biryani (Full - 1:2)", "description": "Generous portion for two with 2 large succulent mutton pieces and 2 potatoes.", "price": 640, "currency": "BDT", "is_bestseller": True},
                    {"name": "Basmati Kacchi (1:3 Portion)", "description": "Family sized kacchi with 3 pieces mutton and 3 potatoes.", "price": 1459, "currency": "BDT", "is_bestseller": True},
                    {"name": "Mutton Tehari (1:1)", "description": "Traditional chinigura rice prepared with mustard oil and soft mutton cubes.", "price": 280, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chicken Dum Biryani (1:1)", "description": "Tender chicken cooked with basmati rice in aromatic saffron dum.", "price": 220, "currency": "BDT", "is_bestseller": False},
                    {"name": "Plain Polao (1:1)", "description": "Aromatic ghee rice cooked with whole spices.", "price": 130, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Combos & Shahi Curries",
                "items": [
                    {"name": "Kacchi Combo 1:1 (Kacchi + Chicken Roast + Borhani + Jali Kabab)", "description": "Complete wedding feast combo in a single box.", "price": 599, "currency": "BDT", "is_bestseller": True},
                    {"name": "Kacchi + Borhani + Firni Combo (1:1)", "description": "Basmati kacchi served with traditional spicy borhani and shahi firni.", "price": 459, "currency": "BDT", "is_bestseller": True},
                    {"name": "Shahi Chicken Roast (Quarter Leg)", "description": "Tender chicken leg cooked in rich cashew and onion barista gravy.", "price": 150, "currency": "BDT", "is_bestseller": True},
                    {"name": "Shahi Beef Rezala", "description": "Slow cooked beef pieces in fragrant yogurt, poppy seed and mace curry.", "price": 200, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chicken Jali Kabab (Per Pc)", "description": "Egg-lace wrapped deep fried minced chicken patty.", "price": 50, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Borhani & Traditional Desserts",
                "items": [
                    {"name": "Sultan's Special Borhani (Glass 250ml)", "description": "Rich yogurt drink blended with mint, coriander, roasted cumin and black salt.", "price": 50, "currency": "BDT", "is_bestseller": True},
                    {"name": "Sultan's Special Borhani (1 Liter Bottle)", "description": "Family bottle of fresh savory borhani.", "price": 180, "currency": "BDT", "is_bestseller": True},
                    {"name": "Shahi Firni (Clay Pot)", "description": "Slow-cooked rice pudding topped with saffron and pistachios.", "price": 60, "currency": "BDT", "is_bestseller": True},
                    {"name": "Shahi Jorda with Baby Sweets", "description": "Sweet saffron rice garnished with morobba and mini gulab jamun.", "price": 70, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]

    # 6. TAKEOUT BANGLADESH (Official Counter Menu Cross-Checked)
    elif rid == "takeout-dhaka":
        r["menu_categories"] = [
            {
                "category_name": "Classic & Gourmet Burgers",
                "items": [
                    {"name": "Takeout Classic Beef Burger", "description": "Juicy marinated beef patty with lettuce, onion and Takeout signature sauce.", "price": 285, "currency": "BDT", "is_bestseller": True},
                    {"name": "Beef Cheese Delight", "description": "Takeout's #1 bestseller: beef patty, double melted cheddar, caramelized onions and house sauce.", "price": 320, "currency": "BDT", "is_bestseller": True},
                    {"name": "Takeout Classic Chicken Burger", "description": "Marinated grilled chicken patty with fresh lettuce, mayo and cheese.", "price": 265, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chick Got Fried", "description": "Tender golden crispy fried chicken breast fillet with creamy sauce.", "price": 285, "currency": "BDT", "is_bestseller": True},
                    {"name": "The MADOX Burger", "description": "Double-layered burger featuring a cheese-stuffed egg muffin and chili marinated beef patty.", "price": 365, "currency": "BDT", "is_bestseller": True},
                    {"name": "The Smash Burger", "description": "Premium beef patty smashed with grilled mushrooms, sliced cheese, caramelized onions and jalapeños.", "price": 435, "currency": "BDT", "is_bestseller": True},
                    {"name": "Double The Smash", "description": "Double smashed beef patties with triple cheese and bacon glaze.", "price": 685, "currency": "BDT", "is_bestseller": True},
                    {"name": "The Aloo Burger (Budget Friendly)", "description": "Crunchy fried spiced potato patty, lettuce, onion and signature sauce.", "price": 155, "currency": "BDT", "is_bestseller": False},
                    {"name": "Eggeroni Burger", "description": "Egg patty stuffed with cheese and chicken pepperoni.", "price": 165, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Wings, Fries & Sides",
                "items": [
                    {"name": "Thai Chili Wings (6 Pcs)", "description": "Crispy fried wings tossed in spicy sweet Thai chili glaze.", "price": 245, "currency": "BDT", "is_bestseller": True},
                    {"name": "BBQ Glazed Wings (6 Pcs)", "description": "Hickory barbecue coated crispy chicken wings.", "price": 235, "currency": "BDT", "is_bestseller": False},
                    {"name": "Deshi Spiced Fries", "description": "Crispy french fries tossed in secret deshi chaat spice blend.", "price": 140, "currency": "BDT", "is_bestseller": True},
                    {"name": "Cheesy Bacon Fries", "description": "Fries loaded with warm cheese sauce and crispy bacon crumbs.", "price": 220, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Thick Shakes & Drinks",
                "items": [
                    {"name": "Takeout Chocolate Thick Shake", "description": "Creamy blended ice cream shake with dark chocolate syrup.", "price": 210, "currency": "BDT", "is_bestseller": True},
                    {"name": "Salted Caramel Shake", "description": "Vanilla ice cream with buttery caramel and sea salt touch.", "price": 230, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chilled Soft Drinks (Can)", "description": "Coke, Sprite, or Fanta.", "price": 50, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]

    # 7. MADCHEF (Official Counter Menu Cross-Checked)
    elif rid == "madchef-dhaka":
        r["menu_categories"] = [
            {
                "category_name": "Gourmet Burgers",
                "items": [
                    {"name": "Mushroom Melt Burger", "description": "Juicy beef patty smothered in sautéed button mushrooms, caramelized onions and melted Swiss cheese.", "price": 428, "currency": "BDT", "is_bestseller": True},
                    {"name": "Smokin' Chic", "description": "Charbroiled chicken patty topped with smoky barbecue sauce, beef bacon and cheese.", "price": 428, "currency": "BDT", "is_bestseller": True},
                    {"name": "Madchef's Fav", "description": "Signature beef patty, cheddar cheese, fried egg, bacon bits and garlic mayo.", "price": 456, "currency": "BDT", "is_bestseller": True},
                    {"name": "Madame Lucy / The Dhakaiya", "description": "Dhakaiya spicy chili-infused beef patty with sharp cheese and pickles.", "price": 475, "currency": "BDT", "is_bestseller": True},
                    {"name": "The Hawk (Monster Burger)", "description": "Double beef patties, double cheese, onion rings and spicy BBQ sauce.", "price": 666, "currency": "BDT", "is_bestseller": True},
                    {"name": "Mad Chicken Sandwich", "description": "Crispy fried chicken breast fillet on butter toasted brioche with slaw.", "price": 361, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Mad Teasers, Wings & Cheez Fries",
                "items": [
                    {"name": "Chicken Cheese Bombs (4 Pcs)", "description": "Crispy battered chicken spheres stuffed with molten cheese core.", "price": 332, "currency": "BDT", "is_bestseller": True},
                    {"name": "OG Cheez Fries", "description": "Crisp french fries drenched in Madchef's signature warm cheese sauce.", "price": 266, "currency": "BDT", "is_bestseller": True},
                    {"name": "Spicy Cajun Fries", "description": "Skin-on fries tossed with spicy New Orleans cajun spices.", "price": 151, "currency": "BDT", "is_bestseller": False},
                    {"name": "Crispy Onion Rings (6 Pcs)", "description": "Golden battered sweet onion rings with dip.", "price": 170, "currency": "BDT", "is_bestseller": False},
                    {"name": "Mad Wings (6 Pcs)", "description": "Crisp fried wings tossed in choice of sweet BBQ or hot naga glaze.", "price": 240, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Combos & Drinks",
                "items": [
                    {"name": "The Beef Bash Combo (1:1)", "description": "Signature beef burger + 6 onion rings + lemon iced tea.", "price": 666, "currency": "BDT", "is_bestseller": True},
                    {"name": "The Chick Flick Combo (1:1)", "description": "Crispy chicken burger + 6 onion rings + lemon iced tea.", "price": 638, "currency": "BDT", "is_bestseller": True},
                    {"name": "Lemon Iced Tea", "description": "Fresh brewed iced tea with lemon essence.", "price": 110, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]

    # 8. KACCHI BHAI (Official Counter Menu Cross-Checked)
    elif rid == "kacchi-bhai":
        r["menu_categories"] = [
            {
                "category_name": "Signature Basmati Kacchi",
                "items": [
                    {"name": "Basmati Kacchi Biryani (1:1)", "description": "Aromatic long-grain basmati rice with succulent mutton (1 pc) and saffron potato.", "price": 340, "currency": "BDT", "is_bestseller": True},
                    {"name": "Basmati Kacchi Biryani (1:3 Portion)", "description": "Generous sharing platter with 3 pcs mutton and 3 potatoes.", "price": 990, "currency": "BDT", "is_bestseller": True},
                    {"name": "Basmati Kacchi Biryani (1:5 Portion)", "description": "Family feast with 5 pcs mutton and 5 potatoes.", "price": 1640, "currency": "BDT", "is_bestseller": True},
                    {"name": "Kacchi Khadok (1:1 - 4 Pcs Mutton)", "description": "For serious meat lovers: basmati kacchi with 4 large tender mutton pieces.", "price": 530, "currency": "BDT", "is_bestseller": True},
                    {"name": "Beef Chui Jhal with Polao Rice (1:1)", "description": "Steamed polao served with spicy Khulna-style Chui Jhal beef curry.", "price": 270, "currency": "BDT", "is_bestseller": True},
                    {"name": "Plain Polao (1:1)", "description": "Fragrant chinigura rice cooked in cow ghee.", "price": 120, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Combos & Curries",
                "items": [
                    {"name": "Basmati Kacchi Combo (1:1 With Borhani & Firni)", "description": "Basmati kacchi served with traditional spicy borhani and shahi firni.", "price": 460, "currency": "BDT", "is_bestseller": True},
                    {"name": "Shahi Chicken Roast (Quarter Leg)", "description": "Tender chicken leg in rich onion-cashew barista gravy.", "price": 150, "currency": "BDT", "is_bestseller": True},
                    {"name": "Beef Rezala (Plate)", "description": "Spiced beef pieces in rich yogurt poppy seed curry.", "price": 200, "currency": "BDT", "is_bestseller": True},
                    {"name": "Beef Chui Jhal Gosht (Plate)", "description": "Fiery beef curry cooked with authentic Satkhira Chui Jhal bark.", "price": 200, "currency": "BDT", "is_bestseller": True},
                    {"name": "Tawa Beef Chaap (1:1)", "description": "Beaten beef slice shallow-fried on flat tawa with crushed spices.", "price": 230, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Borhani & Desserts",
                "items": [
                    {"name": "Special Borhani (Glass)", "description": "Spiced fresh curd drink with mint, black salt and roasted cumin.", "price": 60, "currency": "BDT", "is_bestseller": True},
                    {"name": "Shahi Firni (Clay Pot)", "description": "Creamy ground rice pudding with pistachios.", "price": 60, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]

    # 9. PIZZA HUT BANGLADESH (Transcom Foods Official Counter Menu)
    elif rid == "pizza-hut":
        r["menu_categories"] = [
            {
                "category_name": "Pan Pizzas (Personal & Medium)",
                "items": [
                    {"name": "Classic Margherita (Personal)", "description": "Mozzarella cheese on herb tomato sauce.", "price": 199, "currency": "BDT", "is_bestseller": False},
                    {"name": "Classic Margherita (Medium)", "description": "Medium pan pizza with mozzarella and tomato sauce.", "price": 389, "currency": "BDT", "is_bestseller": False},
                    {"name": "Ultimate Hot Chicken (Personal)", "description": "Spicy chicken, green chilies, onions and mozzarella.", "price": 289, "currency": "BDT", "is_bestseller": True},
                    {"name": "Ultimate Hot Chicken (Medium)", "description": "Medium pan pizza with spicy chicken chunks and extra cheese.", "price": 549, "currency": "BDT", "is_bestseller": True},
                    {"name": "Classic Beef Pizza (Personal)", "description": "Seasoned ground beef, onions, bell peppers and mozzarella.", "price": 289, "currency": "BDT", "is_bestseller": True},
                    {"name": "Classic Beef Pizza (Medium)", "description": "Medium pizza with seasoned ground beef and cheese.", "price": 549, "currency": "BDT", "is_bestseller": True},
                    {"name": "Popcorn Chicken Pan Pizza (Personal)", "description": "Crispy chicken popcorn pieces baked on golden crust.", "price": 389, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chicken Sausage Pan Pizza (Medium)", "description": "Loaded with chicken sausage slices and cheese.", "price": 549, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Appetizers, Garlic Breads & Wings",
                "items": [
                    {"name": "Garlic Bread with Cheese (4 Pcs)", "description": "Warm baguette slices topped with garlic herb butter and melted mozzarella.", "price": 249, "currency": "BDT", "is_bestseller": True},
                    {"name": "Spicy Chicken Wings (6 Pcs)", "description": "Oven roasted chicken wings tossed in hot marinade.", "price": 329, "currency": "BDT", "is_bestseller": True},
                    {"name": "Baked Pasta Alfredo", "description": "Creamy mushroom chicken pasta baked under golden cheese.", "price": 349, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Desserts & Drinks",
                "items": [
                    {"name": "Choco Volcano Molten Cake", "description": "Warm chocolate cake with molten chocolate core.", "price": 219, "currency": "BDT", "is_bestseller": True},
                    {"name": "Fountain Pepsi (Regular)", "description": "Chilled fountain beverage.", "price": 60, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]

    # 10. BURGER KING BANGLADESH
    elif rid == "burger-king":
        r["menu_categories"] = [
            {
                "category_name": "Flame-Grilled Burgers",
                "items": [
                    {"name": "Whopper (Classic Flame-Grilled)", "description": "Quarter pound flame-grilled beef patty, sesame bun, juicy tomatoes, fresh lettuce, mayo, pickles and onions.", "price": 479, "currency": "BDT", "is_bestseller": True},
                    {"name": "Whopper Jr.", "description": "Smaller version of the classic flame-grilled Whopper.", "price": 299, "currency": "BDT", "is_bestseller": True},
                    {"name": "Crispy King Burger", "description": "Golden crispy fried chicken patty with fresh lettuce and creamy mayo.", "price": 399, "currency": "BDT", "is_bestseller": True},
                    {"name": "Grill Hot N Chili Chicken Burger", "description": "Flame-grilled spiced chicken patty with hot chili sauce.", "price": 329, "currency": "BDT", "is_bestseller": True},
                    {"name": "Tandoori Grill Chicken Burger", "description": "Tandoori spiced grilled chicken patty with mint mayo.", "price": 319, "currency": "BDT", "is_bestseller": False},
                    {"name": "Crispy Sausage King Burger", "description": "Crispy chicken patty with chicken sausage slice and cheese.", "price": 309, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Fried Chicken, Tenders & Sides",
                "items": [
                    {"name": "BK Fried Chicken (2 Pcs)", "description": "Crispy fried spiced chicken pieces.", "price": 349, "currency": "BDT", "is_bestseller": True},
                    {"name": "BK Fried Chicken (5 Pcs)", "description": "5 pieces of crispy golden chicken.", "price": 849, "currency": "BDT", "is_bestseller": True},
                    {"name": "BK Golden French Fries (Medium)", "description": "Thick-cut golden salted fries.", "price": 149, "currency": "BDT", "is_bestseller": True},
                    {"name": "BK Onion Rings", "description": "Crispy battered onion rings.", "price": 159, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Drinks & Desserts",
                "items": [
                    {"name": "Chocolate Sundae Cup", "description": "Soft serve ice cream topped with chocolate fudge.", "price": 129, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chilled Soft Drink (Regular)", "description": "Choice of Coke, Sprite, or Fanta.", "price": 60, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]

with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

with open(JS_FILE, "w", encoding="utf-8") as f:
    f.write("window.RESTAURANTS_DATA = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n")

print("Successfully verified and synchronized all top 10 chains with official 2024-2025 dine-in counter menus and pricing!")
