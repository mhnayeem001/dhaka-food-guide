import json, re

with open('scripts/add_menu_images.py', 'r', encoding='utf-8') as f:
    content = f.read()

urls = re.findall(r'https://images\.unsplash\.com/[^\s\"\')]+', content)
print(f'Total URLs in add_menu_images.py: {len(urls)}')
for u in sorted(set(urls)):
    print(u)
