"""
Wave 6 Restaurant Expansion:
Adding 15 more iconic heritage, traditional Bengali, Old Dhaka, Japanese, and popular coffee chains across Dhaka.
"""
import json
import os

wave_6_restaurants = [
    {
        "id": "ghoroa-hotel",
        "name": "Ghoroa Hotel & Restaurant",
        "bangla_name": "ঘরোয়া হোটেল ও রেস্তোরাঁ",
        "category": "Bengali & Heritage",
        "cuisine": ["Bengali", "Biryani", "Khichuri", "Curry"],
        "rating": 4.5,
        "review_count": 8900,
        "price_tier": "৳",
        "logo": "🍛",
        "features": ["Dine-in", "Takeaway", "Legendary Khichuri", "Heritage Brand"],
        "branches": [
            {
                "name": "Motijheel (Original Landmark)",
                "area": "Motijheel",
                "address": "9/A Toyenbee Circular Road, Motijheel C/A, Dhaka",
                "phone": "+880 1711-234567",
                "hours": "7:00 AM - 11:30 PM",
                "map_query": "Ghoroa Hotel Motijheel Dhaka"
            },
            {
                "name": "Purana Paltan",
                "area": "Purana Paltan",
                "address": "Paltan China Town Building, Purana Paltan, Dhaka",
                "phone": "+880 1712-345678",
                "hours": "7:00 AM - 11:00 PM",
                "map_query": "Ghoroa Hotel Paltan Dhaka"
            }
        ],
        "menu": [
            {"id": "gh-1", "name": "Special Beef Bhuna Khichuri", "category": "Khichuri Specials", "price": 280, "description": "Ghoroa's iconic yellow bhuna khichuri served with rich, tender beef bhuna"},
            {"id": "gh-2", "name": "Mutton Bhuna Khichuri", "category": "Khichuri Specials", "price": 340, "description": "Fragrant bhuna khichuri served with spicy mutton bhuna gravy"},
            {"id": "gh-3", "name": "Chicken Bhuna Khichuri", "category": "Khichuri Specials", "price": 240, "description": "Classic comfort khichuri with slow-cooked desi chicken quarter"},
            {"id": "gh-4", "name": "Plain Bhuna Khichuri", "category": "Khichuri Specials", "price": 120, "description": "Steaming hot fragrant lentil and aromatic rice khichuri"},
            {"id": "gh-5", "name": "Egg Bhuna Khichuri", "category": "Khichuri Specials", "price": 160, "description": "Bhuna khichuri served with rich spicy poached egg bhuna"},
            {"id": "gh-6", "name": "Special Beef Bhuna (1 Bowl)", "category": "Curries & Bhuna", "price": 240, "description": "Tender beef chunks slow-simmered in rich caramelised onion gravy"},
            {"id": "gh-7", "name": "Mutton Rezala", "category": "Curries & Bhuna", "price": 310, "description": "Classic curd and cashew nut infused aromatic mutton curry"},
            {"id": "gh-8", "name": "Rui Fish Curry", "category": "Curries & Bhuna", "price": 180, "description": "Fresh river Rui fish cutlet in home-style tomato onion gravy"},
            {"id": "gh-9", "name": "Ilish Macher Jhol", "category": "Curries & Bhuna", "price": 320, "description": "Seasonal Hilsa fish steak cooked in light mustard turmeric gravy"},
            {"id": "gh-10", "name": "Mixed Vegetable Bhaji", "category": "Sides & Bhortas", "price": 50, "description": "Daily fresh seasonal mixed vegetable stir fry"},
            {"id": "gh-11", "name": "Alu Bhorta / Begun Bhorta", "category": "Sides & Bhortas", "price": 40, "description": "Traditional roasted eggplant or mashed mustard potato"},
            {"id": "gh-12", "name": "Thick Masoor Daal", "category": "Sides & Bhortas", "price": 40, "description": "Slow-tempered yellow lentils with dry chili and garlic bagar"},
            {"id": "gh-13", "name": "Paratha / Ruti", "category": "Breads", "price": 20, "description": "Crisp flaky layered ghee paratha or soft handmade ruti"},
            {"id": "gh-14", "name": "Special Borhani (Glass)", "category": "Beverages", "price": 60, "description": "Chilled traditional spiced yogurt digestion drink with mint and mustard"}
        ]
    },
    {
        "id": "kasturi-restaurant",
        "name": "Kasturi Restaurant",
        "bangla_name": "কস্তুরী রেস্তোরাঁ",
        "category": "Bengali & Heritage",
        "cuisine": ["Bengali", "Desi Fish", "Bhorta", "Traditional"],
        "rating": 4.6,
        "review_count": 6200,
        "price_tier": "৳৳",
        "logo": "🐟",
        "features": ["Dine-in", "Authentic Bengali", "Fresh Fish Specialists", "Heritage Since 1970s"],
        "branches": [
            {
                "name": "Purana Paltan (Main Branch)",
                "area": "Purana Paltan",
                "address": "8 Purana Paltan, (Adjacent to Culvert Road), Dhaka",
                "phone": "+880 2-9562728",
                "hours": "11:00 AM - 11:00 PM",
                "map_query": "Kasturi Restaurant Purana Paltan Dhaka"
            },
            {
                "name": "Gulshan 1",
                "area": "Gulshan",
                "address": "Road 138, South Avenue, Gulshan 1, Dhaka",
                "phone": "+880 1819-218321",
                "hours": "12:00 PM - 11:00 PM",
                "map_query": "Kasturi Restaurant Gulshan Dhaka"
            }
        ],
        "menu": [
            {"id": "kas-1", "name": "Shorshe Ilish (Original Padma)", "category": "Fish Delicacies", "price": 480, "description": "Generous cutlet of Padma Hilsa simmered in fresh ground mustard paste and green chillies"},
            {"id": "kas-2", "name": "Ilish Macher Dim Bhuna", "category": "Fish Delicacies", "price": 380, "description": "Seasonal Hilsa roe pan-fried and braised in rich onion masala"},
            {"id": "kas-3", "name": "Chital Macher Muitha", "category": "Fish Delicacies", "price": 420, "description": "Heritage boneless clown knifefish dumplings in thick cardamom gravy"},
            {"id": "kas-4", "name": "Chital Peti Bhuna", "category": "Fish Delicacies", "price": 460, "description": "Rich fatty belly portion of giant Chital fish braised to perfection"},
            {"id": "kas-5", "name": "Kachki Macher Chorchori", "category": "Fish Delicacies", "price": 220, "description": "Tiny freshwater whitefish braised dry with potato matchsticks and green onions"},
            {"id": "kas-6", "name": "Desi Duck Bhuna (Haasher Mangsho)", "category": "Meat & Poultry", "price": 350, "description": "Country duck slow-braised in black pepper, garlic and aromatic garam masala"},
            {"id": "kas-7", "name": "Beef Kala Bhuna", "category": "Meat & Poultry", "price": 320, "description": "Tender beef roasted dark with roasted spices in traditional Chittagong style"},
            {"id": "kas-8", "name": "Desi Murgir Jhol", "category": "Meat & Poultry", "price": 280, "description": "Free-range village rooster curry with baby potatoes"},
            {"id": "kas-9", "name": "Chingri Macher Malaikari", "category": "Fish Delicacies", "price": 440, "description": "Jumbo river prawn cooked in rich coconut milk and mild spices"},
            {"id": "kas-10", "name": "Kasturi Special Bhorta Platter (5 Kinds)", "category": "Bhorta Heritage", "price": 240, "description": "Assortment of Chepa Shutki, Chingri Bhorta, Kalo Jeera, Begun, and Badam Bhorta"},
            {"id": "kas-11", "name": "Chepa Shutki Bhuna", "category": "Bhorta Heritage", "price": 160, "description": "Fermented puntius dry fish braised in spicy caramelized onion and red chilies"},
            {"id": "kas-12", "name": "Steamed Miniket Rice (Per Bowl)", "category": "Rice & Breads", "price": 60, "description": "Aromatic fine long grain boiled white rice"},
            {"id": "kas-13", "name": "Morog Polao (Kasturi Style)", "category": "Rice & Breads", "price": 320, "description": "Fragrant chinigura rice slow cooked with ghee and country chicken leg"},
            {"id": "kas-14", "name": "Signature Borhani", "category": "Drinks & Desserts", "price": 70, "description": "Traditional thick mint mustard borhani made with curd"}
        ]
    },
    {
        "id": "tehari-ghar",
        "name": "Tehari Ghar",
        "bangla_name": "তেহারী ঘর",
        "category": "Biryani & Kacchi",
        "cuisine": ["Tehari", "Bengali", "Old Dhaka Spices"],
        "rating": 4.4,
        "review_count": 4800,
        "price_tier": "৳",
        "logo": "🥩",
        "features": ["Dine-in", "Takeaway", "Lalmatia Legend", "Authentic Mustard Oil Tehari"],
        "branches": [
            {
                "name": "Lalmatia (Original)",
                "area": "Mohammadpur",
                "address": "Block C, 3/14 Lalmatia (Near Minabazar), Mohammadpur, Dhaka",
                "phone": "+880 1715-998877",
                "hours": "11:30 AM - 11:00 PM",
                "map_query": "Tehari Ghar Lalmatia Dhaka"
            },
            {
                "name": "Dhanmondi Branch",
                "area": "Dhanmondi",
                "address": "Mirpur Road, Near Kalabagan Bus Stand, Dhanmondi, Dhaka",
                "phone": "+880 1819-887766",
                "hours": "12:00 PM - 11:30 PM",
                "map_query": "Tehari Ghar Dhanmondi Dhaka"
            }
        ],
        "menu": [
            {"id": "tg-1", "name": "Special Beef Tehari (Full)", "category": "Tehari Specials", "price": 220, "description": "Aromatic Chinigura rice cooked in pure mustard oil with tender bite-sized beef chunks"},
            {"id": "tg-2", "name": "Special Beef Tehari (Half)", "category": "Tehari Specials", "price": 140, "description": "Single serving of authentic mustard oil beef tehari with green chilies"},
            {"id": "tg-3", "name": "Extra Beef Portion (Shahi Bati)", "category": "Tehari Specials", "price": 120, "description": "Extra bowl of slow-cooked spicy tender beef gravy"},
            {"id": "tg-4", "name": "Chicken Tehari (Full)", "category": "Tehari Specials", "price": 200, "description": "Fragrant mustard oil tehari infused with tender desi chicken cubes"},
            {"id": "tg-5", "name": "Chicken Tehari (Half)", "category": "Tehari Specials", "price": 130, "description": "Light portion of spiced aromatic chicken tehari"},
            {"id": "tg-6", "name": "Boiled Egg (Dim Bhuna)", "category": "Add-ons", "price": 25, "description": "Fried spiced egg accompaniment"},
            {"id": "tg-7", "name": "Shahi Borhani (250ml Bottle)", "category": "Beverages", "price": 50, "description": "Fresh tangy digestion borhani prepared daily with rock salt and mint"},
            {"id": "tg-8", "name": "Sweet Lassi (Glass)", "category": "Beverages", "price": 60, "description": "Creamy chilled yogurt drink blended with cardamom"},
            {"id": "tg-9", "name": "Firni (Earthen Cup)", "category": "Desserts", "price": 50, "description": "Traditional thick rice pudding set in clay bowl with pistachio nuts"}
        ]
    },
    {
        "id": "al-razzaque",
        "name": "Al Razzaque International Restaurant",
        "bangla_name": "আল রাজ্জাক ইন্টারন্যাশনাল",
        "category": "Old Dhaka Heritage",
        "cuisine": ["Mughlai", "Biryani", "Kebab", "Heritage"],
        "rating": 4.5,
        "review_count": 7300,
        "price_tier": "৳৳",
        "logo": "🍗",
        "features": ["Dine-in", "Takeaway", "Heritage Icon", "Late Night Dining", "Famous Glash"],
        "branches": [
            {
                "name": "Kazi Alauddin Road (Old Dhaka)",
                "area": "Old Dhaka",
                "address": "29/1 Kazi Alauddin Road, Bangshal, Old Dhaka",
                "phone": "+880 2-9566373",
                "hours": "6:00 AM - 1:30 AM",
                "map_query": "Al Razzaque Restaurant Old Dhaka"
            }
        ],
        "menu": [
            {"id": "arz-1", "name": "Famous Shahi Morog Polao (Glash)", "category": "Heritage Specials", "price": 310, "description": "Legendary jumbo chicken leg cooked in golden ghee gravy served with spiced polao and egg"},
            {"id": "arz-2", "name": "Mutton Kacchi Biryani", "category": "Biryani & Polao", "price": 320, "description": "Aromatic Basmati rice slow dum cooked with tender mutton and saffron potato"},
            {"id": "arz-3", "name": "Beef Biryani", "category": "Biryani & Polao", "price": 240, "description": "Authentic Old Dhaka spiced beef cooked with fragrant chinigura rice"},
            {"id": "arz-4", "name": "Mutton Glash (Special Rich Curry)", "category": "Heritage Specials", "price": 340, "description": "Al Razzaque's signature slow-simmered rich mutton shank curry with marrow"},
            {"id": "arz-5", "name": "Special Beef Bhuna", "category": "Curries & Gravy", "price": 240, "description": "Succulent beef cubes roasted in thick dark brown onion paste"},
            {"id": "arz-6", "name": "Mutton Rezala", "category": "Curries & Gravy", "price": 300, "description": "Rich white gravy mutton braised with cashew paste and mace"},
            {"id": "arz-7", "name": "Chicken Tikka Kebab (Full)", "category": "Tandoor & Kebab", "price": 200, "description": "Char-grilled spicy marinated chicken quarter straight from clay tandoor"},
            {"id": "arz-8", "name": "Beef Boti Kebab", "category": "Tandoor & Kebab", "price": 180, "description": "Tenderized skewered beef cubes roasted over charcoal"},
            {"id": "arz-9", "name": "Shahi Butter Naan", "category": "Breads", "price": 40, "description": "Tandoori flatbread brushed with golden butter"},
            {"id": "arz-10", "name": "Garlic Naan", "category": "Breads", "price": 50, "description": "Oven fresh naan studded with minced garlic and coriander"},
            {"id": "arz-11", "name": "Shahi Tukra", "category": "Desserts", "price": 70, "description": "Crisp fried bread soaked in saffron-scented thickened rabri milk"},
            {"id": "arz-12", "name": "Zarda with Baby Sweets", "category": "Desserts", "price": 80, "description": "Sweet orange aromatic rice tossed with ghee, raisins and mini gulab jamuns"},
            {"id": "arz-13", "name": "Old Dhaka Borhani (Bottle)", "category": "Beverages", "price": 60, "description": "Thick tangy curd borhani laced with black pepper and cumin"}
        ]
    },
    {
        "id": "nirob-hotel",
        "name": "Nirob Hotel & Restaurant",
        "bangla_name": "নীরব হোটেল ও রেস্তোরাঁ",
        "category": "Old Dhaka Heritage",
        "cuisine": ["Bengali", "Bhorta Specialist", "Duck Curry", "Brain Masala"],
        "rating": 4.4,
        "review_count": 5600,
        "price_tier": "৳",
        "logo": "🥣",
        "features": ["Dine-in", "Takeaway", "Nazira Bazar Icon", "30+ Bhorta Varieties"],
        "branches": [
            {
                "name": "Nazira Bazar (Main)",
                "area": "Old Dhaka",
                "address": "113/2 Nazira Bazar, Bangshal, Old Dhaka",
                "phone": "+880 1711-889900",
                "hours": "7:00 AM - 1:00 AM",
                "map_query": "Nirob Hotel Nazira Bazar Dhaka"
            }
        ],
        "menu": [
            {"id": "nr-1", "name": "Nirob Bhorta Tasting Thali (8 Types)", "category": "Bhorta Feast", "price": 220, "description": "Assortment of Chepa shutki, Chingri, Loitta, Kalojeera, Badam, Dhoniyapata, Begun & Pesta"},
            {"id": "nr-2", "name": "Chingri Macher Bhorta", "category": "Bhorta Feast", "price": 50, "description": "Hand-pounded fresh shrimp roasted with mustard oil and charred green chilies"},
            {"id": "nr-3", "name": "Loitta Shutki Bhuna", "category": "Bhorta Feast", "price": 70, "description": "Dried ribbon fish slow-braised with garlic cloves and fiery chili paste"},
            {"id": "nr-4", "name": "Kalo Jeera Bhorta", "category": "Bhorta Feast", "price": 40, "description": "Heated black cumin seeds stone-ground with garlic and mustard oil"},
            {"id": "nr-5", "name": "Badam Bhorta (Cashew & Peanut)", "category": "Bhorta Feast", "price": 50, "description": "Unique rich nutty bhorta made with roasted peanuts and cashew"},
            {"id": "nr-6", "name": "Haasher Mangsho (Desi Duck Curry)", "category": "Special Curries", "price": 310, "description": "Nirob's iconic winter duck curry slow-cooked with rich black pepper and coconut"},
            {"id": "nr-7", "name": "Beef Brain Fry (Mogoj Bhuna)", "category": "Special Curries", "price": 260, "description": "Spiced creamy beef brain sautéed with caramelized onions and green chilies"},
            {"id": "nr-8", "name": "Beef Bot Bhuna (Tripe)", "category": "Special Curries", "price": 200, "description": "Slow-roasted tender beef tripe prepared in traditional Old Dhaka style"},
            {"id": "nr-9", "name": "Desi Chicken Bhuna", "category": "Special Curries", "price": 220, "description": "Village poultry cooked in country gravy with potatoes"},
            {"id": "nr-10", "name": "Plain Rice (Bhaat)", "category": "Staples", "price": 40, "description": "Steamed white rice served hot"},
            {"id": "nr-11", "name": "Cholar Daal / Masoor Daal", "category": "Staples", "price": 40, "description": "Home-style lentils cooked with aromatic tempering"},
            {"id": "nr-12", "name": "Special Borhani", "category": "Beverages", "price": 50, "description": "Chilled spiced yogurt drink"}
        ]
    },
    {
        "id": "premium-sweets",
        "name": "Premium Sweets",
        "bangla_name": "প্রিমিয়াম সুইটস",
        "category": "Sweets & Bakery",
        "cuisine": ["Bengali Sweets", "Gourmet Mithai", "Snacks", "Breakfast"],
        "rating": 4.6,
        "review_count": 9100,
        "price_tier": "৳৳৳",
        "logo": "🍬",
        "features": ["Dine-in", "Gift Boxes", "Artisanal Sweets", "All Dhaka Delivery"],
        "branches": [
            {
                "name": "Gulshan 2 Outlet",
                "area": "Gulshan",
                "address": "House 18, Road 103, Gulshan 2, Dhaka",
                "phone": "+880 1713-445566",
                "hours": "9:00 AM - 11:00 PM",
                "map_query": "Premium Sweets Gulshan 2 Dhaka"
            },
            {
                "name": "Dhanmondi Branch",
                "area": "Dhanmondi",
                "address": "House 32, Road 2, Dhanmondi R/A, Dhaka",
                "phone": "+880 1713-445577",
                "hours": "9:00 AM - 11:00 PM",
                "map_query": "Premium Sweets Dhanmondi Dhaka"
            },
            {
                "name": "Uttara Branch",
                "area": "Uttara",
                "address": "Sector 3, Jashimuddin Avenue, Uttara, Dhaka",
                "phone": "+880 1713-445588",
                "hours": "9:00 AM - 11:00 PM",
                "map_query": "Premium Sweets Uttara Dhaka"
            }
        ],
        "menu": [
            {"id": "ps-1", "name": "Sandesh Royale (Per Pc)", "category": "Artisanal Sweets", "price": 95, "description": "Silky smooth chhana sandesh decorated with saffron and silver leaf"},
            {"id": "ps-2", "name": "Roshomalai (Signature Cup)", "category": "Artisanal Sweets", "price": 220, "description": "Mini melt-in-mouth cottage cheese dumplings soaked in condensed saffron rabri milk"},
            {"id": "ps-3", "name": "Ghee Laddu (Motichoor)", "category": "Artisanal Sweets", "price": 75, "description": "Made with 100% pure deshi ghee, pistachios and cashews"},
            {"id": "ps-4", "name": "Kacha Golla (Pure Chhana)", "category": "Artisanal Sweets", "price": 85, "description": "Fresh mild soft cottage cheese delicacy seasoned with cardamom"},
            {"id": "ps-5", "name": "Shahi Gulab Jamun (Per Pc)", "category": "Artisanal Sweets", "price": 75, "description": "Caramelized deep-brown milk solids dumpling soaked in rose syrup"},
            {"id": "ps-6", "name": "Bogura Shahi Misti Doi (Earthen Pot)", "category": "Curd & Dairy", "price": 320, "description": "Authentic caramel sweet yogurt slow fermented in unglazed clay pot"},
            {"id": "ps-7", "name": "Special Halwa Porota Breakfast Platter", "category": "Snacks & Breakfast", "price": 250, "description": "Flaky ghee parathas served with chana daal and badam sooji halwa"},
            {"id": "ps-8", "name": "Premium Samosa / Shingara (2 Pcs)", "category": "Snacks & Breakfast", "price": 90, "description": "Golden crisp pastry filled with spiced cauliflower and potato mash"},
            {"id": "ps-9", "name": "Assorted Luxury Sweet Box (1 Kg)", "category": "Gift Boxes", "price": 1450, "description": "Hand-picked assortment of Premium Sweets best creations in luxury rigid packaging"},
            {"id": "ps-10", "name": "Special Masala Chai", "category": "Beverages", "price": 90, "description": "Slow brewed spiced milk tea with ginger, cardamom and clove"}
        ]
    },
    {
        "id": "rosh-sweets",
        "name": "Rosh Sweets",
        "bangla_name": "রস সুইটস",
        "category": "Sweets & Bakery",
        "cuisine": ["Bengali Sweets", "Traditional Sweets", "Snacks"],
        "rating": 4.5,
        "review_count": 5200,
        "price_tier": "৳৳",
        "logo": "🍯",
        "features": ["Takeaway", "Dine-in", "Famous Chamcham", "Multiple Outlets"],
        "branches": [
            {
                "name": "Bailey Road",
                "area": "Bailey Road",
                "address": "New Bailey Road, Dhaka",
                "phone": "+880 1711-334411",
                "hours": "8:00 AM - 10:30 PM",
                "map_query": "Rosh Sweets Bailey Road Dhaka"
            },
            {
                "name": "Dhanmondi (Satmasjid Road)",
                "area": "Dhanmondi",
                "address": "Satmasjid Road, Dhanmondi, Dhaka",
                "phone": "+880 1711-334422",
                "hours": "8:00 AM - 11:00 PM",
                "map_query": "Rosh Sweets Dhanmondi Dhaka"
            },
            {
                "name": "Banani Outlet",
                "area": "Banani",
                "address": "Road 11, Block D, Banani, Dhaka",
                "phone": "+880 1711-334433",
                "hours": "9:00 AM - 11:00 PM",
                "map_query": "Rosh Sweets Banani Dhaka"
            }
        ],
        "menu": [
            {"id": "rs-1", "name": "Porabari Style Chamcham (Per Pc)", "category": "Signature Sweets", "price": 60, "description": "Tangail style caramelized dense sweet rolled in roasted mawa powder"},
            {"id": "rs-2", "name": "Roshogolla (Spongy & Juicy)", "category": "Signature Sweets", "price": 50, "description": "Classic white spongy fresh chhana ball swimming in pure sugar syrup"},
            {"id": "rs-3", "name": "Roshomalai (Bowl)", "category": "Signature Sweets", "price": 180, "description": "Soft mini sweet pearls drenched in thick reduced cardamom milk"},
            {"id": "rs-4", "name": "Kheer Kadam", "category": "Signature Sweets", "price": 65, "description": "Mini roshogolla encapsulated in velvety soft grated kheer and mawa layer"},
            {"id": "rs-5", "name": "Kacha Sandesh", "category": "Signature Sweets", "price": 60, "description": "Light, pure freshly kneaded cottage cheese delicate sweet"},
            {"id": "rs-6", "name": "Misti Doi (Clay Pot)", "category": "Yogurt & Dairy", "price": 260, "description": "Creamy traditional sweet curd set in earthen bowl"},
            {"id": "rs-7", "name": "Tok Doi (Sour Curd - 500g)", "category": "Yogurt & Dairy", "price": 140, "description": "Fresh set natural probiotic plain sour yogurt"},
            {"id": "rs-8", "name": "Crispy Daal Puri (2 Pcs)", "category": "Snacks", "price": 50, "description": "Deep-fried spiced lentil-stuffed puffed flatbread"},
            {"id": "rs-9", "name": "Mughlai Porota (Beef Stuffed)", "category": "Snacks", "price": 140, "description": "Crisp envelope stuffed with egg, minced beef, green chilies and onions"}
        ]
    },
    {
        "id": "banoful",
        "name": "Banoful & Co.",
        "bangla_name": "বনফুল অ্যান্ড কোং",
        "category": "Sweets & Bakery",
        "cuisine": ["Bengali Sweets", "Bakery", "Biscuits", "Snacks"],
        "rating": 4.3,
        "review_count": 8400,
        "price_tier": "৳",
        "logo": "🧁",
        "features": ["Takeaway", "Affordable", "Widespread Across Dhaka", "Fresh Bakes"],
        "branches": [
            {
                "name": "Mirpur 10 Outlet",
                "area": "Mirpur",
                "address": "Mirpur 10 Roundabout, Mirpur, Dhaka",
                "phone": "+880 1819-123401",
                "hours": "7:30 AM - 10:30 PM",
                "map_query": "Banoful Mirpur 10 Dhaka"
            },
            {
                "name": "Mohammadpur (Town Hall)",
                "area": "Mohammadpur",
                "address": "Town Hall Market, Mohammadpur, Dhaka",
                "phone": "+880 1819-123402",
                "hours": "7:30 AM - 10:30 PM",
                "map_query": "Banoful Mohammadpur Dhaka"
            },
            {
                "name": "Khilgaon Taltola",
                "area": "Khilgaon",
                "address": "Taltola City Corporation Market, Khilgaon, Dhaka",
                "phone": "+880 1819-123403",
                "hours": "7:30 AM - 10:30 PM",
                "map_query": "Banoful Khilgaon Dhaka"
            }
        ],
        "menu": [
            {"id": "bf-1", "name": "Chomchom (1 Kg)", "category": "Traditional Sweets", "price": 420, "description": "Traditional caramelized chhana chomchom dusted with powdered mawa"},
            {"id": "bf-2", "name": "Spongy Rosgulla (1 Kg)", "category": "Traditional Sweets", "price": 380, "description": "Fluffy cottage cheese balls dipped in clear cardamom sugar syrup"},
            {"id": "bf-3", "name": "Motichoor Laddu (500g)", "category": "Traditional Sweets", "price": 240, "description": "Tender gram flour pearls bonded in fragrant sugar syrup"},
            {"id": "bf-4", "name": "Balushahi Sweet (1 Kg)", "category": "Traditional Sweets", "price": 400, "description": "Flaky glazed deep fried donut-like heritage sweet"},
            {"id": "bf-5", "name": "Chicken Patty (Fresh Baked)", "category": "Bakery & Savory", "price": 45, "description": "Golden puff pastry turnover filled with spicy minced chicken"},
            {"id": "bf-6", "name": "Vegetable Roll", "category": "Bakery & Savory", "price": 35, "description": "Breadcrumb coated roll stuffed with spiced mixed seasonal vegetables"},
            {"id": "bf-7", "name": "Dry Cake Biscuits (Family Pack)", "category": "Bakery & Savory", "price": 160, "description": "Crunchy twice-baked tea-time sponge cake slices"},
            {"id": "bf-8", "name": "Toast Biscuits (Special)", "category": "Bakery & Savory", "price": 120, "description": "Classic crisp tea-dipping rusks"},
            {"id": "bf-9", "name": "Sweet Curd (Misti Doi 500g)", "category": "Dairy", "price": 180, "description": "Creamy sweet yogurt in container"}
        ]
    },
    {
        "id": "tokyo-express",
        "name": "Tokyo Express",
        "bangla_name": "টোকিও এক্সপ্রেস",
        "category": "Pan Asian & Japanese",
        "cuisine": ["Japanese", "Sushi", "Ramen", "Teriyaki"],
        "rating": 4.5,
        "review_count": 4200,
        "price_tier": "৳৳৳",
        "logo": "🍣",
        "features": ["Dine-in", "Takeaway", "Authentic Japanese", "Chef Made Sushi"],
        "branches": [
            {
                "name": "Banani Road 11",
                "area": "Banani",
                "address": "House 45, Road 11, Block D, Banani, Dhaka",
                "phone": "+880 1711-556677",
                "hours": "12:00 PM - 11:00 PM",
                "map_query": "Tokyo Express Banani Dhaka"
            },
            {
                "name": "Dhanmondi Branch",
                "area": "Dhanmondi",
                "address": "House 67, Road 11/A, Dhanmondi, Dhaka",
                "phone": "+880 1711-556688",
                "hours": "12:00 PM - 11:00 PM",
                "map_query": "Tokyo Express Dhanmondi Dhaka"
            },
            {
                "name": "Uttara Sector 3",
                "area": "Uttara",
                "address": "Rabindra Sarani, Sector 3, Uttara, Dhaka",
                "phone": "+880 1711-556699",
                "hours": "12:00 PM - 11:00 PM",
                "map_query": "Tokyo Express Uttara Dhaka"
            }
        ],
        "menu": [
            {"id": "te-1", "name": "California Roll (8 Pcs)", "category": "Sushi & Maki", "price": 680, "description": "Crab stick, creamy avocado, crisp cucumber roll topped with tobiko flying fish roe"},
            {"id": "te-2", "name": "Salmon Nigiri (2 Pcs)", "category": "Sushi & Maki", "price": 420, "description": "Fresh imported Norwegian salmon sliced over seasoned vinegared sushi rice"},
            {"id": "te-3", "name": "Spicy Tuna Maki (8 Pcs)", "category": "Sushi & Maki", "price": 720, "description": "Finely diced fresh yellowfin tuna tossed in spicy sriracha mayo"},
            {"id": "te-4", "name": "Ebi Tempura Roll (8 Pcs)", "category": "Sushi & Maki", "price": 650, "description": "Crisp battered prawn tempura rolled with avocado and drizzled with sweet unagi eel glaze"},
            {"id": "te-5", "name": "Tokyo Shoyu Chicken Ramen", "category": "Ramen & Noodles", "price": 580, "description": "Handmade noodles in rich slow-simmered chicken broth with nitamago egg, menma and nori"},
            {"id": "te-6", "name": "Spicy Miso Beef Ramen", "category": "Ramen & Noodles", "price": 640, "description": "Fiery fermented miso broth topped with sliced tender beef, sweet corn, and spring onions"},
            {"id": "te-7", "name": "Chicken Katsu Curry Don", "category": "Bento & Bowls", "price": 540, "description": "Crispy panko-breaded chicken cutlet over Japanese rice with hearty aromatic curry sauce"},
            {"id": "te-8", "name": "Beef Teriyaki Rice Bowl", "category": "Bento & Bowls", "price": 620, "description": "Tender beef slices glazed in house-made mirin teriyaki reduction over steamed rice"},
            {"id": "te-9", "name": "Crispy Prawn Tempura (4 Pcs)", "category": "Starters & Appetizers", "price": 490, "description": "Golden feather-light battered tiger prawns served with tentsuyu dipping sauce"},
            {"id": "te-10", "name": "Pan-Fried Chicken Gyoza (5 Pcs)", "category": "Starters & Appetizers", "price": 380, "description": "Crisp bottom dumplings stuffed with seasoned minced chicken, ginger and cabbage"},
            {"id": "te-11", "name": "Steamed Edamame with Sea Salt", "category": "Starters & Appetizers", "price": 280, "description": "Fresh green soybean pods sprinkled with rock crystal salt"},
            {"id": "te-12", "name": "Japanese Green Tea (Hot)", "category": "Beverages", "price": 120, "description": "Steamed premium Sencha green tea brewed in ceramic pot"}
        ]
    },
    {
        "id": "soi-71",
        "name": "Soi 71",
        "bangla_name": "সয় ৭১",
        "category": "Pan Asian & Japanese",
        "cuisine": ["Thai", "Asian", "Seafood", "Fine Dining"],
        "rating": 4.6,
        "review_count": 3100,
        "price_tier": "৳৳৳",
        "logo": "🍲",
        "features": ["Dine-in", "Romantic Ambience", "Authentic Thai Chefs", "Fine Dining"],
        "branches": [
            {
                "name": "Gulshan 2 (Main)",
                "area": "Gulshan",
                "address": "House 18, Road 46, Gulshan 2, Dhaka",
                "phone": "+880 2-9844444",
                "hours": "12:30 PM - 11:00 PM",
                "map_query": "Soi 71 Gulshan 2 Dhaka"
            }
        ],
        "menu": [
            {"id": "soi-1", "name": "Tom Yum Goong (Clear / Creamy)", "category": "Soups", "price": 620, "description": "Spicy lemongrass, galangal and kaffir lime broth loaded with fresh jumbo tiger prawns"},
            {"id": "soi-2", "name": "Tom Kha Gai (Coconut Chicken Soup)", "category": "Soups", "price": 540, "description": "Silky coconut milk soup scented with lemongrass, tender chicken and straw mushrooms"},
            {"id": "soi-3", "name": "Som Tum (Green Papaya Salad)", "category": "Salads", "price": 420, "description": "Crushed green shredded papaya with bird's eye chili, roasted peanuts, lime and palm sugar"},
            {"id": "soi-4", "name": "Pad Thai Goong", "category": "Noodles & Rice", "price": 580, "description": "Wok-tossed rice noodles with prawns, firm tofu, bean sprouts, crushed peanuts in tamarind reduction"},
            {"id": "soi-5", "name": "Khao Pad Kra Pao (Basil Beef Fried Rice)", "category": "Noodles & Rice", "price": 560, "description": "Jasmine rice fried with minced beef, fiery red chilies, garlic and sacred Thai holy basil"},
            {"id": "soi-6", "name": "Thai Green Curry (Chicken / Beef)", "category": "Curries", "price": 640, "description": "Aromatic green curry paste simmered in rich coconut milk with Thai eggplants and bamboo shoots"},
            {"id": "soi-7", "name": "Massaman Curry (Mutton / Beef)", "category": "Curries", "price": 720, "description": "Royal mild slow-cooked curry with tender potatoes, star anise and roasted whole peanuts"},
            {"id": "soi-8", "name": "Crispy Whole Fish with Three-Flavored Sauce", "category": "Seafood", "price": 950, "description": "Deep-fried whole sea bass drizzled with sweet, sour, and spicy chili tamarind glaze"},
            {"id": "soi-9", "name": "Thai Jasmine Rice (Per Bowl)", "category": "Noodles & Rice", "price": 140, "description": "Steamed aromatic long grain imported Thai Hom Mali jasmine rice"},
            {"id": "soi-10", "name": "Mango Sticky Rice (Seasonal)", "category": "Desserts", "price": 450, "description": "Sweet coconut sticky rice served with sliced ripe mango and toasted sesame seeds"},
            {"id": "soi-11", "name": "Authentic Cha Yen (Thai Iced Tea)", "category": "Beverages", "price": 240, "description": "Brewed Thai black tea shaken with sweet condensed milk over crushed ice"}
        ]
    },
    {
        "id": "gloria-jeans-coffees",
        "name": "Gloria Jean's Coffees Bangladesh",
        "bangla_name": "গ্লোরিয়া জিন্স কফি",
        "category": "Cafe & Coffee",
        "cuisine": ["Specialty Coffee", "Espresso", "Bakery", "Desserts", "Sandwiches"],
        "rating": 4.5,
        "review_count": 6800,
        "price_tier": "৳৳৳",
        "logo": "☕",
        "features": ["Dine-in", "High Speed WiFi", "Work Friendly", "International Coffee Chain"],
        "branches": [
            {
                "name": "Gulshan 1 Branch",
                "area": "Gulshan",
                "address": "Navana Tower, 45 Gulshan South Avenue, Gulshan 1, Dhaka",
                "phone": "+880 2-8836371",
                "hours": "7:30 AM - 12:00 AM",
                "map_query": "Gloria Jeans Coffees Gulshan 1 Dhaka"
            },
            {
                "name": "Dhanmondi Branch",
                "area": "Dhanmondi",
                "address": "House 35, Road 2, Dhanmondi R/A, Dhaka",
                "phone": "+880 2-9614488",
                "hours": "8:00 AM - 11:30 PM",
                "map_query": "Gloria Jeans Coffees Dhanmondi Dhaka"
            },
            {
                "name": "Gulshan 2 Outlet",
                "area": "Gulshan",
                "address": "Rangs Arcade, 153/A Gulshan North Avenue, Gulshan 2, Dhaka",
                "phone": "+880 2-8819871",
                "hours": "7:30 AM - 12:00 AM",
                "map_query": "Gloria Jeans Coffees Gulshan 2 Dhaka"
            }
        ],
        "menu": [
            {"id": "gjc-1", "name": "Caffe Latte (Regular / Large)", "category": "Hot Coffee", "price": 320, "description": "Rich espresso poured over freshly textured silky steamed milk with subtle microfoam"},
            {"id": "gjc-2", "name": "Cappuccino", "category": "Hot Coffee", "price": 320, "description": "Bold double espresso topped with thick velvety dairy froth and dusted cocoa"},
            {"id": "gjc-3", "name": "Signature Caramelette", "category": "Signature Specialties", "price": 395, "description": "Creamy rich espresso with buttery caramel syrup, whipped cream and caramel drizzle"},
            {"id": "gjc-4", "name": "Iced Vanilla Latte", "category": "Iced Coffee", "price": 360, "description": "Espresso and cold milk infused with aromatic French vanilla poured over ice rocks"},
            {"id": "gjc-5", "name": "Voltage Chiller (Signature Frozen)", "category": "Chillers & Frappes", "price": 440, "description": "Gloria Jeans famous coffee chiller with espresso beans, chocolate and vanilla cream"},
            {"id": "gjc-6", "name": "Cookies & Cream Chiller", "category": "Chillers & Frappes", "price": 420, "description": "Creamy blended chiller with crunchy Oreo cookies and mountain of whipped cream"},
            {"id": "gjc-7", "name": "Smoked Chicken & Mushroom Panini", "category": "Gourmet Sandwiches", "price": 460, "description": "Grilled Italian panini stuffed with smoked shredded chicken breast, button mushrooms, melted cheese"},
            {"id": "gjc-8", "name": "Roast Beef Croissant Sandwich", "category": "Gourmet Sandwiches", "price": 490, "description": "Buttery flaky French croissant packed with sliced tender roast beef and cheddar"},
            {"id": "gjc-9", "name": "Classic New York Cheesecake", "category": "Cakes & Desserts", "price": 390, "description": "Dense and creamy baked cream cheese slice with graham cracker crumb base"},
            {"id": "gjc-10", "name": "Fudgy Chocolate Brownie with Ice Cream", "category": "Cakes & Desserts", "price": 320, "description": "Warm gooey dark chocolate walnut brownie served with vanilla ice cream"}
        ]
    },
    {
        "id": "chaap-shamlao",
        "name": "Chaap Shamlao",
        "bangla_name": "চাপ সামলাও",
        "category": "Fast Food & Burgers",
        "cuisine": ["Chaap", "Luchi", "Grilled Kebab", "Street Food"],
        "rating": 4.4,
        "review_count": 3900,
        "price_tier": "৳",
        "logo": "🥩",
        "features": ["Dine-in", "Takeaway", "Famous Chaap & Luchi", "Budget Friendly"],
        "branches": [
            {
                "name": "Mohammadpur (Salimullah Road)",
                "area": "Mohammadpur",
                "address": "Salimullah Road, Mohammadpur, Dhaka",
                "phone": "+880 1712-443322",
                "hours": "3:00 PM - 11:30 PM",
                "map_query": "Chaap Shamlao Mohammadpur Dhaka"
            },
            {
                "name": "Khilgaon Outlet",
                "area": "Khilgaon",
                "address": "Taltola, Khilgaon, Dhaka",
                "phone": "+880 1712-443333",
                "hours": "3:30 PM - 11:30 PM",
                "map_query": "Chaap Shamlao Khilgaon Dhaka"
            },
            {
                "name": "Mirpur 2",
                "area": "Mirpur",
                "address": "Near Commerce College, Mirpur 2, Dhaka",
                "phone": "+880 1712-443344",
                "hours": "3:30 PM - 11:30 PM",
                "map_query": "Chaap Shamlao Mirpur Dhaka"
            }
        ],
        "menu": [
            {"id": "cs-1", "name": "Special Beef Chaap (Tawa Fried)", "category": "Chaap Specials", "price": 160, "description": "Tenderized thin beef cutlet pan-fried in spices on hot iron tawa"},
            {"id": "cs-2", "name": "Crispy Chicken Chaap", "category": "Chaap Specials", "price": 140, "description": "Spiced crumb-coated chicken breast fried to crisp golden perfection"},
            {"id": "cs-3", "name": "Beef Brain Tawa Fry (Mogoj Chaap)", "category": "Chaap Specials", "price": 180, "description": "Soft spiced beef brain sautéed with onions and chilies on tawa"},
            {"id": "cs-4", "name": "Chicken Boti Kebab (6 Pcs)", "category": "Kebabs", "price": 160, "description": "Boneless marinated chicken chunks skewered and char-grilled"},
            {"id": "cs-5", "name": "Special Hot Puffed Luchi (4 Pcs)", "category": "Sides & Breads", "price": 40, "description": "Golden deep-fried puffy refined flour flatbreads"},
            {"id": "cs-6", "name": "Garlic Paratha", "category": "Sides & Breads", "price": 35, "description": "Crisp flaky layered paratha with roasted garlic flakes"},
            {"id": "cs-7", "name": "Cucumber Onion Salad with Green Mint Chutney", "category": "Sides & Breads", "price": 20, "description": "Fresh tangy accompaniment"},
            {"id": "cs-8", "name": "Sweet Lassi (Chilled)", "category": "Drinks", "price": 50, "description": "Traditional sweet yogurt refreshment"}
        ]
    },
    {
        "id": "decent-pastry-shop",
        "name": "Decent Pastry Shop",
        "bangla_name": "ডিসেন্ট পেস্ট্রি শপ",
        "category": "Sweets & Bakery",
        "cuisine": ["Bakery", "Pastry", "Puff Patty", "Heritage Snack"],
        "rating": 4.5,
        "review_count": 6400,
        "price_tier": "৳",
        "logo": "🥐",
        "features": ["Takeaway", "Since 1968", "Iconic Beef Patty", "Pure Heritage"],
        "branches": [
            {
                "name": "Motijheel (Original)",
                "area": "Motijheel",
                "address": "40/1 Toyenbee Circular Road, Motijheel C/A, Dhaka",
                "phone": "+880 2-9556093",
                "hours": "8:00 AM - 9:30 PM",
                "map_query": "Decent Pastry Shop Motijheel Dhaka"
            },
            {
                "name": "Dhanmondi Branch",
                "area": "Dhanmondi",
                "address": "Road 4, Near Gausia Twin Peak, Dhanmondi, Dhaka",
                "phone": "+880 1711-209933",
                "hours": "9:00 AM - 10:00 PM",
                "map_query": "Decent Pastry Shop Dhanmondi Dhaka"
            }
        ],
        "menu": [
            {"id": "dps-1", "name": "Decent Famous Beef Patty", "category": "Iconic Savories", "price": 55, "description": "Decent's 50-year legendary thousand-layer flaky puff filled with spicy minced beef"},
            {"id": "dps-2", "name": "Chicken Puff Patty", "category": "Iconic Savories", "price": 50, "description": "Buttery golden puff pastry with seasoned minced chicken filling"},
            {"id": "dps-3", "name": "Egg Chop (Spiced)", "category": "Iconic Savories", "price": 35, "description": "Hard-boiled egg wrapped in spicy mashed potato crust and deep-fried"},
            {"id": "dps-4", "name": "Chicken Roll (Breadcrumbed)", "category": "Iconic Savories", "price": 45, "description": "Crisp crusted roll packed with shredded chicken and pepper"},
            {"id": "dps-5", "name": "Black Forest Pastry Slice", "category": "Cakes & Sweets", "price": 90, "description": "Chocolate sponge layered with whipped cream and sour cherry glaze"},
            {"id": "dps-6", "name": "Vanilla Cream Pastry", "category": "Cakes & Sweets", "price": 80, "description": "Fluffy vanilla sponge with silky buttercream icing"},
            {"id": "dps-7", "name": "Decent Butter Biscuits (Box)", "category": "Cakes & Sweets", "price": 180, "description": "Melt in mouth vintage butter cookies"}
        ]
    },
    {
        "id": "al-fresco",
        "name": "Al-Fresco",
        "bangla_name": "আল-ফ্রেসকো",
        "category": "Continental & Italian",
        "cuisine": ["Italian", "Pizza", "Pasta", "Steak", "Continental"],
        "rating": 4.3,
        "review_count": 4100,
        "price_tier": "৳৳",
        "logo": "🍕",
        "features": ["Dine-in", "Student Friendly", "Huge Portion Sizes", "Dhanmondi Favorite"],
        "branches": [
            {
                "name": "Dhanmondi (Shimanto Square)",
                "area": "Dhanmondi",
                "address": "Level 4, Shimanto Square, Dhanmondi Road 2, Dhaka",
                "phone": "+880 1711-098765",
                "hours": "12:00 PM - 10:30 PM",
                "map_query": "Al Fresco Shimanto Square Dhanmondi Dhaka"
            },
            {
                "name": "Banani Outlet",
                "area": "Banani",
                "address": "Road 11, Banani, Dhaka",
                "phone": "+880 1711-098766",
                "hours": "12:30 PM - 11:00 PM",
                "map_query": "Al Fresco Banani Dhaka"
            }
        ],
        "menu": [
            {"id": "alf-1", "name": "Al-Fresco Special Pizza (12 Inch)", "category": "Wood-style Pizzas", "price": 680, "description": "Generously topped with chicken, beef, mushrooms, capsicum, olives and mozzarella"},
            {"id": "alf-2", "name": "BBQ Chicken Pizza (12 Inch)", "category": "Wood-style Pizzas", "price": 640, "description": "Tangy smoked BBQ chicken, red onions, jalapeños and stringy mozzarella cheese"},
            {"id": "alf-3", "name": "Fettuccine Creamy Alfredo", "category": "Pasta Specialties", "price": 460, "description": "Flat pasta tossed in thick garlic cream sauce with grilled chicken breast and parmesan"},
            {"id": "alf-4", "name": "Spaghetti Bolognese", "category": "Pasta Specialties", "price": 440, "description": "Slow-cooked minced beef tomato ragu over al dente spaghetti with parmesan cheese"},
            {"id": "alf-5", "name": "Oven Baked Pasta (Al-Fresco Signature)", "category": "Pasta Specialties", "price": 480, "description": "Macaroni layered with chicken, béchamel, tomato gravy and baked under thick cheese crust"},
            {"id": "alf-6", "name": "Grilled Chicken Steak with Mushroom Pepper Sauce", "category": "Steaks & Platters", "price": 540, "description": "Marinated boneless chicken steak served with sauteed vegetables and mashed potatoes"},
            {"id": "alf-7", "name": "Crispy Buffalo Wings (6 Pcs)", "category": "Appetizers", "price": 320, "description": "Tossed in spicy tangy Louisiana style pepper sauce"},
            {"id": "alf-8", "name": "Virgin Mint Mojito", "category": "Mocktails & Drinks", "price": 180, "description": "Muddled fresh mint sprigs, lime wedges, simple syrup and chilled sparkling soda"}
        ]
    },
    {
        "id": "samdado-japanese",
        "name": "Samdado Japanese Cuisine",
        "bangla_name": "সামদাদো জাপানিজ কুইজিন",
        "category": "Pan Asian & Japanese",
        "cuisine": ["Japanese", "Sushi", "Sashimi", "Teppanyaki", "Fine Dining"],
        "rating": 4.7,
        "review_count": 2800,
        "price_tier": "৳৳৳",
        "logo": "🍱",
        "features": ["Dine-in", "Teppanyaki Counter", "Authentic Slicing", "Executive Dining"],
        "branches": [
            {
                "name": "Gulshan 2 (Main)",
                "area": "Gulshan",
                "address": "House 27, Road 35, Gulshan 2, Dhaka",
                "phone": "+880 2-8815124",
                "hours": "12:00 PM - 3:00 PM, 6:30 PM - 10:30 PM",
                "map_query": "Samdado Japanese Cuisine Gulshan Dhaka"
            }
        ],
        "menu": [
            {"id": "sam-1", "name": "Salmon Sashimi (5 Thick Cuts)", "category": "Sashimi & Raw Bar", "price": 750, "description": "Prime chilled Atlantic salmon sliced to precision, served with shiso leaf and fresh wasabi"},
            {"id": "sam-2", "name": "Tuna Sashimi (5 Thick Cuts)", "category": "Sashimi & Raw Bar", "price": 780, "description": "Fresh grade-A ruby red tuna loin sashimi cuts"},
            {"id": "sam-3", "name": "Dragon Roll (8 Pcs)", "category": "Signature Rolls", "price": 890, "description": "Shrimp tempura and cucumber wrapped with sliced buttery avocado and drizzled with unagi sauce"},
            {"id": "sam-4", "name": "Rainbow Roll (8 Pcs)", "category": "Signature Rolls", "price": 920, "description": "California roll draped in alternating layers of fresh salmon, tuna, prawn and avocado"},
            {"id": "sam-5", "name": "Teppanyaki Beef Tenderloin", "category": "Teppan & Robata", "price": 1250, "description": "Seared tender beef cubes flambéed on iron griddle with garlic butter, served with fried rice"},
            {"id": "sam-6", "name": "Chicken Teriyaki Bento Box", "category": "Bento Sets", "price": 850, "description": "Complete meal with grilled chicken teriyaki, tempura, gyoza, potato salad, miso soup and rice"},
            {"id": "sam-7", "name": "Miso Soup (Traditional)", "category": "Starters & Soups", "price": 180, "description": "Dashi broth with fermented soybean paste, silken tofu, scallions and wakame seaweed"},
            {"id": "sam-8", "name": "Matcha Green Tea Ice Cream (2 Scoops)", "category": "Desserts", "price": 320, "description": "Rich authentic Japanese stone-ground green tea infused cream"}
        ]
    }
]

def add_wave_6():
    db_path = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants.json")
    with open(db_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    existing_ids = {r["id"] for r in data}
    added_count = 0
    for r in wave_6_restaurants:
        if r["id"] not in existing_ids:
            data.append(r)
            existing_ids.add(r["id"])
            added_count += 1

    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Added {added_count} iconic Wave 6 restaurants! Total restaurants now: {len(data)}")

if __name__ == "__main__":
    add_wave_6()
