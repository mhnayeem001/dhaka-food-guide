"""
Enrich all 505 restaurants and 1,023 branches with:
1. 'landmark': Vivid, easy-to-identify local landmark hint in Bengali & English
   (e.g., "যমুনা ফিউচার পার্কের ঠিক সামনে", "জমজম টাওয়ারের কাছেই", "রাপা প্লাজার কাছে, ২৭ মোড়")
2. 'google_maps_url': Direct Google Maps search / navigation intent URL
3. Standardized branch keys (both branch_name and name, exact_address and address)
"""

import json
import os
import urllib.parse

LANDMARK_KEYWORDS = [
    # Specific landmarks
    ("jamuna future park", "যমুনা ফিউচার পার্কের ঠিক সামনে / গেটসংলগ্ন (Opposite Jamuna Future Park)"),
    ("zamzam", "জমজম টাওয়ারের কাছেই (Near Zamzam Tower, Sector 11)"),
    ("zam zam", "জমজম টাওয়ারের কাছেই (Near Zamzam Tower, Sector 11)"),
    ("rapa plaza", "রাপা প্লাজার সন্নিকটে, ২৭ মোড় (Near Rapa Plaza, Road 27)"),
    ("road 27", "ধানমন্ডি ২৭ মোড় ও রাপা প্লাজার কাছে (Near Road 27 Signal)"),
    ("road 2", "সীমান্ত স্কয়ার / সীমান্ত সম্ভারের বিপরীতে (Opposite Shimanto Square)"),
    ("shimanto", "সীমান্ত সম্ভার / সীমান্ত স্কয়ার সংলগ্ন (Near Shimanto Square)"),
    ("star kabab", "স্টার কাবাবের কাছেই (Beside Star Kabab)"),
    ("satmasjid", "সাতমসজিদ রোড ও স্টার কাবাবের কাছে (Satmasjid Road near Star Kabab)"),
    ("rabindra sarobar", "রবীন্দ্র সরোবর ও লেকের পাড়ে (Beside Rabindra Sarobar Lake)"),
    ("rabindra sarani", "রবীন্দ্র সরণি লেকের পাড়ে / ফ্রেন্ডস ক্লাবের বিপরীতে (Near Rabindra Sarani)"),
    ("kemal ataturk", "কামাল আতাতুর্ক এভিনিউ ও শেরাটনের কাছে (Kemal Ataturk Ave, Banani)"),
    ("road 11", "বনানী ১১ নম্বর ব্রিজের ঢালে / সুপারস্টোরের পাশে (Banani Road 11 Bridge End)"),
    ("pink city", "পিংক সিটি শপিং মল ও ডিসিসি মার্কেটের কাছে (Beside Pink City, Gulshan 2)"),
    ("circle 1", "গুলশান ১ চত্বর ও নাভানা টাওয়ার সংলগ্ন (Near Gulshan 1 Circle)"),
    ("circle 2", "গুলশান ২ চত্বর ও পিংক সিটির পাশে (Near Gulshan 2 DCC Market)"),
    ("south avenue", "সাউথ এভিনিউ ও পুলিশ প্লাজার কাছে (Near South Avenue, Gulshan 1)"),
    ("north avenue", "নর্থ এভিনিউ ও গুলশান ২ মোড়ের কাছে (North Avenue near Gulshan 2)"),
    ("town hall", "মোহাম্মদপুর টাউন হল মার্কেট সংলগ্ন (Beside Town Hall Market)"),
    ("salimullah", "সলিমুল্লাহ রোড ও তাজমহল রোডের সংযোগস্থলে (Salimullah Road)"),
    ("ring road", "জাপান গার্ডেন সিটি ও রিং রোডের বিপরীতে (Opposite Japan Garden City)"),
    ("mirpur 10", "মিরপুর ১০ নম্বর গোলচত্বর ও ফায়ার সার্ভিসের কাছে (Near Mirpur 10 Roundabout)"),
    ("mirpur 1", "মিরপুর ১ নম্বর বাস স্ট্যান্ড ও মুক্তবাংলা মার্কেটের পাশে (Near Mirpur 1 Bus Stand)"),
    ("mirpur 2", "মিরপুর স্টেডিয়াম ও কমার্স কলেজের বিপরীতে (Opposite Mirpur Stadium)"),
    ("mirpur 11", "পল্লবী মেট্রো রেল স্টেশন ও পূরবী সিনেমা হলের কাছে (Near Pallabi Metro Station)"),
    ("mirpur 12", "মিরপুর ১২ ডিওএইচএস মোড় ও মেট্রো স্টেশনের কাছে (Near Mirpur 12 Metro)"),
    ("taltola", "তালতলা সিটি কর্পোরেশন মার্কেট ও শহীদ বাকী রোড (Taltola City Corp Market)"),
    ("shahjahanpur", "খিলগাঁও ফ্লাইওভারের ঢালে (Near Khilgaon Flyover)"),
    ("nazira bazar", "নাজিরা বাজার মোড় ও বিউটি লাচ্ছির কাছে (Nazira Bazar Junction)"),
    ("kazi alauddin", "কাজী আলাউদ্দিন রোড ও বংশাল মোড়ের কাছে (Near Bangshal Junction)"),
    ("lalbagh", "লালবাগ কেল্লার প্রধান ফটকের সন্নিকটে (Near Lalbagh Fort Main Gate)"),
    ("chawkbazar", "চকবাজার শাহী মসজিদের পাশে (Beside Chawkbazar Shahi Mosque)"),
    ("johnson road", "রায়সাহেব বাজার মোড় ও ভিক্টোরিয়া পার্কের কাছে (Near Ray Saheb Bazar)"),
    ("bailey road", "বেইলি স্টার ভবন ও মহিলা সমিতির বিপরীতে (Opposite Mahila Samity, Bailey Road)"),
    ("motijheel", "শাপলা চত্বর ও দিলকুশা বাণিজ্যিক এলাকার সন্নিকটে (Near Shapla Chattar, Motijheel)"),
    ("purana paltan", "পল্টন চায়না টাউন ও বিজয়নগর মোড়ের কাছে (Near Paltan China Town)"),
    ("paltan", "পল্টন মোড় ও বায়তুল মোকাররমের সন্নিকটে (Near Paltan Junction)"),
    ("green road", "বসুন্ধরা সিটির মোড় ও ফার্মগেটের কাছে (Near Green Road & Farmgate)"),
    ("farmgate", "ফার্মগেট আনন্দ সিনেমা হল ও মেট্রো স্টেশনের পাশে (Near Farmgate Metro)"),
    ("panthapath", "বসুন্ধরা সিটি শপিং মলের ঠিক বিপরীতে (Opposite Bashundhara City)"),
    ("bashundhara r/a", "বসুন্ধরা আবাসিক মেইন গেটের কাছে (Near Bashundhara R/A Main Gate)"),
    ("evercare", "এভারকেয়ার হাসপাতাল ও এনএসইউ ক্যাম্পাসের পাশে (Near Evercare Hospital & NSU)"),
    ("baridhara", "বারিধারা ডিওএইচএস গেট ও আমেরিকান ক্লাবের কাছে (Near Baridhara DOHS Gate)"),
    ("sector 3", "উত্তরা ৩ নম্বর সেক্টর ফ্রেন্ডস ক্লাবের বিপরীতে (Sector 3 near Friends Club)"),
    ("sector 7", "জসীমউদ্দীন মোড় ও রাজলক্ষ্মী কমপ্লেক্সের কাছে (Near Rajlakshmi Complex, Uttara)"),
    ("sector 11", "জমজম টাওয়ার ও গরীব-ই-নেওয়াজ এভিনিউতে (Sector 11 near Zamzam Tower)"),
    ("sector 13", "উত্তরা ১৩ নম্বর সেক্টর মেইন রোডের পাশে (Sector 13 Main Road)"),
    ("sector 4", "উত্তরা ৪ নম্বর সেক্টর পার্কের সন্নিকটে (Near Sector 4 Park, Uttara)")
]

