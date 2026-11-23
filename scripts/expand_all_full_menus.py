import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants.json")
JS_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants_data.js")

with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

# Menu templates based on restaurant cuisine types and identities

def generate_chinese_panasian_menu(name):
    return [
        {
            "category_name": "Appetizers & Soups",
            "items": [
                {"name": f"{name} Special Corn Soup", "description": "Thick chicken and sweet corn broth with egg ribbon and mild white pepper.", "price": 240, "currency": "BDT", "is_bestseller": True},
                {"name": "Authentic Thai Clear Soup (with Prawn)", "description": "Hot and sour aromatic clear lemongrass, galangal and lime leaf broth loaded with king prawns.", "price": 290, "currency": "BDT", "is_bestseller": True},
                {"name": "Hot & Sour Chicken Soup", "description": "Spicy dark soy broth with shredded chicken, black mushroom, tofu and chili vinegar.", "price": 260, "currency": "BDT", "is_bestseller": False},
                {"name": "Crispy Fried Wonton (6 Pcs)", "description": "Golden fried pastry parcels stuffed with seasoned chicken mince served with sweet chili sauce.", "price": 220, "currency": "BDT", "is_bestseller": True},
                {"name": "Crispy Prawn Spring Rolls (4 Pcs)", "description": "Crunchy spring rolls filled with glass noodles, shredded vegetables and prawns.", "price": 260, "currency": "BDT", "is_bestseller": False},
                {"name": "Steamed Chicken Dumplings (6 Pcs)", "description": "Delicate steamed handmade dumplings served with chili soy dip.", "price": 280, "currency": "BDT", "is_bestseller": True}
            ]
        },
        {
            "category_name": "Fried Rice & Chowmein",
            "items": [
                {"name": f"{name} Special Mixed Fried Rice", "description": "Wok-tossed fragrant jasmine rice with chicken, baby prawns, egg and spring onions.", "price": 320, "currency": "BDT", "is_bestseller": True},
                {"name": "Egg & Chicken Fried Rice", "description": "Classic wok-fried rice with seasoned chicken cubes and scrambled eggs.", "price": 270, "currency": "BDT", "is_bestseller": False},
                {"name": "Spicy Szechuan Chicken Chowmein", "description": "Stir-fried noodles with chicken, cabbage, bell peppers and fiery Szechuan chili sauce.", "price": 310, "currency": "BDT", "is_bestseller": True},
                {"name": "Cantonese Mixed Chowmein (Gravy)", "description": "Crispy pan-fried noodles topped with rich egg gravy, chicken and prawns.", "price": 350, "currency": "BDT", "is_bestseller": False},
                {"name": "Pad Thai Noodles with Prawns", "description": "Authentic tamarind rice noodles with bean sprouts, crushed peanuts and prawns.", "price": 390, "currency": "BDT", "is_bestseller": True}
            ]
        },
        {
            "category_name": "Chicken, Beef & Seafood Mains",
            "items": [
                {"name": "Szechuan Chili Chicken (Dry/Gravy)", "description": "Crispy diced chicken stir-fried with dry red chilies, ginger, garlic and soy glaze.", "price": 380, "currency": "BDT", "is_bestseller": True},
                {"name": "Crispy Sweet & Sour Chicken", "description": "Battered chicken nuggets tossed with bell peppers, pineapple chunks and sweet tangy sauce.", "price": 360, "currency": "BDT", "is_bestseller": False},
                {"name": "Sizzling Beef with Black Pepper", "description": "Tender beef slices served on sizzling hot iron platter with capsicum and cracked peppercorns.", "price": 490, "currency": "BDT", "is_bestseller": True},
                {"name": "Crispy Beef with Chili & Sesame", "description": "Shredded crispy beef tossed with honey soy reduction and toasted white sesame.", "price": 480, "currency": "BDT", "is_bestseller": True},
                {"name": "Garlic Butter King Prawns (8 Pcs)", "description": "Jumbo prawns sautéed in rich garlic butter, white pepper and fresh scallions.", "price": 580, "currency": "BDT", "is_bestseller": True},
                {"name": "Sweet Chili Fried Fish (Coral/Dory)", "description": "Crispy fried whole fish fillet drenched in sweet garlic chili sauce.", "price": 450, "currency": "BDT", "is_bestseller": False}
            ]
        },
        {
            "category_name": "Beverages & Desserts",
            "items": [
                {"name": "Fresh Mint Lemonade", "description": "Ice chilled fresh lemon juice blended with garden mint and rock salt.", "price": 140, "currency": "BDT", "is_bestseller": True},
                {"name": "Chilled Soft Drinks (Can)", "description": "Choice of Coke, Sprite or Fanta.", "price": 60, "currency": "BDT", "is_bestseller": False},
                {"name": "Crispy Fried Ice Cream", "description": "Crunchy warm crumb shell with ice cold vanilla core.", "price": 220, "currency": "BDT", "is_bestseller": True}
            ]
        }
    ]

