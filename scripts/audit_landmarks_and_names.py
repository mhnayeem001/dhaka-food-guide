import json, re

with open('data/restaurants.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

AREA_LANDMARK_MAP = {
    'Dhanmondi': 'সাতমসজিদ রোড ও স্টার কাবাবের কাছে (Satmasjid Road near Star Kabab)',
    'Banani': 'বনানী ১১ নম্বর ব্রিজের ঢালে / সুপারস্টোরের পাশে (Banani Road 11 Bridge End)',
    'Gulshan': 'সাউথ এভিনিউ ও পুলিশ প্লাজার কাছে (Near South Avenue, Gulshan 1)',
    'Uttara': 'জমজম টাওয়ার ও গরীব-ই-নেওয়াজ এভিনিউতে (Sector 11 near Zamzam Tower)',
    'Mirpur': 'মিরপুর ১০ নম্বর গোলচত্বর ও ফায়ার সার্ভিসের কাছে (Near Mirpur 10 Roundabout)',
    'Old Dhaka': 'নাজিরাবাজার মোড় ও আল রাজ্জাকের কাছে (Nazira Bazar Crossing)',
    'Bashundhara': 'যমুনা ফিউচার পার্কের বিপরীতে ও গেটের কাছে (Near Jamuna Future Park)',
    'Mohammadpur': 'সলিমুল্লাহ রোড ও টাউন হলের বিপরীতে (Opposite Town Hall, Salimullah Road)',
    'Khilgaon': 'তালতলা মার্কেট ও শহীদ বাকী রোডে (Taltola Market, Shahid Baki Road)',
    'Bailey Road': 'বেইলি স্টার ভবন ও মহিলা সমিতির বিপরীতে (Opposite Mahila Samity, Bailey Road)',
    'Mohakhali': 'আমতলী মোড় ও ওয়্যারলেস গেটের কাছে (Near Amtoli Crossing)',
    'Panthapath': 'বসুন্ধরা সিটি শপিং মলের ঠিক বিপরীতে (Opposite Bashundhara City)'
}

# 1. Clean restaurant names: If a restaurant has branches in MULTIPLE areas, its name should NOT have a single branch in parentheses!
# e.g. "Kacchi Station (Panthapath)" with branches in Panthapath, Dhanmondi, Uttara -> Name should simply be "Kacchi Station"!
# If it only has branches in Panthapath, it's fine, but even then, clean brand names are better.
fixed_names = 0
fixed_landmarks = 0

for r in data:
    branches = r.get('branches', [])
    branch_areas = set(b.get('area', '') for b in branches)
    
    # Check if name has (Area)
    match = re.search(r'\s*\((Dhanmondi|Banani|Gulshan|Uttara|Mirpur|Old Dhaka|Bashundhara|Mohammadpur|Khilgaon|Bailey Road|Mohakhali|Panthapath)\)', r['name'], re.IGNORECASE)
    if match:
        area_in_name = match.group(1)
        # If the restaurant has branches in other areas, remove the area suffix from the restaurant name!
        if len(branch_areas) > 1 or list(branch_areas)[0].lower() != area_in_name.lower():
            old_name = r['name']
            r['name'] = re.sub(r'\s*\(' + re.escape(area_in_name) + r'\)', '', r['name'], flags=re.IGNORECASE).strip()
            fixed_names += 1
            print(f'Fixed Name: "{old_name}" --> "{r["name"]}" (Branches in {branch_areas})')

    # Ensure every branch has the CORRECT landmark matching its branch area!
    for b in branches:
        b_area = b.get('area', '')
        correct_landmark = AREA_LANDMARK_MAP.get(b_area)
        if correct_landmark:
            # Check if current landmark belongs to another area
            curr_lm = b.get('landmark', '')
            for other_area, other_lm in AREA_LANDMARK_MAP.items():
                if other_area != b_area and other_lm == curr_lm:
                    print(f"Fixing Landmark mismatch for {r['name']} ({b_area}): Was '{curr_lm}' --> '{correct_landmark}'")
                    b['landmark'] = correct_landmark
                    fixed_landmarks += 1
                    break

print(f'\nTotal Fixed Names: {fixed_names}')
print(f'Total Fixed Landmarks: {fixed_landmarks}')

with open('data/restaurants.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Saved cleaned data/restaurants.json successfully!')
