import json, re

with open('data/restaurants.json', 'r', encoding='utf-8') as f:
    restaurants = json.load(f)

# Common brand aliases mapped to canonical search keywords or ID prefixes
BRAND_ALIASES = {
    'chillox': 'chillox',
    'চিলক্স': 'chillox',
    'sultans dine': "sultan's dine",
    'sultan dine': "sultan's dine",
    "sultan's dine": "sultan's dine",
    'সুলতানস ডাইন': "sultan's dine",
    'kacchi bhai': 'kacchi bhai',
    'কাচ্চি ভাই': 'kacchi bhai',
    'takeout': 'takeout',
    'টেকআউট': 'takeout',
    'pizza burg': 'pizza burg',
    'pizzaburg': 'pizza burg',
    'পিজ্জাবার্গ': 'pizza burg',
    'the pizza guy': 'the pizza guy',
    'pizza guy': 'the pizza guy',
    'khao san': 'khao san',
    'খাও সান': 'khao san',
    'thai emerald': 'thai emerald',
    'thai garden': 'thai garden',
    'north end': 'north end',
    'নর্থ এন্ড': 'north end',
    'gloria jeans': "gloria jean's",
    "gloria jean's": "gloria jean's",
    'crimson cup': 'crimson cup',
    'woodhouse': 'woodhouse grill',
    'farmhouse burger': 'farmhouse burger',
    'farmhouse': 'farmhouse burger',
    'madchef': 'madchef',
    'ম্যাডশেফ': 'madchef',
    'herfy': 'herfy',
    'star kabab': 'star kabab',
    'স্টার কাবাব': 'star kabab',
    'shad tehari': 'shad tehari',
    'স্বাদ তেহারি': 'shad tehari',
    'bismillah kabab': 'bismillah kabab',
    'dim sum town': 'dim sum town',
    'mainland china': 'mainland china',
    'secret recipe': 'secret recipe',
    'mr baker': 'mr. baker',
    'coopers': "cooper's",
    'kasturi': 'kasturi',
    'dominos': "domino's",
    'pizza hut': 'pizza hut',
    'kfc': 'kfc',
    'bfc': 'bfc'
}

def find_target_restaurant(q):
    q_lower = q.lower().strip()
    
    # 1. Check direct aliases first
    for alias, target in sorted(BRAND_ALIASES.items(), key=lambda x: len(x[0]), reverse=True):
        pattern = r'(?:\b|^|\s)' + re.escape(alias) + r'(?:\b|$|\s|[?.,!])'
        if re.search(pattern, q_lower):
            # Find restaurant in data
            for r in restaurants:
                if target in r['name'].lower() or r['id'].startswith(target.replace(' ', '-').replace("'", "")):
                    return r

    # 2. Check full restaurant names in dataset (at least 5 characters)
    for r in sorted(restaurants, key=lambda x: len(x['name']), reverse=True):
        r_name_clean = r['name'].lower().replace("'", "").replace(".", "")
        if len(r_name_clean) >= 6:
            pattern = r'(?:\b|^|\s)' + re.escape(r_name_clean) + r'(?:\b|$|\s|[?.,!])'
            if re.search(pattern, q_lower.replace("'", "").replace(".", "")):
                return r

    return None

queries = [
    'chillox er burger kemon?',
    'sultans dine kacchi kemon?',
    'sultan dine e kacchi koto?',
    'takeout burger kemon hobe?',
    'khao san er thai food kemon?',
    'north end coffee kemon?',
    'pizza burg er pizza kemon?',
    'uttarar best thai foods er restaurant konta?'
]

for q in queries:
    matched = find_target_restaurant(q)
    print(f'Query: "{q}" --> Matched: {matched["name"] if matched else "None"}')
