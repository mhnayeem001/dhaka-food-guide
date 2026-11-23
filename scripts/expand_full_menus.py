import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants.json")

with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

for r in data:
    rid = r["id"]

    # PIZZABURG
    if rid == "pizzaburg":
        r["menu_categories"] = [
            {
                "category_name": "Signature Pizzas (8\" / 12\")",
                "items": [
                    {"name": "Meaty Onion Pizza", "description": "Double beef pepperoni, seasoned chicken, fresh red onion, secret marinara and melted mozzarella.", "price": 389, "currency": "BDT", "sizes": [{"size": "8 inch", "price": 389}, {"size": "12 inch", "price": 689}], "is_bestseller": True},
                    {"name": "BBQ Temptation Pizza", "description": "Smoky BBQ chicken, roasted capsicum, sweet corn, mushrooms and thick layer of mozzarella.", "price": 419, "currency": "BDT", "sizes": [{"size": "8 inch", "price": 419}, {"size": "12 inch", "price": 729}], "is_bestseller": True},
                    {"name": "Naga Feast Pizza (Super Spicy)", "description": "Fiery Sylheti Naga chili infused chicken chunks, red paprika, jalapenos and mozzarella.", "price": 429, "currency": "BDT", "sizes": [{"size": "8 inch", "price": 429}, {"size": "12 inch", "price": 749}], "is_bestseller": True},
                    {"name": "Four Seasons Pizza", "description": "Quarter beef pepperoni, quarter mushroom, quarter chicken sausage, quarter loaded four-cheese.", "price": 449, "currency": "BDT", "sizes": [{"size": "8 inch", "price": 449}, {"size": "12 inch", "price": 769}], "is_bestseller": False},
                    {"name": "Beef Delight Pizza", "description": "Ground seasoned beef, beef bacon rashers, black olives, onions and melted cheese.", "price": 429, "currency": "BDT", "sizes": [{"size": "8 inch", "price": 429}, {"size": "12 inch", "price": 749}], "is_bestseller": False},
                    {"name": "Sausage Carnival Pizza", "description": "Sliced chicken and beef sausages, bell peppers, tomatoes and mozzarella.", "price": 379, "currency": "BDT", "sizes": [{"size": "8 inch", "price": 379}, {"size": "12 inch", "price": 669}], "is_bestseller": False},
                    {"name": "Mushroom & Cheese Pizza", "description": "Sautéed fresh button mushrooms, garlic butter drizzle and double mozzarella cheese.", "price": 369, "currency": "BDT", "sizes": [{"size": "8 inch", "price": 369}, {"size": "12 inch", "price": 649}], "is_bestseller": False},
                    {"name": "Vegetarian Supreme Pizza", "description": "Sweet corn, bell peppers, black olives, red onions, tomatoes and cheese.", "price": 349, "currency": "BDT", "sizes": [{"size": "8 inch", "price": 349}, {"size": "12 inch", "price": 599}], "is_bestseller": False}
                ]
            },
            {
                "category_name": "Loaded Burgers",
                "items": [
                    {"name": "Smokey BBQ Beef Burger", "description": "Charbroiled beef patty coated in smoky BBQ sauce, cheddar cheese slice, lettuce and garlic mayo.", "price": 249, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chicken Cheese Blast Burger", "description": "Deep-fried chicken patty stuffed with molten cheese, topped with extra cheddar slice.", "price": 289, "currency": "BDT", "is_bestseller": True},
                    {"name": "Double Decker Monster Burger", "description": "Two hearty beef or chicken patties, double cheese, caramelized onions and house burger sauce.", "price": 369, "currency": "BDT", "is_bestseller": True},
                    {"name": "Classic Beef Burger", "description": "Grilled seasoned beef patty with fresh tomato, lettuce and special sauce.", "price": 199, "currency": "BDT", "is_bestseller": False},
                    {"name": "Classic Crispy Chicken Burger", "description": "Crunchy golden fried chicken patty with tangy mayo and lettuce.", "price": 189, "currency": "BDT", "is_bestseller": False},
                    {"name": "Naga Beef Burger", "description": "Beef patty topped with fiery Naga morich sauce and melted cheese.", "price": 259, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Oven Baked Pastas",
                "items": [
                    {"name": "Oven Baked Creamy White Pasta", "description": "Penne pasta tossed in creamy white mushroom sauce, chicken chunks, baked under golden melted mozzarella.", "price": 329, "currency": "BDT", "is_bestseller": True},
                    {"name": "Oven Baked Spicy Red Pasta", "description": "Penne pasta baked in spicy marinara sauce, chicken chunks and melted cheese.", "price": 319, "currency": "BDT", "is_bestseller": False},
                    {"name": "Oven Baked Naga Pasta", "description": "Fiery naga spiced baked pasta with chicken, sausage and extra cheese crust.", "price": 349, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Wings & Sides",
                "items": [
                    {"name": "Naga Wings (6 Pcs)", "description": "Deep-fried crispy wings tossed in authentic Sylheti Naga glaze.", "price": 239, "currency": "BDT", "is_bestseller": True},
                    {"name": "Smoky BBQ Wings (6 Pcs)", "description": "Crispy chicken wings glazed in sweet & smoky barbecue sauce.", "price": 229, "currency": "BDT", "is_bestseller": False},
                    {"name": "Cheesy Garlic Bread (4 Pcs)", "description": "Warm baguette slices topped with garlic herb butter and melted mozzarella.", "price": 179, "currency": "BDT", "is_bestseller": True},
                    {"name": "French Fries (Large)", "description": "Hot salted crispy potato fries.", "price": 129, "currency": "BDT", "is_bestseller": False},
                    {"name": "Chicken Tenders (5 Pcs)", "description": "Boneless crispy chicken tenders with garlic dip.", "price": 219, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Beverages",
                "items": [
                    {"name": "Coca Cola / Sprite (250ml)", "description": "Chilled soft drink.", "price": 35, "currency": "BDT", "is_bestseller": False},
                    {"name": "Cold Coffee with Ice Cream", "description": "Creamy blended cold coffee topped with vanilla ice cream.", "price": 149, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chocolate Milkshake", "description": "Rich thick chocolate shake.", "price": 159, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]

    # KHAO SAN
    elif rid == "khao-san":
        r["menu_categories"] = [
            {
                "category_name": "Authentic Soups",
                "items": [
                    {"name": "Tom Yum Goong (River Prawn)", "description": "Authentic spicy and sour clear broth with king river prawns, galangal, lemongrass, kaffir lime leaves and straw mushrooms.", "price": 540, "currency": "BDT", "is_bestseller": True},
                    {"name": "Tom Yum Gai (Chicken)", "description": "Spicy lemongrass clear broth with tender sliced chicken and Thai herbs.", "price": 470, "currency": "BDT", "is_bestseller": False},
                    {"name": "Tom Kha Gai (Chicken Coconut Soup)", "description": "Rich coconut milk soup infused with galangal, lemongrass, lime juice and tender chicken.", "price": 490, "currency": "BDT", "is_bestseller": True},
                    {"name": "Seafood Glass Noodle Clear Soup", "description": "Clear aromatic broth with calamari, prawns, glass noodles and cilantro.", "price": 510, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Appetizers & Salads",
                "items": [
                    {"name": "Grilled Chicken Satay with Peanut Dip", "description": "Marinated grilled chicken skewers served with rich traditional peanut-tamarind sauce and cucumber relish.", "price": 420, "currency": "BDT", "is_bestseller": True},
                    {"name": "Crispy Morning Glory with Larb Gai", "description": "Tempura fried crispy water spinach served with spicy minced chicken Thai herb dip.", "price": 460, "currency": "BDT", "is_bestseller": True},
                    {"name": "Thai Fish Cake (Tod Mun Pla)", "description": "Traditional spiced fish patties with red curry paste and sweet chili dip.", "price": 410, "currency": "BDT", "is_bestseller": False},
                    {"name": "Fried Garlic Calamari", "description": "Crispy golden squid rings tossed with roasted garlic and pepper.", "price": 490, "currency": "BDT", "is_bestseller": False},
                    {"name": "Som Tam (Green Papaya Salad)", "description": "Traditional shredded green papaya tossed with lime juice, fish sauce, peanuts and bird's eye chilies.", "price": 380, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chicken Cashew Nut Salad", "description": "Fried chicken chunks tossed with roasted cashew nuts, chili paste, onions and lime dressing.", "price": 450, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Pad Thai & Noodles",
                "items": [
                    {"name": "Classic Pad Thai (Prawn)", "description": "High-wok tossed flat rice noodles with king prawns, egg, tofu, bean sprouts, crushed roasted peanuts and tamarind glaze.", "price": 550, "currency": "BDT", "is_bestseller": True},
                    {"name": "Classic Pad Thai (Chicken)", "description": "Pad Thai noodles with chicken, egg, bean sprouts and roasted peanuts.", "price": 490, "currency": "BDT", "is_bestseller": False},
                    {"name": "Thai Chilli Garlic Noodles", "description": "Spicy egg noodles tossed in high wok with fresh garlic, holy basil and vegetables.", "price": 440, "currency": "BDT", "is_bestseller": True},
                    {"name": "Lad Na Seafood Noodles", "description": "Wide flat rice noodles served under rich savory gravy with mixed seafood.", "price": 530, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Authentic Curries & Mains",
                "items": [
                    {"name": "Thai Green Chicken Curry", "description": "Fragrant green curry paste cooked in pure coconut milk with Thai eggplants, sweet basil and chicken.", "price": 560, "currency": "BDT", "is_bestseller": True},
                    {"name": "Penang Beef Curry", "description": "Thick, rich roasted red curry with tender sliced beef, crushed peanuts and kaffir lime leaf.", "price": 640, "currency": "BDT", "is_bestseller": True},
                    {"name": "Wok Charred Holy Basil Beef", "description": "Sliced tenderloin wok-tossed with fiery red chilies, garlic and fresh Thai basil leaves.", "price": 620, "currency": "BDT", "is_bestseller": True},
                    {"name": "Sweet & Sour Crispy Fish Fillet", "description": "Crispy fish fillet in vibrant sweet and sour pineapple sauce.", "price": 580, "currency": "BDT", "is_bestseller": False},
                    {"name": "Garlic Black Pepper Prawns", "description": "Jumbo prawns stir-fried in aromatic crushed black pepper and garlic sauce.", "price": 690, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Fried Rice & Steamed Rice",
                "items": [
                    {"name": "Thai Basil Fried Rice", "description": "Jasmine rice stir-fried with fragrant holy basil, garlic, bird's eye chilies and minced chicken.", "price": 480, "currency": "BDT", "is_bestseller": True},
                    {"name": "Pineapple Seafood Fried Rice", "description": "Wok fried rice served with prawns, calamari, cashew nuts, raisins and pineapple.", "price": 590, "currency": "BDT", "is_bestseller": True},
                    {"name": "Garlic Egg Fried Rice", "description": "Aromatic wok-charred fried rice with fried garlic and scrambled eggs.", "price": 380, "currency": "BDT", "is_bestseller": False},
                    {"name": "Steamed Thai Jasmine Rice", "description": "Fragrant steamed premium Thai jasmine rice.", "price": 160, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Desserts & Beverages",
                "items": [
                    {"name": "Thai Mango Sticky Rice", "description": "Sweet coconut sticky rice served with fresh ripe mango slices and toasted sesame.", "price": 450, "currency": "BDT", "is_bestseller": True},
                    {"name": "Authentic Thai Iced Milk Tea (Cha Yen)", "description": "Brewed Ceylon tea spiced with star anise, poured over crushed ice and sweetened condensed milk.", "price": 240, "currency": "BDT", "is_bestseller": True},
                    {"name": "Lemongrass Mint Cooler", "description": "Refreshing iced drink made with fresh boiled lemongrass and mint leaves.", "price": 210, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]

    # YUM CHA DISTRICT
    elif rid == "yum-cha-district":
        r["menu_categories"] = [
            {
                "category_name": "Handcrafted Dim Sum & Bao",
                "items": [
                    {"name": "Chicken & Prawn Siu Mai (4 Pcs)", "description": "Steamed open-topped dumplings filled with minced chicken, river prawns, scallions and tobiko.", "price": 395, "currency": "BDT", "is_bestseller": True},
                    {"name": "Spicy Steamed Wontons in Chilli Oil (5 Pcs)", "description": "Silky wontons filled with seasoned chicken, drenched in aromatic Sichuan chili oil and toasted sesame.", "price": 420, "currency": "BDT", "is_bestseller": True},
                    {"name": "Crispy Prawn Cheung Fung", "description": "Golden crispy netted prawn wrapped in delicate steamed rice noodle rolls with sweet soy sauce.", "price": 465, "currency": "BDT", "is_bestseller": True},
                    {"name": "Crystal Prawn Har Gow (4 Pcs)", "description": "Translucent dumpling skins filled with juicy whole prawns and bamboo shoots.", "price": 440, "currency": "BDT", "is_bestseller": True},
                    {"name": "Steamed BBQ Chicken Bao (2 Pcs)", "description": "Fluffy white steamed buns filled with sweet and savory char siu BBQ chicken.", "price": 360, "currency": "BDT", "is_bestseller": False},
                    {"name": "Pan-Fried Chicken Gyoza (4 Pcs)", "description": "Japanese style potstickers with crispy bottom and juicy minced chicken filling.", "price": 380, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Soups",
                "items": [
                    {"name": "Chicken Wonton Clear Soup", "description": "Delicate clear broth with handmade chicken wontons, pak choi and sesame oil.", "price": 430, "currency": "BDT", "is_bestseller": True},
                    {"name": "Hot & Sour Seafood Soup", "description": "Spicy and tangy thick broth with prawns, squid, tofu, mushrooms and egg ribbons.", "price": 460, "currency": "BDT", "is_bestseller": False},
                    {"name": "Mushroom Chicken Ball Soup", "description": "Light aromatic chicken broth with handcrafted chicken balls and shiitake mushrooms.", "price": 430, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Asian Rice Bowls",
                "items": [
                    {"name": "Beef Bulgogi Rice Bowl", "description": "Tender marinated beef slices stir-fried with sesame and onions, served over egg fried rice and vegetables.", "price": 620, "currency": "BDT", "is_bestseller": True},
                    {"name": "Ginger Chicken Rice Bowl", "description": "Wok tossed chicken breast with julienned fresh ginger, scallions and jasmine rice.", "price": 585, "currency": "BDT", "is_bestseller": False},
                    {"name": "Seafood Rice Bowl", "description": "Prawns, calamari and fish tossed in mild savory sauce over egg fried rice.", "price": 625, "currency": "BDT", "is_bestseller": True},
                    {"name": "Sichuan Cashew Chicken Rice Bowl", "description": "Spicy diced chicken with roasted cashews, dry red chilies and Sichuan pepper.", "price": 580, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Wok Tossed Noodles",
                "items": [
                    {"name": "Hot Seafood Noodles", "description": "Flat wheat noodles tossed with prawns, calamari, fish cake and spicy garlic chili paste.", "price": 510, "currency": "BDT", "is_bestseller": True},
                    {"name": "House Special Chicken Noodles", "description": "Egg noodles wok-charred with chicken strips, shredded cabbage and dark soy sauce.", "price": 470, "currency": "BDT", "is_bestseller": False},
                    {"name": "House Special Beef Noodles", "description": "Savory wok noodles with tender sliced beef and spring onions.", "price": 515, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Signature Mains",
                "items": [
                    {"name": "Chicken Nanban", "description": "Crispy fried chicken breast dipped in sweet-sour soy vinegar sauce, topped with house tartar.", "price": 495, "currency": "BDT", "is_bestseller": True},
                    {"name": "Sriracha Chicken & Mushroom", "description": "Crispy chicken bites glazed in creamy spicy sriracha sauce with sautéed mushrooms.", "price": 495, "currency": "BDT", "is_bestseller": False},
                    {"name": "YCD Special Naga Fried Rice", "description": "Signature egg fried rice infused with fiery naga peppers, chicken, beef and shrimp.", "price": 500, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Signature Teas & Coolers",
                "items": [
                    {"name": "Wild Berries & Peach Iced Tea", "description": "Refreshing cold brewed premium black tea infused with natural wild berry and peach compote.", "price": 260, "currency": "BDT", "is_bestseller": True},
                    {"name": "Traditional Jasmine Blossom Tea (Pot)", "description": "Aromatic steamed whole-leaf green tea scented with night-blooming jasmine flowers.", "price": 220, "currency": "BDT", "is_bestseller": False},
                    {"name": "Lychee Sparkler", "description": "Muddled lychees with sparkling soda, mint and lime.", "price": 250, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]

    # SULTAN'S DINE
    elif rid == "sultans-dine":
        r["menu_categories"] = [
            {
                "category_name": "Royal Basmati Kacchi",
                "items": [
                    {"name": "Kacchi Bashmati (Half)", "description": "Fragrant aged Basmati rice cooked with tender marinated mutton pieces and spiced aloo.", "price": 330, "currency": "BDT", "is_bestseller": True},
                    {"name": "Kacchi Bashmati (Full)", "description": "Full generous serving of signature Royal Basmati Mutton Kacchi Biryani.", "price": 535, "currency": "BDT", "is_bestseller": True},
                    {"name": "Kacchi Basmati (1:3 Sharing)", "description": "Generous serving for 3 people with 3 tender mutton portions and aloo.", "price": 1499, "currency": "BDT", "is_bestseller": True},
                    {"name": "Kacchi Basmati (1:5 Feast)", "description": "Grand feast portion for 5 people with 5 mutton portions and 5 spiced potatoes.", "price": 2399, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Wedding Bonanza Platters",
                "items": [
                    {"name": "Wedding Bonanza Platter (Single)", "description": "Full Kacchi with Chicken Roast, Jali Kabab, Beef Rezala, Borhani, Chutney, Salad and choice of Jorda/Firni.", "price": 999, "currency": "BDT", "is_bestseller": True},
                    {"name": "Wedding Bonanza Platter (1:3)", "description": "Complete wedding feast platter for 3 people with all accompaniments.", "price": 2699, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Polao, Tehari & Curries",
                "items": [
                    {"name": "Shahi Morog Polao", "description": "Fragrant Chinigura rice cooked with tender chicken leg quarter and rich ghee.", "price": 380, "currency": "BDT", "is_bestseller": True},
                    {"name": "Dhakaiya Beef Tehari", "description": "Spiced mustard oil rice cooked with small tender beef chunks.", "price": 340, "currency": "BDT", "is_bestseller": True},
                    {"name": "Shahi Beef Rezala", "description": "Slow cooked tender beef in rich yogurt, cashew nut and mawa gravy.", "price": 240, "currency": "BDT", "is_bestseller": True},
                    {"name": "Shahi Chicken Roast (1 Pc)", "description": "Tender chicken quarter slow-cooked in rich fragrant wedding-style caramelized onion gravy.", "price": 160, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Kababs & Traditional Sides",
                "items": [
                    {"name": "Shahi Jali Kabab (1 Pc)", "description": "Minced spiced mutton/beef patty enveloped in crispy egg lace netting.", "price": 70, "currency": "BDT", "is_bestseller": True},
                    {"name": "Shahi Tikka Kabab (1 Pc)", "description": "Lentil and shredded beef patty pan-fried with aromatic garam masala.", "price": 65, "currency": "BDT", "is_bestseller": False},
                    {"name": "Special Shahi Borhani (250ml)", "description": "Traditional spiced yogurt digestive drink with mint, black salt and roasted cumin.", "price": 80, "currency": "BDT", "is_bestseller": True},
                    {"name": "Special Shahi Borhani (1 Liter Bottle)", "description": "1 Liter family bottle of signature chilled Shahi Borhani.", "price": 280, "currency": "BDT", "is_bestseller": True},
                    {"name": "Alu Bukhara Chutney", "description": "Sweet and tangy plum chutney with raisins and almonds.", "price": 40, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Royal Desserts",
                "items": [
                    {"name": "Shahi Jorda", "description": "Traditional sweet saffron rice dessert garnished with mawa, nuts and baby sweets.", "price": 80, "currency": "BDT", "is_bestseller": True},
                    {"name": "Special Shahi Firni (Clay Cup)", "description": "Creamy ground rice pudding slow-cooked in milk, saffron and cardamom.", "price": 80, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]

    # CHILLOX
    elif rid == "chillox":
        r["menu_categories"] = [
            {
                "category_name": "Beef Loaded Burgers",
                "items": [
                    {"name": "Cheese Blast Beef Burger", "description": "Double thick beef patty stuffed with hot molten cheddar cheese inside, topped with melted slice and Chillox secret sauce.", "price": 340, "currency": "BDT", "is_bestseller": True},
                    {"name": "Smokey BBQ Beef with Bacon", "description": "Juicy beef patty basted with smoky BBQ sauce, crispy beef bacon strips and melted cheese.", "price": 310, "currency": "BDT", "is_bestseller": True},
                    {"name": "Beef Classic Burger", "description": "Standard grilled beef patty with special house sauce, lettuce and tomato.", "price": 210, "currency": "BDT", "is_bestseller": False},
                    {"name": "Beef Cheese Burger", "description": "Grilled beef patty layered with melted cheese and special burger sauce.", "price": 240, "currency": "BDT", "is_bestseller": False},
                    {"name": "Double Decker Beef Burger", "description": "Double beef patties and double melted cheese with caramelized onions.", "price": 370, "currency": "BDT", "is_bestseller": True},
                    {"name": "Giganto Beef Burger", "description": "Giant double beef patties, double beef bacon, double cheese and house sauce.", "price": 460, "currency": "BDT", "is_bestseller": False},
                    {"name": "Binge Burger (The Ultimate)", "description": "Double giant patties, smoked chicken, chicken ham and triple cheese.", "price": 540, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Chicken Loaded Burgers",
                "items": [
                    {"name": "Crisper Chicken Cheese Burger", "description": "Whole crispy boneless chicken thigh with crunchy lettuce, pickles, cheese and sauce.", "price": 280, "currency": "BDT", "is_bestseller": True},
                    {"name": "Cheese Blast Chicken Burger", "description": "Deep-fried chicken patty stuffed with gooey molten cheese inside.", "price": 320, "currency": "BDT", "is_bestseller": True},
                    {"name": "Smokey BBQ Chicken Burger", "description": "Grilled chicken breast basted in sweet smoky BBQ glaze with cheese.", "price": 260, "currency": "BDT", "is_bestseller": False},
                    {"name": "Classic Chicken Burger", "description": "Tender chicken patty with mayo and lettuce.", "price": 200, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Aged Beef Smasher Burgers",
                "items": [
                    {"name": "Truffle Smasher (Double)", "description": "Two aged beef patties smashed crispy on griddle with aromatic truffle sauce, caramelized onions and melted American cheese.", "price": 420, "currency": "BDT", "is_bestseller": True},
                    {"name": "Truffle Smasher (Single)", "description": "Single smashed aged beef patty with truffle sauce and cheese.", "price": 290, "currency": "BDT", "is_bestseller": False},
                    {"name": "Shiitake Mushroom Smasher", "description": "Smashed beef patty layered with sautéed shiitake mushrooms and velvety warm cheese sauce.", "price": 380, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Wings & Loaded Sides",
                "items": [
                    {"name": "Naga Drums (4 Pcs)", "description": "Fiery crispy chicken drumsticks seasoned with authentic hot Sylheti naga pepper.", "price": 280, "currency": "BDT", "is_bestseller": True},
                    {"name": "Pankha Wings - BBQ Glazed (6 Pcs)", "description": "Deep-fried chicken wings glazed in sweet & smoky barbecue sauce.", "price": 260, "currency": "BDT", "is_bestseller": True},
                    {"name": "Pankha Wings - Naga Glazed (6 Pcs)", "description": "Extremely spicy wings tossed in rich fiery naga sauce.", "price": 270, "currency": "BDT", "is_bestseller": True},
                    {"name": "Pankha Wings - Cheesy Cream (6 Pcs)", "description": "Crispy wings coated in rich garlic cheese sauce.", "price": 280, "currency": "BDT", "is_bestseller": False},
                    {"name": "Loaded Cheese Fries", "description": "Golden French fries drowned in warm melted cheddar cheese sauce.", "price": 210, "currency": "BDT", "is_bestseller": True},
                    {"name": "Naga Loaded Fries", "description": "Fries topped with shredded chicken, naga sauce and melted cheese.", "price": 250, "currency": "BDT", "is_bestseller": True},
                    {"name": "Crispy Chicken Tenders (4 Pcs)", "description": "Boneless white meat strips with garlic herb dip.", "price": 220, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Shakes & Drinks",
                "items": [
                    {"name": "Chillox Brownie Shake", "description": "Thick chocolate ice cream blended with crushed brownie chunks.", "price": 230, "currency": "BDT", "is_bestseller": True},
                    {"name": "Oreo Vanilla Shake", "description": "Thick milkshake blended with crushed Oreos.", "price": 210, "currency": "BDT", "is_bestseller": False},
                    {"name": "Cold Drinks (Can)", "description": "Coke / Sprite / Fanta.", "price": 40, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]

    # BFC
    elif rid == "bfc-best-fried-chicken":
        r["menu_categories"] = [
            {
                "category_name": "Crispy Fried Chicken & Buckets",
                "items": [
                    {"name": "BFC Fried Chicken (2 Pcs)", "description": "Classic recipe crispy chicken pieces (Rib/Thigh & Leg).", "price": 220, "currency": "BDT", "is_bestseller": True},
                    {"name": "BFC Fried Chicken (3 Pcs)", "description": "3 pieces of crunchy fried chicken.", "price": 330, "currency": "BDT", "is_bestseller": False},
                    {"name": "BFC Fried Chicken (5 Pcs)", "description": "5 pieces of fresh crunchy seasoned chicken.", "price": 550, "currency": "BDT", "is_bestseller": False},
                    {"name": "Midi Bucket (9 Pcs)", "description": "Value chicken bucket ideal for 3-4 people.", "price": 980, "currency": "BDT", "is_bestseller": True},
                    {"name": "Family Bucket (12 Pcs)", "description": "12 pieces of signature fried chicken for whole family feasts.", "price": 1300, "currency": "BDT", "is_bestseller": True},
                    {"name": "Maxi Bucket (15 Pcs)", "description": "15 pieces of crispy golden chicken.", "price": 1620, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Hot Wings & Strips",
                "items": [
                    {"name": "BFC Hot Wings (8 Pcs)", "description": "Crunchy spicy coated wings served piping hot.", "price": 250, "currency": "BDT", "is_bestseller": True},
                    {"name": "BFC Hot Wings (24 Pcs Bucket)", "description": "Large party bucket of 24 crispy hot wings.", "price": 725, "currency": "BDT", "is_bestseller": True},
                    {"name": "Naga Wings (8 Pcs)", "description": "Fiery wings tossed in signature spicy naga spice.", "price": 270, "currency": "BDT", "is_bestseller": True},
                    {"name": "Crispy Chicken Strips (6 Pcs)", "description": "Tender boneless chicken strips fried to a crisp.", "price": 300, "currency": "BDT", "is_bestseller": False},
                    {"name": "BBQ Boneless Chicken (20 Pcs)", "description": "Bite-sized chicken popcorn nuggets in sweet BBQ seasoning.", "price": 300, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Burgers & Sandwiches",
                "items": [
                    {"name": "Regular Chicken Burger", "description": "Standard fried chicken patty with mayo and lettuce.", "price": 175, "currency": "BDT", "is_bestseller": False},
                    {"name": "Supreme Cheese Burger", "description": "Tender chicken patty topped with melted cheese, lettuce and mayo.", "price": 210, "currency": "BDT", "is_bestseller": True},
                    {"name": "Grilled Chicken Burger", "description": "Marinated grilled chicken patty with herb dressing.", "price": 220, "currency": "BDT", "is_bestseller": False},
                    {"name": "Chicken Wrap", "description": "Crispy chicken strips rolled in tortilla with cheese and mayo.", "price": 240, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Rice Combos & Sides",
                "items": [
                    {"name": "BFC Fried Rice with 1 Pc Chicken", "description": "Fragrant Chinese-style fried rice served with 1 pc crispy chicken and coleslaw.", "price": 240, "currency": "BDT", "is_bestseller": True},
                    {"name": "BFC Fried Rice with 2 Pcs Chicken", "description": "Fried rice paired with 2 pieces of fried chicken and coleslaw.", "price": 340, "currency": "BDT", "is_bestseller": True},
                    {"name": "French Fries (Regular)", "description": "Salted potato fries.", "price": 110, "currency": "BDT", "is_bestseller": False},
                    {"name": "French Fries (Large)", "description": "Large portion of salted fries.", "price": 150, "currency": "BDT", "is_bestseller": False},
                    {"name": "BFC Coleslaw", "description": "Sweet creamy shredded cabbage and carrot salad.", "price": 60, "currency": "BDT", "is_bestseller": False},
                    {"name": "Mashed Potato with Gravy", "description": "Creamy mashed potato topped with brown chicken gravy.", "price": 90, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]

    # COOPERS BAKERY
    elif rid == "coopers-bakery":
        r["menu_categories"] = [
            {
                "category_name": "Whole Celebration Cakes (500g / 1kg)",
                "items": [
                    {"name": "American Black Forest Cake (500g)", "description": "Layered chocolate sponge filled with whipped cream, cherries and dark chocolate shavings.", "price": 900, "currency": "BDT", "is_bestseller": True},
                    {"name": "American Black Forest Cake (1 kg)", "description": "1 kg full celebration size Black Forest cake.", "price": 1600, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chocolate Fudge Cake (500g)", "description": "Dense, moist chocolate sponge coated with rich chocolate ganache.", "price": 900, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chocolate Fudge Cake (1 kg)", "description": "1 kg rich chocolate fudge cake.", "price": 1650, "currency": "BDT", "is_bestseller": False},
                    {"name": "Red Velvet Cake (500g)", "description": "Classic crimson sponge layered with smooth cream cheese frosting.", "price": 1000, "currency": "BDT", "is_bestseller": True},
                    {"name": "Tiramisu Cake (500g)", "description": "Coffee liqueur infused sponge with mascarpone cream.", "price": 850, "currency": "BDT", "is_bestseller": False},
                    {"name": "Vanilla Birthday Cake (1 kg)", "description": "Classic vanilla sponge with colorful celebratory piping.", "price": 1300, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Single Slices & Pastries",
                "items": [
                    {"name": "Black Forest Cake Slice", "description": "Single serving slice of signature Black Forest cake.", "price": 199, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chocolate Fudge Slice", "description": "Single slice of rich chocolate fudge cake.", "price": 180, "currency": "BDT", "is_bestseller": True},
                    {"name": "Vanilla Cake Slice", "description": "Classic sweet vanilla slice.", "price": 170, "currency": "BDT", "is_bestseller": False},
                    {"name": "Chocolate Pastry", "description": "Moist chocolate sponge pastry.", "price": 115, "currency": "BDT", "is_bestseller": False},
                    {"name": "Red Velvet Cupcake", "description": "Individual cupcake with cream cheese swirl.", "price": 80, "currency": "BDT", "is_bestseller": False},
                    {"name": "Chocolate Donut", "description": "Ring donut with rich chocolate icing.", "price": 50, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Savories & Hot Snacks",
                "items": [
                    {"name": "Cooper's Baked Singara", "description": "Flaky golden baked pastry packed with savory spiced minced potato and vegetables.", "price": 40, "currency": "BDT", "is_bestseller": True},
                    {"name": "Cooper's Baked Samosa", "description": "Crispy baked puff pastry filled with spiced minced chicken.", "price": 45, "currency": "BDT", "is_bestseller": False},
                    {"name": "Zesty Chicken Roll", "description": "Puff pastry stuffed with tangy, spiced shredded chicken.", "price": 35, "currency": "BDT", "is_bestseller": True},
                    {"name": "Crunchy Chicken Tikka Roll", "description": "Savory roll loaded with tandoori spiced chicken filling.", "price": 60, "currency": "BDT", "is_bestseller": True},
                    {"name": "Chicken Club Sandwich", "description": "Triple-decker sandwich with chicken, egg, lettuce and mayonnaise.", "price": 180, "currency": "BDT", "is_bestseller": True},
                    {"name": "Mini Pizza Bun", "description": "Baked bun topped with chicken, cheese and tomato sauce.", "price": 85, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Daily Breads & Biscuits",
                "items": [
                    {"name": "Cooper's Special Brown Bread", "description": "Freshly baked whole wheat high-fiber bread loaf.", "price": 145, "currency": "BDT", "is_bestseller": True},
                    {"name": "White Bread Loaf", "description": "Soft daily white sandwich bread.", "price": 80, "currency": "BDT", "is_bestseller": False},
                    {"name": "Plain Salted Biscuits (500g Pack)", "description": "Crispy traditional tea-time salted biscuits.", "price": 180, "currency": "BDT", "is_bestseller": True},
                    {"name": "Coffee Biscuits (500g Pack)", "description": "Aromatic coffee flavored sweet biscuits.", "price": 160, "currency": "BDT", "is_bestseller": False},
                    {"name": "Dry Cake (Box)", "description": "Crispy twice-baked sweet tea cake.", "price": 250, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]

with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# update JS file too
js_file = os.path.join(os.path.dirname(DATA_FILE), "restaurants_data.js")
with open(js_file, "w", encoding="utf-8") as f:
    f.write("window.RESTAURANTS_DATA = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n")

print("Full categorized menus written successfully!")