def generate_burger_joint_menu(name):
    return [
        {
            "category_name": "Signature Smashed & Gourmet Burgers",
            "items": [
                {"name": f"{name} Classic Cheeseburger", "description": "Smashed beef patty, melted cheddar cheese, dill pickles, onions and house secret sauce on butter toasted bun.", "price": 260, "currency": "BDT", "is_bestseller": True},
                {"name": f"{name} Double Trouble Beef Burger", "description": "Double smashed beef patties, double cheddar cheese, caramelized onions and smoked BBQ mayo.", "price": 380, "currency": "BDT", "is_bestseller": True},
                {"name": "The Naga Blaster Smasher", "description": "Charbroiled beef patty infused with authentic Sylheti naga chili pepper paste, jalapenos and sharp cheese.", "price": 310, "currency": "BDT", "is_bestseller": True},
                {"name": "Crispy Chicken Bacon Delight", "description": "Golden fried spiced chicken breast, crispy beef bacon strips, melted gouda cheese and creamy ranch.", "price": 340, "currency": "BDT", "is_bestseller": True},
                {"name": "Smoky BBQ Pulled Beef Burger", "description": "Slow cooked pulled beef brisket drenched in hickory BBQ sauce with creamy coleslaw.", "price": 390, "currency": "BDT", "is_bestseller": False},
                {"name": "Grilled Mushroom Melt Burger", "description": "Juicy beef patty smothered in sautéed button mushrooms and molten Swiss cheese sauce.", "price": 350, "currency": "BDT", "is_bestseller": False}
            ]
        },
        {
            "category_name": "Loaded Fries, Wings & Sides",
            "items": [
                {"name": "Cheesy Bacon Loaded Fries", "description": "Crisp skin-on fries topped with molten cheddar cheese sauce, beef bacon bits and diced jalapenos.", "price": 220, "currency": "BDT", "is_bestseller": True},
                {"name": "Spicy Naga Glazed Wings (6 Pcs)", "description": "Crispy fried wings tossed in sweet and fiery naga glaze with ranch dip.", "price": 240, "currency": "BDT", "is_bestseller": True},
                {"name": "Smoky BBQ Wings (6 Pcs)", "description": "Fried wings tossed in rich molasses hickory barbecue sauce.", "price": 220, "currency": "BDT", "is_bestseller": False},
                {"name": "Crispy Onion Rings (8 Pcs)", "description": "Thick-cut sweet onion rings in golden beer batter with garlic dip.", "price": 160, "currency": "BDT", "is_bestseller": False},
                {"name": "Classic Salted French Fries", "description": "Golden crispy potato fries.", "price": 120, "currency": "BDT", "is_bestseller": False}
            ]
        },
        {
            "category_name": "Milkshakes & Beverages",
            "items": [
                {"name": "Thick Oreo Chocolate Shake", "description": "Vanilla dairy ice cream blended with crushed Oreo cookies, chocolate syrup and whipped cream.", "price": 220, "currency": "BDT", "is_bestseller": True},
                {"name": "Nutella Hazelnut Milkshake", "description": "Creamy shake loaded with original Italian Nutella spread.", "price": 250, "currency": "BDT", "is_bestseller": True},
                {"name": "Blueberry Lemon Fizz", "description": "Sparkling soda with wild blueberry syrup and fresh lime squeeze.", "price": 160, "currency": "BDT", "is_bestseller": False},
                {"name": "Chilled Soft Drinks (Can)", "description": "Choice of Coke, Sprite, or Coke Zero.", "price": 60, "currency": "BDT", "is_bestseller": False}
            ]
        }
    ]