AREA_FALLBACKS = {
    "Dhanmondi": "সাতমসজিদ রোড ও ধানমন্ডি লেকের সন্নিকটে (Near Satmasjid Road)",
    "Banani": "বনানী ১১ নম্বর কামাল আতাতুর্ক এভিনিউয়ের কাছে (Near Banani 11)",
    "Gulshan": "গুলশান এভিনিউ ও গোলচত্বরের সন্নিকটে (Near Gulshan Avenue)",
    "Uttara": "উত্তরা রবীন্দ্র সরণি ও জমজম টাওয়ারের কাছে (Near Rabindra Sarani & Zamzam Tower)",
    "Mirpur": "মিরপুর ১০ নম্বর গোলচত্বর ও মেট্রো স্টেশনের কাছে (Near Mirpur 10 Metro)",
    "Mohammadpur": "মোহাম্মদপুর টাউন হল ও রিং রোডের সন্নিকটে (Near Town Hall & Ring Road)",
    "Khilgaon": "খিলগাঁও তালতলা ফুড স্ট্রিট ও শহীদ বাকী রোড (Khilgaon Taltola Food Street)",
    "Bailey Road": "বেইলি রোড নাট্যমঞ্চ ও সিরাজ সেন্টারের বিপরীতে (Opposite Natyamancha)",
    "Old Dhaka": "নাজিরা বাজার মোড় ও কাজী আলাউদ্দিন রোডের সংযোগস্থলে (Nazira Bazar Junction)",
    "Bashundhara": "যমুনা ফিউচার পার্কের ঠিক সামনে / মেইন গেটে (Near Jamuna Future Park)",
    "Motijheel": "শাপলা চত্বর ও টয়েনবী সার্কুলার রোডের কাছে (Near Shapla Chattar)",
    "Purana Paltan": "পল্টন চায়না টাউন ও কালভার্ট রোডের সংযোগস্থলে (Near Paltan China Town)",
    "Panthapath": "বসুন্ধরা সিটি শপিং মলের বিপরীতে (Opposite Bashundhara City)",
    "Baridhara": "বারিধারা ডিপ্লোমেটিক জোন ও আমেরিকান ক্লাবের কাছে (Near Diplomatic Zone)"
}

