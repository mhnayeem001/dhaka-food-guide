import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants.json")
JS_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants_data.js")

with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

for r in data:
    rid = r["id"]

    # COOPER'S BAKERY (Expanded to 16 major outlets)
    if rid == "coopers-bakery":
        r["total_branches"] = 16
        r["branches"] = [
            {"branch_name": "Gulshan 1 Circle", "area": "Gulshan", "exact_address": "Navana Tower, Gulshan 1 Circle, Dhaka", "phone": "02-9892603", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Gulshan 1, Dhaka"},
            {"branch_name": "Gulshan 2 Avenue", "area": "Gulshan", "exact_address": "House 10, Road 46, Gulshan 2, Dhaka", "phone": "02-9892603", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Gulshan 2, Dhaka"},
            {"branch_name": "Banani Road 11", "area": "Banani", "exact_address": "House 54, Road 11, Block D, Banani, Dhaka", "phone": "02-9883582", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Banani, Dhaka"},
            {"branch_name": "Dhanmondi Road 27", "area": "Dhanmondi", "exact_address": "House 27 (Old), Road 16 (New), Dhanmondi, Dhaka", "phone": "02-9134567", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Dhanmondi Satmasjid Road", "area": "Dhanmondi", "exact_address": "Plot 52/1, Road 3/A, Satmasjid Road, Dhanmondi, Dhaka", "phone": "02-9134567", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Uttara Sector 3", "area": "Uttara", "exact_address": "Plot 18, Road 7, Sector 3, Uttara, Dhaka", "phone": "02-8951234", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Uttara, Dhaka"},
            {"branch_name": "Uttara Sector 11", "area": "Uttara", "exact_address": "Gareeb-e-Nawaz Avenue, Sector 11, Uttara, Dhaka", "phone": "02-8951234", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Uttara, Dhaka"},
            {"branch_name": "Mirpur 10 Circle", "area": "Mirpur", "exact_address": "Section 10, Mirpur Roundabout, Dhaka", "phone": "02-9012345", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Mirpur 10, Dhaka"},
            {"branch_name": "Mirpur 2 Mirpur Stadium", "area": "Mirpur", "exact_address": "Section 2, Near National Cricket Stadium, Mirpur, Dhaka", "phone": "02-9012345", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Mirpur 2, Dhaka"},
            {"branch_name": "Bailey Road", "area": "Bailey Road", "exact_address": "12 New Bailey Road, Dhaka", "phone": "02-9334567", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Bailey Road, Dhaka"},
            {"branch_name": "Khilgaon Taltola", "area": "Khilgaon", "exact_address": "Shahid Baki Road, Block B, Khilgaon, Dhaka", "phone": "02-7212345", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Khilgaon, Dhaka"},
            {"branch_name": "Banasree", "area": "Khilgaon", "exact_address": "Block C, Main Road, Banasree, Dhaka", "phone": "02-7212345", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Banasree, Dhaka"},
            {"branch_name": "Mohammadpur Iqbal Road", "area": "Mohammadpur", "exact_address": "Iqbal Road, Block A, Mohammadpur, Dhaka", "phone": "02-9123456", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Mohammadpur, Dhaka"},
            {"branch_name": "Mohammadpur Ring Road", "area": "Mohammadpur", "exact_address": "Ring Road, Near Suchona Community Center, Mohammadpur, Dhaka", "phone": "02-9123456", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Mohammadpur, Dhaka"},
            {"branch_name": "Bashundhara R/A Main Gate", "area": "Bashundhara", "exact_address": "Block B, Main Gate Avenue, Bashundhara R/A, Dhaka", "phone": "02-8412345", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Bashundhara, Dhaka"},
            {"branch_name": "Old Dhaka Wari", "area": "Old Dhaka", "exact_address": "Rankin Street, Wari, Dhaka 1203", "phone": "02-7112345", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Wari, Dhaka"}
        ]

    # WELL FOOD (Expanded to 12 major outlets)
    elif rid == "well-food":
        r["total_branches"] = 12
        r["branches"] = [
            {"branch_name": "Gulshan 1", "area": "Gulshan", "exact_address": "Gulshan 1 Circle, DCC Market Opposite, Dhaka", "phone": "01730-088990", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Gulshan 1, Dhaka"},
            {"branch_name": "Gulshan 2", "area": "Gulshan", "exact_address": "Road 103, Near Pink City, Gulshan 2, Dhaka", "phone": "01730-088990", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Gulshan 2, Dhaka"},
            {"branch_name": "Banani Road 11", "area": "Banani", "exact_address": "Plot 78, Road 11, Banani, Dhaka", "phone": "01730-088990", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Banani, Dhaka"},
            {"branch_name": "Dhanmondi 27", "area": "Dhanmondi", "exact_address": "Road 27 (Old), Opposite Dhanmondi Girls College, Dhaka", "phone": "01730-088990", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Dhanmondi Satmasjid Road", "area": "Dhanmondi", "exact_address": "Near Road 8/A, Satmasjid Road, Dhanmondi, Dhaka", "phone": "01730-088990", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Uttara Sector 3", "area": "Uttara", "exact_address": "Rabindra Sarani, Sector 3, Uttara, Dhaka", "phone": "01730-088990", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Uttara, Dhaka"},
            {"branch_name": "Uttara Sector 11", "area": "Uttara", "exact_address": "Gareeb-e-Nawaz Avenue, Sector 11, Uttara, Dhaka", "phone": "01730-088990", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Uttara, Dhaka"},
            {"branch_name": "Mirpur 10", "area": "Mirpur", "exact_address": "Mirpur 10 Roundabout, Section 10, Dhaka", "phone": "01730-088990", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Mirpur 10, Dhaka"},
            {"branch_name": "Mirpur 1", "area": "Mirpur", "exact_address": "Near Sony Cinema Hall, Section 1, Mirpur, Dhaka", "phone": "01730-088990", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Mirpur 1, Dhaka"},
            {"branch_name": "Bailey Road", "area": "Bailey Road", "exact_address": "New Bailey Road, Dhaka", "phone": "01730-088990", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Bailey Road, Dhaka"},
            {"branch_name": "Mohammadpur", "area": "Mohammadpur", "exact_address": "Tajmahal Road, Block C, Mohammadpur, Dhaka", "phone": "01730-088990", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Mohammadpur, Dhaka"},
            {"branch_name": "Old Dhaka Wari", "area": "Old Dhaka", "exact_address": "Rankin Street, Wari, Dhaka", "phone": "01730-088990", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Wari, Dhaka"}
        ]

    # MITHAI (PRAN-RFL SWEETS CHAIN - 14 OUTLETS)
    elif rid == "mithai-dhaka":
        r["total_branches"] = 14
        r["branches"] = [
            {"branch_name": "Mirpur 10 Circle", "area": "Mirpur", "exact_address": "Section 10, Mirpur Roundabout, Dhaka", "phone": "09613-737737", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Mirpur 10, Dhaka"},
            {"branch_name": "Mirpur 2 Stadium Road", "area": "Mirpur", "exact_address": "Section 2, Mirpur Cricket Stadium Gate 1 area, Dhaka", "phone": "09613-737737", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Mirpur 2, Dhaka"},
            {"branch_name": "Mirpur 11 Kalshi", "area": "Mirpur", "exact_address": "Kalshi Main Road, Mirpur 11, Dhaka", "phone": "09613-737737", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Mirpur 11, Dhaka"},
            {"branch_name": "Dhanmondi Satmasjid Road", "area": "Dhanmondi", "exact_address": "Near Road 7/A, Satmasjid Road, Dhanmondi, Dhaka", "phone": "09613-737737", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Dhanmondi 27", "area": "Dhanmondi", "exact_address": "Road 27 (Old), Near Rapa Plaza, Dhanmondi, Dhaka", "phone": "09613-737737", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Mohammadpur Town Hall", "area": "Mohammadpur", "exact_address": "Town Hall Super Market, Mohammadpur, Dhaka", "phone": "09613-737737", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Mohammadpur, Dhaka"},
            {"branch_name": "Mohammadpur Ring Road", "area": "Mohammadpur", "exact_address": "Ring Road, Near Japan Garden City, Mohammadpur, Dhaka", "phone": "09613-737737", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Mohammadpur, Dhaka"},
            {"branch_name": "Uttara Sector 7", "area": "Uttara", "exact_address": "Sector 7, Rabindra Sarani, Uttara, Dhaka", "phone": "09613-737737", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Uttara, Dhaka"},
            {"branch_name": "Uttara Sector 11", "area": "Uttara", "exact_address": "Gareeb-e-Nawaz Avenue, Sector 11, Uttara, Dhaka", "phone": "09613-737737", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Uttara, Dhaka"},
            {"branch_name": "Khilgaon Taltola", "area": "Khilgaon", "exact_address": "Shahid Baki Road, Taltola, Khilgaon, Dhaka", "phone": "09613-737737", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Khilgaon, Dhaka"},
            {"branch_name": "Banasree", "area": "Khilgaon", "exact_address": "Block B, Banasree Main Road, Dhaka", "phone": "09613-737737", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Banasree, Dhaka"},
            {"branch_name": "Farmgate Indira Road", "area": "Panthapath", "exact_address": "Indira Road, Farmgate, Dhaka", "phone": "09613-737737", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Farmgate, Dhaka"},
            {"branch_name": "Old Dhaka Wari", "area": "Old Dhaka", "exact_address": "Avoy Das Lane, Tikatuli / Wari, Dhaka", "phone": "09613-737737", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Wari, Dhaka"},
            {"branch_name": "Old Dhaka Nazimuddin Road", "area": "Old Dhaka", "exact_address": "Nazimuddin Road, Chawkbazar area, Old Dhaka", "phone": "09613-737737", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Old Dhaka"}
        ]

    # BREAD & BEYOND (EXPAND TO 8 OUTLETS)
    elif rid == "bread-and-beyond":
        r["total_branches"] = 8
        r["branches"] = [
            {"branch_name": "Gulshan 1", "area": "Gulshan", "exact_address": "House 1, Road 138, Gulshan 1, Dhaka", "phone": "01788-990011", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Gulshan 1, Dhaka"},
            {"branch_name": "Banani Road 11", "area": "Banani", "exact_address": "Plot 54, Road 11, Banani, Dhaka", "phone": "01788-990011", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Banani, Dhaka"},
            {"branch_name": "Dhanmondi Road 8/A", "area": "Dhanmondi", "exact_address": "House 28, Road 8/A, Dhanmondi, Dhaka", "phone": "01788-990011", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Dhanmondi 27", "area": "Dhanmondi", "exact_address": "Road 27 (Old), Dhanmondi, Dhaka", "phone": "01788-990011", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Uttara Sector 4", "area": "Uttara", "exact_address": "Shahjalal Avenue, Sector 4, Uttara, Dhaka", "phone": "01788-990011", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Uttara, Dhaka"},
            {"branch_name": "Uttara Sector 11", "area": "Uttara", "exact_address": "Gareeb-e-Nawaz Avenue, Sector 11, Uttara, Dhaka", "phone": "01788-990011", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Uttara, Dhaka"},
            {"branch_name": "Mirpur 2 Mirpur DOHS", "area": "Mirpur", "exact_address": "Mirpur Shopping Center area, Mirpur 2, Dhaka", "phone": "01788-990011", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Mirpur 2, Dhaka"},
            {"branch_name": "Bashundhara R/A", "area": "Bashundhara", "exact_address": "Main Gate, Block B, Bashundhara R/A, Dhaka", "phone": "01788-990011", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Bashundhara, Dhaka"}
        ]

    # SHUMI'S HOT CAKE (EXPAND TO 10 OUTLETS)
    elif rid == "shumis-hot-cake":
        r["total_branches"] = 10
        r["branches"] = [
            {"branch_name": "Gulshan 2", "area": "Gulshan", "exact_address": "House 12, Road 53, Gulshan 2, Dhaka", "phone": "02-9887766", "opening_hours": "09:00 AM - 10:30 PM", "map_location": "Gulshan 2, Dhaka"},
            {"branch_name": "Banani Road 11", "area": "Banani", "exact_address": "Road 11, Block D, Banani, Dhaka", "phone": "02-9887766", "opening_hours": "09:00 AM - 10:30 PM", "map_location": "Banani, Dhaka"},
            {"branch_name": "Dhanmondi Road 27", "area": "Dhanmondi", "exact_address": "Road 27 (Old), Near Shatabdi Bhaban, Dhanmondi, Dhaka", "phone": "02-9887766", "opening_hours": "09:00 AM - 10:30 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Dhanmondi Road 5", "area": "Dhanmondi", "exact_address": "Mirpur Road, Near Road 5, Dhanmondi, Dhaka", "phone": "02-9887766", "opening_hours": "09:00 AM - 10:30 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Uttara Sector 3", "area": "Uttara", "exact_address": "Rabindra Sarani, Sector 3, Uttara, Dhaka", "phone": "02-9887766", "opening_hours": "09:00 AM - 10:30 PM", "map_location": "Uttara, Dhaka"},
            {"branch_name": "Uttara Sector 7", "area": "Uttara", "exact_address": "Sector 7, Jashimuddin Avenue, Uttara, Dhaka", "phone": "02-9887766", "opening_hours": "09:00 AM - 10:30 PM", "map_location": "Uttara, Dhaka"},
            {"branch_name": "Bailey Road", "area": "Bailey Road", "exact_address": "Bailey Road Commercial Area, Dhaka", "phone": "02-9887766", "opening_hours": "09:00 AM - 10:30 PM", "map_location": "Bailey Road, Dhaka"},
            {"branch_name": "Mohammadpur", "area": "Mohammadpur", "exact_address": "Tajmahal Road, Mohammadpur, Dhaka", "phone": "02-9887766", "opening_hours": "09:00 AM - 10:30 PM", "map_location": "Mohammadpur, Dhaka"},
            {"branch_name": "Mirpur 10", "area": "Mirpur", "exact_address": "Section 10 Circle, Mirpur, Dhaka", "phone": "02-9887766", "opening_hours": "09:00 AM - 10:30 PM", "map_location": "Mirpur 10, Dhaka"},
            {"branch_name": "Old Dhaka Wari", "area": "Old Dhaka", "exact_address": "Rankin Street, Wari, Dhaka", "phone": "02-9887766", "opening_hours": "09:00 AM - 10:30 PM", "map_location": "Wari, Dhaka"}
        ]

    # NORTH END COFFEE ROASTERS (EXPAND TO 8 OUTLETS)
    elif rid == "north-end-coffee":
        r["total_branches"] = 8
        r["branches"] = [
            {"branch_name": "Pragati Sarani (Flagship Roastery)", "area": "Gulshan", "exact_address": "KHA-47 Pragati Sarani, Shahjadpur, Gulshan, Dhaka", "phone": "01730-058866", "opening_hours": "07:30 AM - 11:00 PM", "map_location": "Gulshan, Dhaka"},
            {"branch_name": "Banani Road 11", "area": "Banani", "exact_address": "Plot 54, Road 11, Banani, Dhaka", "phone": "01730-058866", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Banani, Dhaka"},
            {"branch_name": "Gulshan 2 (Pink City area)", "area": "Gulshan", "exact_address": "Plot 14, Road 103, Gulshan 2, Dhaka", "phone": "01730-058866", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Gulshan 2, Dhaka"},
            {"branch_name": "Dhanmondi Road 27", "area": "Dhanmondi", "exact_address": "Green Akshay Plaza, 1st Floor, Road 27 (Old), Dhanmondi, Dhaka", "phone": "01730-058866", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Dhanmondi, Dhaka"},
            {"branch_name": "Uttara Sector 11", "area": "Uttara", "exact_address": "Gareeb-e-Nawaz Avenue, Sector 11, Uttara, Dhaka", "phone": "01730-058866", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Uttara, Dhaka"},
            {"branch_name": "City Bank Center Cafe", "area": "Gulshan", "exact_address": "City Bank Center, 136 Gulshan Avenue, Dhaka", "phone": "01730-058866", "opening_hours": "08:30 AM - 08:00 PM", "map_location": "Gulshan Avenue, Dhaka"},
            {"branch_name": "Bashundhara R/A", "area": "Bashundhara", "exact_address": "Block C, Near Independent University Bangladesh (IUB), Bashundhara R/A, Dhaka", "phone": "01730-058866", "opening_hours": "08:00 AM - 10:30 PM", "map_location": "Bashundhara, Dhaka"},
            {"branch_name": "Bailey Road", "area": "Bailey Road", "exact_address": "Officers Club area, New Bailey Road, Dhaka", "phone": "01730-058866", "opening_hours": "08:00 AM - 11:00 PM", "map_location": "Bailey Road, Dhaka"}
        ]

with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

with open(JS_FILE, "w", encoding="utf-8") as f:
    f.write("window.RESTAURANTS_DATA = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n")

print("Cooper's, Well Food, Mithai, Bread & Beyond, Shumi's, and North End branch networks expanded!")