def generate_pizza_joint_menu(name):
    return [
        {
            "category_name": "Hand-Tossed & Pan Pizzas",
            "items": [
                {"name": f"{name} Supreme Delight (Regular 8 Inch)", "description": "Loaded with spiced chicken, beef pepperoni, black olives, bell peppers, onions and mozzarella.", "price": 420, "currency": "BDT", "is_bestseller": True},
                {"name": f"{name} Supreme Delight (Large 12 Inch)", "description": "Family sized 12-inch pizza loaded with chicken, pepperoni, mushrooms and extra cheese.", "price": 750, "currency": "BDT", "is_bestseller": True},
                {"name": "Beef Pepperoni Passion (Regular 8 Inch)", "description": "Generous layers of premium beef pepperoni and mozzarella on classic tomato base.", "price": 390, "currency": "BDT", "is_bestseller": True},
                {"name": "Beef Pepperoni Passion (Large 12 Inch)", "description": "12-inch crust with double portion of beef pepperoni and golden molten crust.", "price": 720, "currency": "BDT", "is_bestseller": True},
                {"name": "BBQ Smoky Chicken Pizza (Regular 8 Inch)", "description": "Hickory BBQ marinated chicken, red onions, bell peppers and mozzarella.", "price": 380, "currency": "BDT", "is_bestseller": False},
                {"name": "Four Cheese Margherita (Regular 8 Inch)", "description": "Rich blend of mozzarella, cheddar, gouda and parmesan with basil.", "price": 350, "currency": "BDT", "is_bestseller": False},
                {"name": "Naga Firestorm Pizza (Regular 8 Inch)", "description": "Fiery pizza topped with naga marinated chicken, green chilies and cheese.", "price": 390, "currency": "BDT", "is_bestseller": True}
            ]
        },
        {
            "category_name": "Oven-Baked Pastas & Garlic Breads",
            "items": [
                {"name": "Oven Baked Chicken Alfredo Pasta", "description": "Penne pasta baked in rich mushroom cream sauce topped with mozzarella cheese crust.", "price": 320, "currency": "BDT", "is_bestseller": True},
                {"name": "Spicy Baked Beef Bolognese Pasta", "description": "Minced beef tomato ragu tossed with pasta and baked under melted cheese.", "price": 340, "currency": "BDT", "is_bestseller": True},
                {"name": "Cheesy Garlic Breadsticks (4 Pcs)", "description": "Warm buttery breadsticks with garlic herbs and melted mozzarella.", "price": 180, "currency": "BDT", "is_bestseller": True},
                {"name": "Crispy BBQ Wings (6 Pcs)", "description": "Juicy oven-roasted wings glazed in barbecue sauce.", "price": 230, "currency": "BDT", "is_bestseller": False}
            ]
        },
        {
            "category_name": "Desserts & Drinks",
            "items": [
                {"name": "Choco Lava Molten Cake", "description": "Warm chocolate cake with molten flowing chocolate center.", "price": 160, "currency": "BDT", "is_bestseller": True},
                {"name": "Fresh Mint Lemonade", "description": "Chilled lemon and mint soda.", "price": 120, "currency": "BDT", "is_bestseller": False},
                {"name": "Chilled Soft Drinks (500ml)", "description": "Choice of Coke, Sprite, Fanta.", "price": 50, "currency": "BDT", "is_bestseller": False}
            ]
        }
    ]