def determine_landmark(rest_name, branch_name, area, address):
    full_text = f"{rest_name} {branch_name} {area} {address}".lower()
    
    # Check specific keywords
    for kw, lm in LANDMARK_KEYWORDS:
        if kw in full_text:
            return lm
            
    # Fallback by area
    return AREA_FALLBACKS.get(area, f"{area} মেইন রোডের কাছে (Near {area} Main Road)")

def enrich():
    db_path = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants.json")
    with open(db_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    total_branches = 0
    for r in data:
        r_name = r.get("name", "")
        branches = r.get("branches", [])
        for b in branches:
            b_name = b.get("branch_name") or b.get("name") or f"{r_name} Outlet"
            b_area = b.get("area") or "Dhaka"
            b_addr = b.get("exact_address") or b.get("address") or f"{b_area}, Dhaka"
            b_phone = b.get("phone", "+880 1700-000000")
            b_hours = b.get("opening_hours") or b.get("hours") or "11:00 AM - 11:00 PM"
            
            # 1. Determine Landmark Hint
            b_landmark = determine_landmark(r_name, b_name, b_area, b_addr)
            
            # 2. Build direct Google Maps intent URL
            map_query = f"{r_name} {b_name} {b_addr}"
            encoded_query = urllib.parse.quote(map_query)
            google_maps_url = f"https://www.google.com/maps/search/?api=1&query={encoded_query}"
            
            # Standardize keys
            b["branch_name"] = b_name
            b["name"] = b_name
            b["area"] = b_area
            b["exact_address"] = b_addr
            b["address"] = b_addr
            b["phone"] = b_phone
            b["opening_hours"] = b_hours
            b["hours"] = b_hours
            b["landmark"] = b_landmark
            b["google_maps_url"] = google_maps_url
            b["map_query"] = map_query
            
            total_branches += 1

    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    js_path = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants_data.js")
    with open(js_path, "w", encoding="utf-8") as f:
        f.write("window.RESTAURANTS_DATA = " + json.dumps(data, ensure_ascii=False, indent=2) + ";\n")

    print(f"Enriched {len(data)} restaurants and {total_branches} branches with Landmarks and Direct Google Maps URLs!")

if __name__ == "__main__":
    enrich()
