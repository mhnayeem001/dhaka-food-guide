import json, re

with open('data/restaurants.json', 'r', encoding='utf-8') as f:
    restaurants = json.load(f)

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
    'pizza burg': 'pizzaburg',
    'pizzaburg': 'pizzaburg',
    'পিজ্জাবার্গ': 'pizzaburg',
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
    'herfy': 'herfy',
    'star kabab': 'star kabab',
    'shad tehari': 'shad tehari',
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
    for alias, target in sorted(BRAND_ALIASES.items(), key=lambda x: len(x[0]), reverse=True):
        pattern = r'(?:\b|^|\s)' + re.escape(alias) + r'(?:\b|$|\s|[?.,!])'
        if re.search(pattern, q_lower):
            for r in restaurants:
                r_clean = r['name'].lower().replace("'", "").replace(".", "").replace(" ", "")
                t_clean = target.replace("'", "").replace(".", "").replace(" ", "")
                if t_clean in r_clean or target in r['name'].lower():
                    return r
    return None

q = 'chillox er burger kemon?'
r = find_target_restaurant(q)
print(f'Matched Restaurant: {r["name"] if r else "None"}')
if r:
    print('Rating:', r['rating'], 'Reviews:', r['review_count'])
    print('Cuisines:', r['cuisine'])
    print('Branches:', len(r['branches']), [b['area'] for b in r['branches']])
    items = [(i['name'], i['price']) for cat in r['menu_categories'] for i in cat['items']]
    print('Top items:', items[:3])