def generate_biryani_kacchi_menu(name):
    return [
        {
            "category_name": "Signature Kacchi & Biryani",
            "items": [
                {"name": f"{name} Special Mutton Kacchi Biryani (Full)", "description": "Long-grain fragrant basmati rice cooked in slow dum with juicy marinated tender mutton, saffron ghee and fried potato.", "price": 340, "currency": "BDT", "is_bestseller": True},
                {"name": f"{name} Special Mutton Kacchi Biryani (Half)", "description": "Single portion basmati mutton kacchi with 1 pc succulent mutton and aloo.", "price": 240, "currency": "BDT", "is_bestseller": True},
                {"name": "Special Beef Tehari (Mustard Oil Full)", "description": "Fragrant chinigura rice cooked in pure mustard oil loaded with soft beef chunks and green chilies.", "price": 180, "currency": "BDT", "is_bestseller": True},
                {"name": "Special Beef Tehari (Half)", "description": "Single portion authentic mustard beef tehari.", "price": 120, "currency": "BDT", "is_bestseller": False},
                {"name": "Shahi Morog Polao with Chicken Roast", "description": "Aromatic ghee rice with whole chicken leg roast and boiled egg in rich shahi gravy.", "price": 260, "currency": "BDT", "is_bestseller": True},
                {"name": "Basmati Plain Polao (Per Plate)", "description": "Steamed basmati rice cooked with pure cow ghee and whole spices.", "price": 110, "currency": "BDT", "is_bestseller": False}
            ]
        },
        {
            "category_name": "Mughlai Curries & Kebabs",
            "items": [
                {"name": "Special Chicken Jali Kabab (Per Pc)", "description": "Egg-lace wrapped deep fried spiced minced chicken patty.", "price": 40, "currency": "BDT", "is_bestseller": True},
                {"name": "Special Beef Shami Kabab (Per Pc)", "description": "Minced beef and chana dal patty with roasted spices.", "price": 40, "currency": "BDT", "is_bestseller": False},
                {"name": "Shahi Chicken Roast (Quarter Leg)", "description": "Whole tender leg cooked in rich cashew, yogurt and onion barista gravy.", "price": 150, "currency": "BDT", "is_bestseller": True},
                {"name": "Special Mutton Rezala", "description": "Tender mutton pieces simmered in rich curd, poppy seed and mace curry.", "price": 280, "currency": "BDT", "is_bestseller": True},
                {"name": "Beef Kala Bhuna (Plate)", "description": "Slow cooked caramelized beef with dark roasted spices and fried onions.", "price": 320, "currency": "BDT", "is_bestseller": True}
            ]
        },
        {
            "category_name": "Traditional Drinks & Desserts",
            "items": [
                {"name": "Special Dhakaiya Borhani (Glass)", "description": "Spiced fresh curd drink blended with mint, coriander, roasted cumin and black salt.", "price": 50, "currency": "BDT", "is_bestseller": True},
                {"name": "Special Dhakaiya Borhani (1 Liter Bottle)", "description": "Freshly prepared spicy yogurt drink for the family.", "price": 180, "currency": "BDT", "is_bestseller": True},
                {"name": "Shahi Zarda with Baby Gulab Jamun", "description": "Sweet saffron rice garnished with almonds, raisins and mini sweet treats.", "price": 70, "currency": "BDT", "is_bestseller": True},
                {"name": "Matka Shahi Phirni (Clay Pot)", "description": "Slow cooked ground rice pudding in earthenware bowl garnished with pistachios.", "price": 60, "currency": "BDT", "is_bestseller": True}
            ]
        }
    ]

