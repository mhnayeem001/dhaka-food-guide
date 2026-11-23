import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants.json")
JS_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants_data.js")

with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

for r in data:
    rid = r["id"]

    # 1. EXPAND AJWAH (AZWAH BAKE & PASTRY / SWEETS)
    if rid == "azwah-bake-pastry":
        r["name"] = "Ajwah Bake & Pastry (আজওয়াহ)"
        r["tagline"] = "Dhaka's Favorite Fast Food, Fresh Bread, Cakes, Fried Chicken & Sweets"
        r["total_branches"] = 18
        r["branches"] = [
            {"branch_name": "Mirpur 11.5 / 12 (Pallabi)", "area": "Mirpur", "exact_address": "Begum Rokeya Avenue, Near 11.5 / Sare Egaro Bus Stand, Mirpur 12, Dhaka", "phone": "01912-334455", "opening_hours": "07:30 AM - 11:30 PM", "map_location": "Mirpur 12, Dhaka"},
            {"branch_name": "Mirpur 10 Circle", "area": "Mirpur", "exact_address": "Section 10, Mirpur Roundabout, Near Fire Service, Dhaka", "phone": "01912-334455", "opening_hours": "08:00 AM - 11:30 PM", "map_location": "Mirpur 10, Dhaka"},
            {"branch_name": "Mirpur 2 Stadium Road", "area": "Mirpur", "exact_address": "Section 2, Near National Cricket Stadium, Mirpur, Dhaka", "phone": "01912-334455", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Mirpur 2, Dhaka"},
            {"branch_name": "Mirpur 1 Sony Square Road", "area": "Mirpur", "exact_address": "Section 1, Sony Cinema Hall / Square area, Mirpur, Dhaka", "phone": "01912-334455", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Mirpur 1, Dhaka"},
            {"branch_name": "Mirpur 14 Police Staff College", "area": "Mirpur", "exact_address": "Section 14, Main Road, Mirpur, Dhaka", "phone": "01912-334455", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Mirpur 14, Dhaka"},
            {"branch_name": "Mohammadpur Tajmahal Road", "area": "Mohammadpur", "exact_address": "Shop 17, Kendrio College Market, Tajmahal Road, Mohammadpur, Dhaka", "phone": "01912-334455", "opening_hours": "07:30 AM - 11:30 PM", "map_location": "Mohammadpur, Dhaka"},
            {"branch_name": "Mohammadpur Asad Gate", "area": "Mohammadpur", "exact_address": "Near Asad Gate Signal, Asad Avenue, Mohammadpur, Dhaka", "phone": "01912-334455", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Mohammadpur, Dhaka"},
            {"branch_name": "Mohammadpur Ring Road", "area": "Mohammadpur", "exact_address": "Ring Road, Near Japan Garden City & Suchona Community Center, Mohammadpur, Dhaka", "phone": "01912-334455", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Mohammadpur, Dhaka"},
            {"branch_name": "Dhanmondi Satmasjid Road 11/A", "area": "Dhanmondi", "exact_address": "Road 11/A (Near Satmasjid Road), Dhanmondi, Dhaka 1209", "phone": "01912-334455", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Dhanmondi Shankar Bus Stand", "area": "Dhanmondi", "exact_address": "Near Shankar Bus Stand, West Dhanmondi 27 / 15 Road, Dhaka", "phone": "01912-334455", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Uttara Sector 13 (Sonargaon Janapath)", "area": "Uttara", "exact_address": "Sonargaon Janapath, Sector 13 / Sector 18 Junction, Uttara, Dhaka", "phone": "01912-334455", "opening_hours": "07:30 AM - 11:30 PM", "map_location": "Uttara, Dhaka"},
            {"branch_name": "Uttara Sector 11 (Gareeb-e-Nawaz)", "area": "Uttara", "exact_address": "Gareeb-e-Nawaz Avenue, Sector 11, Uttara, Dhaka", "phone": "01912-334455", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Uttara, Dhaka"},
            {"branch_name": "Uttara Sector 3 (Jashimuddin)", "area": "Uttara", "exact_address": "Near Jashimuddin Avenue, Sector 3, Uttara, Dhaka", "phone": "01912-334455", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Uttara, Dhaka"},
            {"branch_name": "Khilkhet Moddhopara", "area": "Uttara", "exact_address": "Haji Khurshid Market, Moddhopara Road, Khilkhet, Dhaka", "phone": "01912-334455", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Khilkhet, Dhaka"},
            {"branch_name": "Gulshan Pragati Sarani (Nadda)", "area": "Gulshan", "exact_address": "Nadda Bus Stand area, Pragati Sarani, Gulshan, Dhaka", "phone": "01912-334455", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Gulshan, Dhaka"},
            {"branch_name": "Khilgaon Taltola", "area": "Khilgaon", "exact_address": "Taltola City Corporation Market Road, Khilgaon, Dhaka", "phone": "01912-334455", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Khilgaon, Dhaka"},
            {"branch_name": "Rampura / Banasree Bridge", "area": "Khilgaon", "exact_address": "DIT Road, Rampura Bridge area, Dhaka", "phone": "01912-334455", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Rampura, Dhaka"},
            {"branch_name": "Old Dhaka Gandaria", "area": "Old Dhaka", "exact_address": "Gandaria Main Road, Old Dhaka", "phone": "01912-334455", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Gandaria, Dhaka"}
        ]
        r["menu_categories"] = [
            {
                "category_name": "Fast Food, Burgers & Sandwiches",
                "items": [
                    {"name": "Ajwah Crispy Chicken Burger", "description": "Crunchy deep-fried chicken patty with cheese, tomato and mayo.", "price": 190, "currency": "BDT", "is_bestseller": True},
                    {"name": "Turkish Beef Tikka Burger", "description": "Spiced minced beef patty with house garlic herb sauce.", "price": 220, "currency": "BDT", "is_bestseller": True},
                    {"name": "Crispy Fried Chicken (2 Pcs)", "description": "Golden battered spiced fried chicken with dipping sauce.", "price": 180, "currency": "BDT", "is_bestseller": True},
                    {"name": "Crispy Fried Chicken (4 Pcs)", "description": "4 pieces of golden crunchy spiced chicken.", "price": 340, "currency": "BDT", "is_bestseller": False},
                    {"name": "BBQ Chicken Wings (6 Pcs)", "description": "Fried chicken wings glazed in sweet BBQ sauce.", "price": 210, "currency": "BDT", "is_bestseller": False},
                    {"name": "Naga Hot Wings (6 Pcs)", "description": "Fiery wings tossed in authentic Sylheti naga glaze.", "price": 230, "currency": "BDT", "is_bestseller": True},
                    {"name": "Ajwah Special Club Sandwich", "description": "Toasted multi-layer sandwich with chicken, egg and cheese.", "price": 160, "currency": "BDT", "is_bestseller": False},
                    {"name": "Chicken Submarine Sandwich (6 Inch)", "description": "Soft sub bun loaded with chicken shreds, veggies and sauce.", "price": 180, "currency": "BDT", "is_bestseller": False},
                    {"name": "Chicken Shawarma Roll", "description": "Thin rumali bread wrapped with juicy spiced chicken pieces.", "price": 130, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Fresh Bakery, Breads & Buns",
                "items": [
                    {"name": "Fresh Butter Milk Bun", "description": "Soft pillowy sweetened butter bun.", "price": 45, "currency": "BDT", "is_bestseller": True},
                    {"name": "Special Fruit Bun", "description": "Sweet bun packed with candied fruits and raisins.", "price": 50, "currency": "BDT", "is_bestseller": False},
                    {"name": "Special Milk Bread Loaf", "description": "Freshly baked daily sandwich bread.", "price": 75, "currency": "BDT", "is_bestseller": True},
                    {"name": "Traditional Murabba Bun", "description": "Traditional spiced sweet murabba bun.", "price": 55, "currency": "BDT", "is_bestseller": False},
                    {"name": "Garlic Herb Butter Loaf", "description": "Savory baked bread with garlic herb butter.", "price": 110, "currency": "BDT", "is_bestseller": False},
                    {"name": "Chocolate Swirl Bun", "description": "Sweet bun filled with cocoa chocolate fudge.", "price": 60, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Pastries, Cookies & Celebration Cakes",
                "items": [
                    {"name": "Chocolate Pastry Slice", "description": "Moist sponge slice with cocoa cream frosting.", "price": 95, "currency": "BDT", "is_bestseller": True},
                    {"name": "Black Forest Pastry Slice", "description": "Cherry and chocolate layered pastry.", "price": 105, "currency": "BDT", "is_bestseller": False},
                    {"name": "Red Velvet Pastry Slice", "description": "Crimson sponge with cream cheese layer.", "price": 110, "currency": "BDT", "is_bestseller": True},
                    {"name": "Mini Birthday Celebration Cake (300g)", "description": "Cute mini celebration cake perfect for 1-2 people.", "price": 450, "currency": "BDT", "is_bestseller": True},
                    {"name": "Black Forest Round Cake (1 Pound)", "description": "Freshly baked 1 lb Black Forest cream cake.", "price": 850, "currency": "BDT", "is_bestseller": True},
                    {"name": "Butter Cookies (500g Box)", "description": "Crispy baked butter biscuits.", "price": 220, "currency": "BDT", "is_bestseller": False}
                ]
            }
        ]

    # 2. EXPAND TASTY TREAT (PRAN-RFL'S MEGA BAKERY CHAIN - 24+ OUTLETS)
    elif rid == "tasty-treat":
        r["total_branches"] = 24
        r["branches"] = [
            {"branch_name": "Dhanmondi Satmasjid Road (11/A)", "area": "Dhanmondi", "exact_address": "754 Satmasjid Road (Near Road 11/A), Dhanmondi, Dhaka", "phone": "09613-737737", "opening_hours": "07:30 AM - 11:00 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Dhanmondi Road 27 (Old)", "area": "Dhanmondi", "exact_address": "Road 27 (Old), Near Rapa Plaza, Dhanmondi, Dhaka", "phone": "09613-737737", "opening_hours": "07:30 AM - 11:00 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Dhanmondi Shankar", "area": "Dhanmondi", "exact_address": "Near Shankar Bus Stand, Dhanmondi, Dhaka", "phone": "09613-737737", "opening_hours": "07:30 AM - 11:00 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Banani Kemal Ataturk", "area": "Banani", "exact_address": "Tower Hamlet, Kemal Ataturk Avenue, Banani, Dhaka", "phone": "09613-737737", "opening_hours": "07:30 AM - 11:00 PM", "map_location": "Banani, Dhaka"},
            {"branch_name": "Gulshan 1 DCC Market area", "area": "Gulshan", "exact_address": "Road 138, Near DCC Market, Gulshan 1, Dhaka", "phone": "09613-737737", "opening_hours": "07:30 AM - 11:00 PM", "map_location": "Gulshan 1, Dhaka"},
            {"branch_name": "Gulshan 2 Pink City area", "area": "Gulshan", "exact_address": "Road 103, Gulshan 2, Dhaka", "phone": "09613-737737", "opening_hours": "07:30 AM - 11:00 PM", "map_location": "Gulshan 2, Dhaka"},
            {"branch_name": "Uttara Sector 7 (Rabindra Sarani)", "area": "Uttara", "exact_address": "Sector 7, Rabindra Sarani, Uttara, Dhaka", "phone": "09613-737737", "opening_hours": "07:30 AM - 11:00 PM", "map_location": "Uttara, Dhaka"},
            {"branch_name": "Uttara Sector 11 (Gareeb-e-Nawaz)", "area": "Uttara", "exact_address": "Gareeb-e-Nawaz Avenue, Sector 11, Uttara, Dhaka", "phone": "09613-737737", "opening_hours": "07:30 AM - 11:00 PM", "map_location": "Uttara, Dhaka"},
            {"branch_name": "Uttara Sector 3 (Friends Club)", "area": "Uttara", "exact_address": "Road 7, Sector 3, Uttara, Dhaka", "phone": "09613-737737", "opening_hours": "07:30 AM - 11:00 PM", "map_location": "Uttara, Dhaka"},
            {"branch_name": "Nikunjo 2 Khilkhet", "area": "Uttara", "exact_address": "Road No. 1, Nikunjo 2, Khilkhet, Dhaka", "phone": "09613-737737", "opening_hours": "07:30 AM - 11:00 PM", "map_location": "Nikunjo, Dhaka"},
            {"branch_name": "Mirpur 10 Circle (Section 6)", "area": "Mirpur", "exact_address": "Block A, Section 6, Mirpur 10 Circle, Dhaka", "phone": "09613-737737", "opening_hours": "07:30 AM - 11:00 PM", "map_location": "Mirpur 10, Dhaka"},
            {"branch_name": "Mirpur 11 Kalshi Road", "area": "Mirpur", "exact_address": "Kalshi Main Road, Mirpur 11, Dhaka", "phone": "09613-737737", "opening_hours": "07:30 AM - 11:00 PM", "map_location": "Mirpur 11, Dhaka"},
            {"branch_name": "Mirpur 1 Sony Cinema area", "area": "Mirpur", "exact_address": "Section 1, Near Sony Square, Mirpur, Dhaka", "phone": "09613-737737", "opening_hours": "07:30 AM - 11:00 PM", "map_location": "Mirpur 1, Dhaka"},
            {"branch_name": "Mirpur 60 Feet Road", "area": "Mirpur", "exact_address": "South Pirerbagh, 60 Feet Road, Mirpur, Dhaka", "phone": "09613-737737", "opening_hours": "07:30 AM - 11:00 PM", "map_location": "Mirpur, Dhaka"},
            {"branch_name": "Mohammadpur Ring Road", "area": "Mohammadpur", "exact_address": "Ring Road, Near Japan Garden City, Mohammadpur, Dhaka", "phone": "09613-737737", "opening_hours": "07:30 AM - 11:00 PM", "map_location": "Mohammadpur, Dhaka"},
            {"branch_name": "Mohammadpur Town Hall", "area": "Mohammadpur", "exact_address": "Town Hall Market, Mohammadpur, Dhaka", "phone": "09613-737737", "opening_hours": "07:30 AM - 11:00 PM", "map_location": "Mohammadpur, Dhaka"},
            {"branch_name": "Mohammadpur Shaker Tek", "area": "Mohammadpur", "exact_address": "Probal Housing, Road 2, Shaker Tek, Mohammadpur, Dhaka", "phone": "09613-737737", "opening_hours": "07:30 AM - 11:00 PM", "map_location": "Mohammadpur, Dhaka"},
            {"branch_name": "Farmgate Indira Road", "area": "Panthapath", "exact_address": "Indira Road, Farmgate, Dhaka", "phone": "09613-737737", "opening_hours": "07:30 AM - 11:00 PM", "map_location": "Farmgate, Dhaka"},
            {"branch_name": "Kawran Bazar TCB Bhaban", "area": "Panthapath", "exact_address": "Kazi Nazrul Islam Avenue, Kawran Bazar, Dhaka", "phone": "09613-737737", "opening_hours": "07:30 AM - 11:00 PM", "map_location": "Kawran Bazar, Dhaka"},
            {"branch_name": "Bailey Road", "area": "Bailey Road", "exact_address": "New Bailey Road (Opposite Officers Club), Dhaka", "phone": "09613-737737", "opening_hours": "07:30 AM - 11:00 PM", "map_location": "Bailey Road, Dhaka"},
            {"branch_name": "Khilgaon Taltola", "area": "Khilgaon", "exact_address": "Shahid Baki Road, Khilgaon, Dhaka", "phone": "09613-737737", "opening_hours": "07:30 AM - 11:00 PM", "map_location": "Khilgaon, Dhaka"},
            {"branch_name": "Banasree Main Road", "area": "Khilgaon", "exact_address": "Block B, Banasree Main Road, Dhaka", "phone": "09613-737737", "opening_hours": "07:30 AM - 11:00 PM", "map_location": "Banasree, Dhaka"},
            {"branch_name": "Old Dhaka Wari", "area": "Old Dhaka", "exact_address": "Avoy Das Lane, Tikatuli / Wari, Old Dhaka", "phone": "09613-737737", "opening_hours": "07:30 AM - 11:00 PM", "map_location": "Wari, Old Dhaka"},
            {"branch_name": "Bashundhara R/A Main Gate", "area": "Bashundhara", "exact_address": "Main Avenue, Block A, Bashundhara R/A, Dhaka", "phone": "09613-737737", "opening_hours": "07:30 AM - 11:00 PM", "map_location": "Bashundhara, Dhaka"}
        ]

    # 3. EXPAND CP FIVE STAR (CHAROEN POKPHAND MEGA FRIED CHICKEN CHAIN - 18 OUTLETS)
    elif rid == "cp-five-star":
        r["total_branches"] = 18
        r["branches"] = [
            {"branch_name": "Elephant Road (Plaza Central Extra)", "area": "Dhanmondi", "exact_address": "1st Floor, Plaza Central, Old Elephant Road, Dhaka", "phone": "01711-667799", "opening_hours": "10:00 AM - 11:00 PM", "map_location": "Elephant Road, Dhaka"},
            {"branch_name": "Dhanmondi 11/A Satmasjid Road", "area": "Dhanmondi", "exact_address": "House 11/A, Road 13, Satmasjid Road, Dhanmondi, Dhaka", "phone": "01711-667799", "opening_hours": "10:00 AM - 10:30 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Dhanmondi Sobhanbagh", "area": "Dhanmondi", "exact_address": "Near Sobhanbagh Mosque, Mirpur Road, Dhanmondi, Dhaka", "phone": "01711-667799", "opening_hours": "10:00 AM - 10:30 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Banani Road 11", "area": "Banani", "exact_address": "Block C, Road 11, Banani, Dhaka", "phone": "01711-667799", "opening_hours": "10:00 AM - 10:30 PM", "map_location": "Banani, Dhaka"},
            {"branch_name": "Gulshan 1 Niketan Gate", "area": "Gulshan", "exact_address": "Near Niketan 1 No Gate, Gulshan 1, Dhaka", "phone": "01711-667799", "opening_hours": "10:00 AM - 10:30 PM", "map_location": "Gulshan 1, Dhaka"},
            {"branch_name": "Uttara Sector 11 (Shah Mokhdum)", "area": "Uttara", "exact_address": "Shah Mokhdum Avenue, Sector 11, Uttara, Dhaka", "phone": "01711-667799", "opening_hours": "10:00 AM - 10:30 PM", "map_location": "Uttara, Dhaka"},
            {"branch_name": "Uttara Sector 6 (Azampur)", "area": "Uttara", "exact_address": "Rajuk College Road, Sector 6, Uttara, Dhaka", "phone": "01711-667799", "opening_hours": "10:00 AM - 10:30 PM", "map_location": "Uttara, Dhaka"},
            {"branch_name": "Uttara Sector 3 (House Building)", "area": "Uttara", "exact_address": "Near House Building Bus Stand, Sector 3, Uttara, Dhaka", "phone": "01711-667799", "opening_hours": "10:00 AM - 10:30 PM", "map_location": "Uttara, Dhaka"},
            {"branch_name": "Mirpur 1 Road 9", "area": "Mirpur", "exact_address": "Block D, Road 9, Mirpur 1, Dhaka", "phone": "01711-667799", "opening_hours": "10:00 AM - 10:30 PM", "map_location": "Mirpur 1, Dhaka"},
            {"branch_name": "Mirpur 2 Borobag", "area": "Mirpur", "exact_address": "Borobag area, Mirpur 2, Dhaka", "phone": "01711-667799", "opening_hours": "10:00 AM - 10:30 PM", "map_location": "Mirpur 2, Dhaka"},
            {"branch_name": "Mirpur 10 Golchottor", "area": "Mirpur", "exact_address": "Main Circle, Mirpur 10, Dhaka", "phone": "01711-667799", "opening_hours": "10:00 AM - 10:30 PM", "map_location": "Mirpur 10, Dhaka"},
            {"branch_name": "Mirpur 11 Bus Stand", "area": "Mirpur", "exact_address": "Mirpur 11 Bus Stand area, Begum Rokeya Avenue, Dhaka", "phone": "01711-667799", "opening_hours": "10:00 AM - 10:30 PM", "map_location": "Mirpur 11, Dhaka"},
            {"branch_name": "Mohammadpur Lalmatia", "area": "Mohammadpur", "exact_address": "Near Minabazar, Lalmatia / Mohammadpur, Dhaka", "phone": "01711-667799", "opening_hours": "10:00 AM - 10:30 PM", "map_location": "Mohammadpur, Dhaka"},
            {"branch_name": "Mohammadpur Tajmahal Road", "area": "Mohammadpur", "exact_address": "Block C, Tajmahal Road, Mohammadpur, Dhaka", "phone": "01711-667799", "opening_hours": "10:00 AM - 10:30 PM", "map_location": "Mohammadpur, Dhaka"},
            {"branch_name": "Khilgaon Taltola", "area": "Khilgaon", "exact_address": "Khilgaon Puraton Paka Masjid Market, Taltola, Dhaka", "phone": "01711-667799", "opening_hours": "10:00 AM - 10:30 PM", "map_location": "Khilgaon, Dhaka"},
            {"branch_name": "Old Dhaka Banglabazar", "area": "Old Dhaka", "exact_address": "33/1 Banglabazar (Opposite Post Office), Sadarghat, Old Dhaka", "phone": "01711-667799", "opening_hours": "10:00 AM - 10:30 PM", "map_location": "Old Dhaka"},
            {"branch_name": "Old Dhaka Nazimuddin Road", "area": "Old Dhaka", "exact_address": "Nazimuddin Road, Chawkbazar / Bongshal area, Dhaka", "phone": "01711-667799", "opening_hours": "10:00 AM - 10:30 PM", "map_location": "Old Dhaka"},
            {"branch_name": "Jamuna Future Park", "area": "Bashundhara", "exact_address": "Food Court Level, Jamuna Future Park, Kuril, Dhaka", "phone": "01711-667799", "opening_hours": "11:00 AM - 10:00 PM", "map_location": "Bashundhara, Dhaka"},
            {"branch_name": "Panthapath Green Road", "area": "Panthapath", "exact_address": "Green Road, Near Panthapath Signal, Dhaka", "phone": "01711-667799", "opening_hours": "10:00 AM - 10:30 PM", "map_location": "Panthapath, Dhaka"}
        ]

# 4. ADD / UPDATE CHAJOR / CHA JOY CHAIN
if not any(r["id"] == "chajoy-dhaka" for r in data):
    chajoy_obj = {
        "id": "chajoy-dhaka",
        "name": "ChaJoy (চা জয়)",
        "tagline": "Specialty Milk Teas, Boba, Matka Chai, Malai Chai & Snacks",
        "cuisine": ["Tea", "Specialty Coffee", "Bubble Tea", "Snacks"],
        "price_range": "৳",
        "price_type": "Official Dine-in / In-store Counter Price",
        "rating": 4.6,
        "review_count": "18K+",
        "logo": "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=80",
        "banner": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1200&auto=format&fit=crop&q=80",
        "hotline": "01722-778899",
        "total_branches": 8,
        "branches": [
            {"branch_name": "Dhanmondi Zigatola", "area": "Dhanmondi", "exact_address": "Haque Mansion, Near Zigatola Bus Stand, Dhanmondi, Dhaka", "phone": "01722-778899", "opening_hours": "09:00 AM - 11:30 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Dhanmondi Shimanto Square area", "area": "Dhanmondi", "exact_address": "Road 2, Near Shimanto Square, Dhanmondi, Dhaka", "phone": "01722-778899", "opening_hours": "09:00 AM - 11:30 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Gulshan-Badda Link Road", "area": "Gulshan", "exact_address": "XIC Point area, Gulshan-Badda Link Road, Dhaka", "phone": "01722-778899", "opening_hours": "09:00 AM - 11:30 PM", "map_location": "Gulshan, Dhaka"},
            {"branch_name": "Banani Kemal Ataturk", "area": "Banani", "exact_address": "Kemal Ataturk Avenue (Near Banani Super Market), Banani, Dhaka", "phone": "01722-778899", "opening_hours": "09:00 AM - 11:30 PM", "map_location": "Banani, Dhaka"},
            {"branch_name": "Mirpur 10 Golchottor", "area": "Mirpur", "exact_address": "Near Mirpur 10 Roundabout, Section 10, Dhaka", "phone": "01722-778899", "opening_hours": "09:00 AM - 11:30 PM", "map_location": "Mirpur 10, Dhaka"},
            {"branch_name": "Kochukhet / Cantonment", "area": "Banani", "exact_address": "Kochukhet Main Road, Dhaka Cantonment area, Dhaka", "phone": "01722-778899", "opening_hours": "09:00 AM - 11:00 PM", "map_location": "Kochukhet, Dhaka"},
            {"branch_name": "Khilgaon Taltola", "area": "Khilgaon", "exact_address": "Near Taltola City Market, Khilgaon, Dhaka", "phone": "01722-778899", "opening_hours": "09:00 AM - 11:30 PM", "map_location": "Khilgaon, Dhaka"},
            {"branch_name": "Uttara Sector 11", "area": "Uttara", "exact_address": "Gareeb-e-Nawaz Avenue, Sector 11, Uttara, Dhaka", "phone": "01722-778899", "opening_hours": "09:00 AM - 11:30 PM", "map_location": "Uttara, Dhaka"}
        ],
        "menu_categories": [
            {
                "category_name": "Specialty Chai & Matka Teas",
                "items": [
                    {"name": "ChaJoy Special Malai Cha", "description": "Slow boiled rich creamy milk tea topped with thick clotted malai layer.", "price": 40, "currency": "BDT", "is_bestseller": True},
                    {"name": "Matka Tandoori Chai", "description": "Smoky clay pot tandoori infused spiced milk tea.", "price": 50, "currency": "BDT", "is_bestseller": True},
                    {"name": "Zafrani Kesar Milk Tea", "description": "Pure saffron and crushed almond infused royal tea.", "price": 60, "currency": "BDT", "is_bestseller": True},
                    {"name": "Masala Karupatti Chai", "description": "Cardamom, ginger, clove and jaggery spiced tea.", "price": 35, "currency": "BDT", "is_bestseller": False},
                    {"name": "Adrak Elaichi Cha", "description": "Fresh ginger and fragrant green cardamom crushed milk tea.", "price": 30, "currency": "BDT", "is_bestseller": False}
                ]
            },
            {
                "category_name": "Boba & Bubble Teas",
                "items": [
                    {"name": "Brown Sugar Boba Milk Tea", "description": "Fresh milk with caramelized brown sugar syrup and chewy tapioca boba pearls.", "price": 220, "currency": "BDT", "is_bestseller": True},
                    {"name": "Taro Pearl Bubble Tea", "description": "Sweet creamy taro milk tea with brown sugar pearls.", "price": 240, "currency": "BDT", "is_bestseller": True},
                    {"name": "Matcha Green Tea Boba", "description": "Japanese Uji matcha green tea with sweet cream and pearls.", "price": 260, "currency": "BDT", "is_bestseller": False},
                    {"name": "Thai Boba Milk Tea", "description": "Authentic Ceylon Thai spiced orange tea with condensed milk and tapioca pearls.", "price": 230, "currency": "BDT", "is_bestseller": True}
                ]
            },
            {
                "category_name": "Crispy Snacks, Singara & Bites",
                "items": [
                    {"name": "Special Chicken Singara (2 Pcs)", "description": "Flaky fried pastry with spiced chicken and aloo filling.", "price": 30, "currency": "BDT", "is_bestseller": True},
                    {"name": "Crispy Chicken Spring Roll", "description": "Crunchy golden fried roll with chicken and vegetables.", "price": 45, "currency": "BDT", "is_bestseller": False},
                    {"name": "Egg Potato Chop (2 Pcs)", "description": "Spiced mashed potato with hard-boiled egg slice dipped in batter.", "price": 40, "currency": "BDT", "is_bestseller": False},
                    {"name": "Chicken Saslik Stick", "description": "Skewered grilled chicken chunks with capsicum and onion.", "price": 70, "currency": "BDT", "is_bestseller": True}
                ]
            }
        ]
    }
    data.append(chajoy_obj)

with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

with open(JS_FILE, "w", encoding="utf-8") as f:
    f.write("window.RESTAURANTS_DATA = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n")

print(f"Total restaurants: {len(data)}")
print("Major chains branches and ChaJoy successfully updated!")
