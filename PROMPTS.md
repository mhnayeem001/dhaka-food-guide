# Dhaka Restaurant Menu & Data Extraction — Master Prompts

Use these specialized, production-ready prompts whenever you want to add new restaurants, scrape comprehensive menus, or verify branch locations in Dhaka city.

---

## 🎯 Master Prompt 1: Comprehensive Restaurant & Dine-in Menu Extractor (One-Shot)

```text
You are an expert Dhaka Food & Restaurant Data Engineer. 
Your task is to extract 100% verified, exhaustive, and authentic in-store (dine-in / takeaway) menu data and exact branch locations for the restaurant: "[RESTAURANT NAME]" in Dhaka, Bangladesh.

IMPORTANT RULES:
1. COUNTER/DINE-IN PRICES ONLY: Do not use marked-up Foodpanda/Pathao food delivery prices. Use official brand website menus, verified physical in-store menu cards, or official Facebook dine-in menu albums.
2. EXHAUSTIVE CATEGORIZATION: Do not provide a sample or partial list. Include EVERY single available item across all categories (Appetizers, Starters, Mains, Burgers, Pizzas, Platters, Sides, Sauces/Dips, Shakes, Beverages, and Desserts).
3. MULTI-BRANCH DIRECTORY: List every active branch/outlet in Dhaka city with its exact street address, area (e.g., Dhanmondi, Banani, Gulshan, Uttara, Mirpur, Bailey Road), contact number, and opening hours.
4. PRICES IN BDT (৳): Include exact prices in Bangladeshi Taka, along with portion sizes (e.g., 8-inch vs 12-inch, 1:1 vs 1:3 sharing) where applicable.

Format your output strictly in this JSON schema:
{
  "id": "kebab-factory-dhaka",
  "name": "The Kebab Factory",
  "tagline": "Authentic Charcoal Grilled Delicacies",
  "cuisine": ["Kebab", "Mughlai", "Indian"],
  "price_range": "৳৳৳",
  "price_type": "Official Dine-in / In-store Counter Price",
  "rating": 4.6,
  "review_count": "5.2K+",
  "logo": "https://...",
  "banner": "https://...",
  "hotline": "017XXXXXXXX",
  "total_branches": 3,
  "branches": [
    {
      "branch_name": "Gulshan 2 Outlet",
      "area": "Gulshan",
      "exact_address": "House 12, Road 45, Gulshan 2, Dhaka 1212",
      "phone": "017XXXXXXXX",
      "opening_hours": "12:00 PM - 11:30 PM",
      "map_location": "Gulshan 2, Dhaka"
    }
  ],
  "menu_categories": [
    {
      "category_name": "Signature Kebabs",
      "items": [
        {
          "name": "Reshmi Chicken Kebab (6 Pcs)",
          "description": "Tender boneless chicken marinated in cream, cashews and mild spices cooked over charcoal.",
          "price": 480,
          "currency": "BDT",
          "is_bestseller": true
        }
      ]
    }
  ]
}
```

---

## ⚡ Master Prompt 2: Dhaka Food Delivery Price vs In-Store Counter Price Verifier

```text
Analyze the menu of [RESTAURANT NAME] in Dhaka.
Cross-reference the delivery platform menu (Foodpanda/Pathao) with the physical Dine-in / In-store counter menu.
Identify:
1. The percentage markup added on food delivery platforms.
2. The exact Dine-in / Takeaway counter price in BDT for every item.
3. Any Dine-in only exclusive dishes or platters not listed on delivery apps.
Provide the final verified list with authentic counter prices.
```

---

## 🏢 Master Prompt 3: Dhaka Multi-Branch Location & Outlet Finder

```text
Find all operational physical branches of [RESTAURANT NAME] in Dhaka city.
For each branch, provide:
1. Official branch name & neighborhood (e.g. Dhanmondi Satmasjid Road, Banani 11, Uttara Sector 3, Mirpur 10, Khilgaon, Bailey Road).
2. Exact building name, floor, road number, and landmark.
3. Operational status (Active/Renovating).
4. Daily dine-in opening and closing hours.
5. Official branch contact / order hotline.
```