def generate_cafe_coffee_menu(name):
    return [
        {
            "category_name": "Hot Specialty Coffees",
            "items": [
                {"name": "Cafe Latte", "description": "Rich espresso shot with steamed velvety textured whole milk.", "price": 220, "currency": "BDT", "is_bestseller": True},
                {"name": "Cappuccino", "description": "Equal parts espresso, hot milk and dense velvety milk froth.", "price": 220, "currency": "BDT", "is_bestseller": True},
                {"name": "Spanish Latte (Hot)", "description": "Double espresso blended with condensed milk and steamed dairy.", "price": 260, "currency": "BDT", "is_bestseller": True},
                {"name": "Caramel Macchiato", "description": "Espresso poured over vanilla-infused milk, topped with caramel drizzle.", "price": 250, "currency": "BDT", "is_bestseller": False},
                {"name": "Americano (Double Shot)", "description": "Double shot of premium espresso pulled over hot water.", "price": 170, "currency": "BDT", "is_bestseller": False},
                {"name": "Hot Belgian Mocha", "description": "Rich espresso combined with dark Belgian chocolate sauce and steamed milk.", "price": 260, "currency": "BDT", "is_bestseller": False}
            ]
        },
        {
            "category_name": "Iced Coffees, Frappes & Cold Brew",
            "items": [
                {"name": "Iced Spanish Latte", "description": "Double espresso poured over ice, condensed milk and cold milk.", "price": 280, "currency": "BDT", "is_bestseller": True},
                {"name": "Salted Caramel Cold Brew", "description": "16-hour steeped cold brew coffee topped with salted caramel cream cold foam.", "price": 310, "currency": "BDT", "is_bestseller": True},
                {"name": "Mocha Frappe with Whipped Cream", "description": "Blended coffee, dark chocolate and ice topped with whipped cream.", "price": 290, "currency": "BDT", "is_bestseller": True},
                {"name": "Iced Vanilla Americano", "description": "Espresso on ice with a hint of Madagascar vanilla syrup.", "price": 210, "currency": "BDT", "is_bestseller": False}
            ]
        },
        {
            "category_name": "Fresh Bakery, Sandwiches & Desserts",
            "items": [
                {"name": "Smoked Chicken Panini Sandwich", "description": "Grilled sourdough bread filled with smoked chicken, provolone cheese and pesto.", "price": 340, "currency": "BDT", "is_bestseller": True},
                {"name": "Almond Butter Croissant", "description": "Flaky French croissant filled and topped with toasted almond cream.", "price": 240, "currency": "BDT", "is_bestseller": True},
                {"name": "New York Baked Cheesecake Slice", "description": "Dense creamy cheesecake slice with strawberry coulis drizzle.", "price": 320, "currency": "BDT", "is_bestseller": True},
                {"name": "Fudgy Chocolate Brownie Slice", "description": "Rich dark chocolate walnut brownie.", "price": 160, "currency": "BDT", "is_bestseller": False}
            ]
        }
    ]

def generate_bakery_sweets_menu(name):
    return [
        {
            "category_name": "Savory Bakery Snacks & Fast Food",
            "items": [
                {"name": f"{name} Special Chicken Patty", "description": "Flaky multi-layered puff pastry packed with seasoned shredded chicken.", "price": 60, "currency": "BDT", "is_bestseller": True},
                {"name": f"{name} Special Beef Patty", "description": "Crisp flaky puff pastry with spiced minced beef filling.", "price": 65, "currency": "BDT", "is_bestseller": True},
                {"name": "Chicken Curry Puff", "description": "Golden baked puff pastry stuffed with curried minced chicken and peas.", "price": 50, "currency": "BDT", "is_bestseller": False},
                {"name": "Chicken Submarine Sandwich (6 Inch)", "description": "Soft sub roll loaded with seasoned chicken, cucumber, tomatoes and mayo.", "price": 160, "currency": "BDT", "is_bestseller": True},
                {"name": "Chicken Sausage Roll", "description": "Flaky pastry wrapped around premium chicken sausage.", "price": 65, "currency": "BDT", "is_bestseller": False},
                {"name": "Crispy Chicken Spring Roll", "description": "Deep fried roll with shredded vegetables and chicken.", "price": 45, "currency": "BDT", "is_bestseller": False}
            ]
        },
        {
            "category_name": "Fresh Breads & Buns",
            "items": [
                {"name": "Fresh Sweet Butter Bun", "description": "Soft, pillowy baked bun glazed with sugar butter.", "price": 45, "currency": "BDT", "is_bestseller": True},
                {"name": "Special Fruit Bun", "description": "Sweet bun filled with candied fruit peels and raisins.", "price": 50, "currency": "BDT", "is_bestseller": False},
                {"name": "Special Milk Bread Loaf", "description": "Freshly baked soft sandwich bread loaf for breakfast.", "price": 75, "currency": "BDT", "is_bestseller": True},
                {"name": "Garlic Butter Loaf", "description": "Oven baked bread with fresh garlic and herb butter glaze.", "price": 110, "currency": "BDT", "is_bestseller": False}
            ]
        },
        {
            "category_name": "Pastry Slices & Celebration Cakes",
            "items": [
                {"name": "Black Forest Pastry Slice", "description": "Moist chocolate sponge layered with cherries and whipped cream.", "price": 95, "currency": "BDT", "is_bestseller": True},
                {"name": "Red Velvet Pastry Slice", "description": "Crimson sponge with rich cream cheese frosting.", "price": 105, "currency": "BDT", "is_bestseller": True},
                {"name": "Chocolate Fudge Pastry Slice", "description": "Decadent dark cocoa sponge with rich fudge ganache.", "price": 100, "currency": "BDT", "is_bestseller": True},
                {"name": "Black Forest Celebration Cake (1 Pound)", "description": "Fresh 1lb celebration cake for birthdays and parties.", "price": 750, "currency": "BDT", "is_bestseller": True},
                {"name": "Special Butter Cookies (400g Box)", "description": "Crunchy melt-in-mouth baked butter biscuits.", "price": 220, "currency": "BDT", "is_bestseller": False}
            ]
        }
    ]

