# Dhaka Food Guide (DhakaFood AI) 🍽️
> **All Dhaka Restaurant Menus, Exact Outlets, GPS Proximity & 100% Verified Counter Rates in One Place.**

**Dhaka Food Guide** is a modern, high-performance web platform built for Dhaka foodies. Instead of navigating marked-up delivery aggregators, users can explore official dine-in counter menus, exact prices in BDT (৳), and all branch locations with real-time GPS proximity and an intelligent AI assistant.

---

## 🌟 Key Features

- **🤖 DhakaFood AI Assistant:** Production-grade NLP taxonomy engine with restaurant entity resolution, zero-hallucination intent gating, and natural Bengali/Banglish review answering.
- **🧭 GPS Near Me Engine:** Real-time distance calculation to the nearest branch across Dhaka using the Haversine formula with instant Google Maps directions.
- **⚖️ Side-by-Side Menu Comparator:** Compare menu items, pricing, branch counts, and ratings head-to-head.
- **🎲 Food Decision Wheel ("আজ কি খাব?"):** Interactive decision spinner with area and budget constraints.
- **🧾 Live Bill Splitter & Thermal POS Cash Memo:** Add items directly from menus with quantity steppers (`[-] Qty [+]`), calculate 5% VAT and delivery fees, and share itemized split receipts with friends.
- **🛡️ 100% Anti-Markup Price Guarantee:** Official in-store counter pricing across all 505 restaurants and 4,688 dishes.
- **⚡ Cloudflare & PWA Ready:** Service worker caching, mobile-optimized responsive design, offline support.

---

## 📂 Project Structure
```
├── data/
│   ├── restaurants.json          # Master database of 505 restaurants & 1,023 branches
│   └── restaurants_data.js       # Offline browser fallback script
├── scripts/
│   ├── verify_ai_precision.py    # Automated Playwright test suite for AI Assistant
│   ├── audit_landmarks_and_names.py # Database auditor & normalizer
│   └── scrape_engine.py         # Data analytics & verification engine
├── index.html                   # High-performance, modern single-page application
├── start_server.py              # Local HTTP development server
├── manifest.json                # PWA manifest
├── sw.js                        # Service worker for offline caching
└── README.md                    # Project documentation
```

---

## 🚀 How to Run the App

### Option 1 (Instant — Zero Installation):
Simply double-click `index.html` in your file explorer to open it in Chrome, Edge, or Firefox.

### Option 2 (Via Local Server):
Run the included python server:
```bash
python start_server.py
```
Then visit: `http://localhost:5000`

---

## 📊 Current Database Snapshot
- **Total Featured Restaurants:** 505 Iconic Chains, Fine Dining Hubs, Cafes & Heritage Eateries
- **Total Branches Documented in Dhaka:** 1,023 Outlets
- **Total Menu Items with Verified Counter Prices:** 4,688 Items (Cross-checked with Official In-store Counter Rates)
- **Covered Areas with Dedicated Filters:** Dhanmondi, Banani, Gulshan, Uttara, Mirpur, Bailey Road, Khilgaon, Bashundhara, Mohammadpur, Motijheel, Purana Paltan, Old Dhaka, Panthapath, Baridhara.