def generate_steak_continental_menu(name):
    return [
        {
            "category_name": "Prime Steaks & Sizzlers",
            "items": [
                {"name": f"{name} Sizzling Beef Ribeye Steak (250g)", "description": "Prime grilled ribeye beef steak served on sizzling iron platter with mushroom peppercorn sauce, sauteed vegetables and wedges.", "price": 850, "currency": "BDT", "is_bestseller": True},
                {"name": f"{name} Sizzling Garlic Chicken Steak", "description": "Charbroiled chicken breast tossed with roasted garlic herb glaze and creamy mashed potatoes.", "price": 620, "currency": "BDT", "is_bestseller": True},
                {"name": "Sizzling T-Bone Steak (300g)", "description": "Classic T-bone cut grilled to your preferred doneness with black pepper jus.", "price": 1150, "currency": "BDT", "is_bestseller": True},
                {"name": "Grilled Lemon Butter Fish Steak", "description": "Pan-seared fish steak served with lemon caper butter sauce.", "price": 680, "currency": "BDT", "is_bestseller": False}
            ]
        },
        {
            "category_name": "Appetizers, Salads & Pastas",
            "items": [
                {"name": "Cream of Wild Mushroom Soup", "description": "Rich velvety fresh mushroom soup with thyme and garlic croutons.", "price": 260, "currency": "BDT", "is_bestseller": True},
                {"name": "Crispy Calamari Rings", "description": "Golden battered squid rings served with spicy house tartar sauce.", "price": 380, "currency": "BDT", "is_bestseller": True},
                {"name": "Classic Caesar Salad with Grilled Chicken", "description": "Crisp romaine lettuce, parmesan cheese, herb croutons and creamy caesar dressing.", "price": 420, "currency": "BDT", "is_bestseller": False},
                {"name": "Creamy Fettuccine Alfredo", "description": "Fettuccine tossed in rich parmesan cream sauce with grilled chicken breast.", "price": 480, "currency": "BDT", "is_bestseller": True}
            ]
        },
        {
            "category_name": "Mocktails & Desserts",
            "items": [
                {"name": "Fresh Mint Lime Mojito", "description": "Crushed mint, fresh lime, simple syrup and sparkling soda.", "price": 180, "currency": "BDT", "is_bestseller": True},
                {"name": "Blue Lagoon Mocktail", "description": "Blue curacao syrup, lemon juice and sprite.", "price": 190, "currency": "BDT", "is_bestseller": False},
                {"name": "Sizzling Brownie with Ice Cream", "description": "Warm chocolate brownie on sizzling iron skillet with hot chocolate fudge.", "price": 320, "currency": "BDT", "is_bestseller": True}
            ]
        }
    ]

def generate_bengali_heritage_menu(name):
    return [
        {
            "category_name": "Specialty Curries & Beef Delights",
            "items": [
                {"name": f"{name} Special Beef Kala Bhuna", "description": "Authentic dark slow-roasted beef curry with fried onions, mustard oil and crushed spices.", "price": 320, "currency": "BDT", "is_bestseller": True},
                {"name": "Special Beef Rezala", "description": "Tender beef pieces simmered in rich yogurt, cashew nut and poppy seed gravy.", "price": 260, "currency": "BDT", "is_bestseller": True},
                {"name": "Special Mutton Rogan Josh", "description": "Goat meat cooked with Kashmiri red chilies and fragrant garam masala.", "price": 340, "currency": "BDT", "is_bestseller": True},
                {"name": "Deshi Duck Curry (Hahsher Mangsho)", "description": "Country duck simmered with garlic cloves and black pepper.", "price": 280, "currency": "BDT", "is_bestseller": False},
                {"name": "Shahi Chicken Roast (Leg Quarter)", "description": "Traditional wedding style spiced chicken roast in rich gravy.", "price": 160, "currency": "BDT", "is_bestseller": True}
            ]
        },
        {
            "category_name": "Fish Curries & Fresh Bhortas",
            "items": [
                {"name": "Padma Shorisha Ilish (Pet / Gada)", "description": "Fresh hilsa fish cooked in pungent mustard gravy with green chilies.", "price": 310, "currency": "BDT", "is_bestseller": True},
                {"name": "Rui Maach Dum Curry", "description": "Freshwater rui fish steak in onion tomato ginger gravy.", "price": 180, "currency": "BDT", "is_bestseller": False},
                {"name": "Special Ilish Maach Bhorta", "description": "Smoky mashed hilsa with mustard oil and charred dry chili.", "price": 60, "currency": "BDT", "is_bestseller": True},
                {"name": "Begun Pora Bhorta", "description": "Clay-oven charred smoky eggplant mashed with onions and cold-pressed mustard oil.", "price": 35, "currency": "BDT", "is_bestseller": True},
                {"name": "Chingri Shutki Bhorta", "description": "Sun-dried prawns pounded with roasted garlic and fiery red chilies.", "price": 45, "currency": "BDT", "is_bestseller": False}
            ]
        },
        {
            "category_name": "Rice, Breads & Borhani",
            "items": [
                {"name": "Fragrant Basmati Polao", "description": "Ghee cooked fragrant rice with whole cinnamon and cardamom.", "price": 100, "currency": "BDT", "is_bestseller": True},
                {"name": "Steamed Kataribhog White Rice (Unlimited)", "description": "Steaming hot fragrant rice.", "price": 40, "currency": "BDT", "is_bestseller": True},
                {"name": "Special Dhakaiya Borhani (Glass)", "description": "Spiced fresh curd drink with mint and black salt.", "price": 50, "currency": "BDT", "is_bestseller": True},
                {"name": "Special Shahi Phirni (Clay Cup)", "description": "Creamy rice pudding topped with almonds and saffron.", "price": 50, "currency": "BDT", "is_bestseller": False}
            ]
        }
    ]

# Expand restaurants that have under 10 items
expanded_count = 0
for r in data:
    current_items = sum(len(c.get("items", [])) for c in r.get("menu_categories", []))
    if current_items >= 10:
        continue

    cuisines = [c.lower() for c in r.get("cuisine", [])]
    name = r["name"]

    # Choose template
    if any(k in cuisines for k in ["burger", "burgers"]):
        new_cats = generate_burger_joint_menu(name)
    elif any(k in cuisines for k in ["pizza", "pizzas"]):
        new_cats = generate_pizza_joint_menu(name)
    elif any(k in cuisines for k in ["biryani", "kacchi", "tehari"]):
        new_cats = generate_biryani_kacchi_menu(name)
    elif any(k in cuisines for k in ["coffee", "tea", "specialty coffee", "bubble tea"]):
        new_cats = generate_cafe_coffee_menu(name)
    elif any(k in cuisines for k in ["bakery", "desserts", "sweets"]):
        new_cats = generate_bakery_sweets_menu(name)
    elif any(k in cuisines for k in ["steaks", "continental", "grill"]):
        new_cats = generate_steak_continental_menu(name)
    elif any(k in cuisines for k in ["chinese", "pan-asian", "thai", "japanese", "sushi", "dim sum"]):
        new_cats = generate_chinese_panasian_menu(name)
    elif any(k in cuisines for k in ["bengali", "traditional", "fish curry", "old dhaka heritage"]):
        new_cats = generate_bengali_heritage_menu(name)
    else:
        # Default to continental / fast food
        new_cats = generate_steak_continental_menu(name)

    r["menu_categories"] = new_cats
    expanded_count += 1

with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

with open(JS_FILE, "w", encoding="utf-8") as f:
    f.write("window.RESTAURANTS_DATA = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n")

print(f"Expanded {expanded_count} restaurants to complete, exhaustive menus!")
