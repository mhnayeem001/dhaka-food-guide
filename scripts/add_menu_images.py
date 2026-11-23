"""
Add high-quality dish photography to all menu items in data/restaurants.json:
Classifies each item by name, category, and cuisine to attach relevant Unsplash food photos.
"""
import json
import os

IMAGE_MAPPINGS = [
    # Biryani, Kacchi, Rice
    (["kacchi", "kachchi", "mutton kacchi", "shahi mutton"], "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?auto=format&fit=crop&w=300&q=80"),
    (["tehari", "tahari", "beef tehari", "mustard oil"], "https://images.unsplash.com/photo-1589302168068-964664d93dc0?auto=format&fit=crop&w=300&q=80"),
    (["biryani", "briyani", "beef biryani"], "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?auto=format&fit=crop&w=300&q=80"),
    (["polao", "pulao", "morog polao", "chicken roast"], "https://images.unsplash.com/photo-1633945274405-b6c8069047b0?auto=format&fit=crop&w=300&q=80"),
    (["khichuri", "khichdi", "bhuna khichuri"], "https://images.unsplash.com/photo-1626777552726-4a6b54c97e46?auto=format&fit=crop&w=300&q=80"),
    (["rice", "bhaat", "fried rice", "jasmine rice"], "https://images.unsplash.com/photo-1516684732162-798a0062be99?auto=format&fit=crop&w=300&q=80"),

    # Burgers & Sandwiches
    (["zinger", "chicken burger", "crispy chicken burger", "crunchy"], "https://images.unsplash.com/photo-1625813506062-0aeb1d7a094b?auto=format&fit=crop&w=300&q=80"),
    (["smasher", "beef burger", "smash", "double beef", "patty"], "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=300&q=80"),
    (["burger", "cheeseburger"], "https://images.unsplash.com/photo-1586190848861-99aa4a171e90?auto=format&fit=crop&w=300&q=80"),
    (["sandwich", "panini", "sub", "club sandwich"], "https://images.unsplash.com/photo-1528735602780-2552fd46c7af?auto=format&fit=crop&w=300&q=80"),
    (["wrap", "shawarma", "roll"], "https://images.unsplash.com/photo-1626700051175-6818013e1d4f?auto=format&fit=crop&w=300&q=80"),

    # Fried Chicken, Wings & Fries
    (["chicken bucket", "fried chicken", "broast", "hot & crispy", "crispy"], "https://images.unsplash.com/photo-1626645738196-c2a7c87a8f58?auto=format&fit=crop&w=300&q=80"),
    (["wings", "buffalo wings", "naga wings", "bbq wings"], "https://images.unsplash.com/photo-1567620832903-9fc6debc209f?auto=format&fit=crop&w=300&q=80"),
    (["nugget", "popcorn", "strips", "finger"], "https://images.unsplash.com/photo-1562967914-608f82629710?auto=format&fit=crop&w=300&q=80"),
    (["fries", "french fries", "poutine", "potato"], "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?auto=format&fit=crop&w=300&q=80"),

    # Pizza & Pasta
    (["pepperoni", "pizza", "pizza slice", "meaty"], "https://images.unsplash.com/photo-1628840042765-356cda07504e?auto=format&fit=crop&w=300&q=80"),
    (["margherita", "cheese pizza", "four cheese"], "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=300&q=80"),
    (["baked pasta", "oven baked", "lasagna"], "https://images.unsplash.com/photo-1551183053-bf91a1d81141?auto=format&fit=crop&w=300&q=80"),
    (["pasta", "fettuccine", "spaghetti", "penne", "alfredo"], "https://images.unsplash.com/photo-1621996346565-e3d5d628178a?auto=format&fit=crop&w=300&q=80"),

    # Kebabs, Tandoor & Chaap
    (["boti", "seekh", "kebab", "tikka", "grill"], "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?auto=format&fit=crop&w=300&q=80"),
    (["tandoori", "peri-peri", "grilled chicken", "charbroiled"], "https://images.unsplash.com/photo-1610057099443-fde8c4d50f91?auto=format&fit=crop&w=300&q=80"),
    (["chaap", "chap", "tawa chaap", "brain fry"], "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=300&q=80"),
    (["naan", "paratha", "porota", "luchi", "ruti", "bread"], "https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=300&q=80"),

    # Asian, Dim Sum, Sushi & Ramen
    (["dim sum", "siu mai", "dumpling", "momo", "wonton", "gyoza"], "https://images.unsplash.com/photo-1496116218417-1a781b1c416c?auto=format&fit=crop&w=300&q=80"),
    (["sushi", "maki", "sashimi", "california roll", "nigiri"], "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?auto=format&fit=crop&w=300&q=80"),
    (["ramen", "soup noodle", "noodle soup"], "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=300&q=80"),
    (["noodle", "chow mein", "pad thai"], "https://images.unsplash.com/photo-1585032226651-759b368d7246?auto=format&fit=crop&w=300&q=80"),
    (["tom yum", "soup", "corn soup", "clear soup", "thai soup"], "https://images.unsplash.com/photo-1548946526-f69e2424cf45?auto=format&fit=crop&w=300&q=80"),

    # Bengali Traditional & Curries
    (["ilish", "hilsha", "fish", "ruy", "chingri", "prawn", "seafood"], "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?auto=format&fit=crop&w=300&q=80"),
    (["kala bhuna", "beef bhuna", "rezala", "glash", "curry", "duck", "haash"], "https://images.unsplash.com/photo-1545247181-516773cae754?auto=format&fit=crop&w=300&q=80"),
    (["bhorta", "vorta", "shutki", "daal", "dal"], "https://images.unsplash.com/photo-1610057099431-d73a1c9d2f2f?auto=format&fit=crop&w=300&q=80"),

    # Steaks
    (["steak", "ribeye", "sirloin", "tenderloin"], "https://images.unsplash.com/photo-1558030006-450675393462?auto=format&fit=crop&w=300&q=80"),

    # Desserts, Sweets & Bakery
    (["roshomalai", "rasmalai", "chomchom", "rosgulla", "laddu", "sweet", "mithai", "sandesh"], "https://images.unsplash.com/photo-1599785209707-a456fc1337bb?auto=format&fit=crop&w=300&q=80"),
    (["doi", "dahi", "yogurt", "curd"], "https://images.unsplash.com/photo-1488477181946-6428a0291777?auto=format&fit=crop&w=300&q=80"),
    (["cake", "pastry", "cheesecake", "red velvet", "black forest"], "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=300&q=80"),
    (["brownie", "lava cake", "waffle", "donut", "ice cream"], "https://images.unsplash.com/photo-1606313564200-e75d5e30476c?auto=format&fit=crop&w=300&q=80"),
    (["patty", "patties", "croissant", "puff", "bagel", "biscuit", "toast"], "https://images.unsplash.com/photo-1555507036-ab1f4038808a?auto=format&fit=crop&w=300&q=80"),
    (["fuchka", "fuska", "chotpoti", "shingara", "somosa", "puri"], "https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=300&q=80"),

    # Drinks, Coffees & Beverages
    (["cappuccino", "latte", "espresso", "americano", "coffee", "mocha"], "https://images.unsplash.com/photo-1534778101976-62847782c213?auto=format&fit=crop&w=300&q=80"),
    (["iced coffee", "cold brew", "frappe", "chiller"], "https://images.unsplash.com/photo-1517701550927-30cf4ba1dba5?auto=format&fit=crop&w=300&q=80"),
    (["borhani", "burhani"], "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=300&q=80"),
    (["lassi", "faluda", "shake", "milkshake", "smoothie"], "https://images.unsplash.com/photo-1572490122747-3968b75cc699?auto=format&fit=crop&w=300&q=80"),
    (["tea", "chai", "mojito", "lemonade", "juice", "beverage", "drink", "soda"], "https://images.unsplash.com/photo-1576092768241-dec231879fc3?auto=format&fit=crop&w=300&q=80")
]

DEFAULT_FOOD_IMAGE = "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=300&q=80"

def get_dish_image(item_name, cat_name):
    text = f"{item_name} {cat_name}".lower()
    for keywords, url in IMAGE_MAPPINGS:
        if any(kw in text for kw in keywords):
            return url
    return DEFAULT_FOOD_IMAGE

def add_images():
    db_path = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants.json")
    with open(db_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    total_items = 0
    for r in data:
        for cat in r.get("menu_categories", []):
            cat_name = cat.get("category") or cat.get("category_name") or ""
            for item in cat.get("items", []):
                item_name = item.get("name", "")
                item["image"] = get_dish_image(item_name, cat_name)
                total_items += 1

    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    js_path = os.path.join(os.path.dirname(__file__), "..", "data", "restaurants_data.js")
    with open(js_path, "w", encoding="utf-8") as f:
        f.write("window.RESTAURANTS_DATA = " + json.dumps(data, ensure_ascii=False, indent=2) + ";\n")

    print(f"Successfully attached dish photography to all {total_items} menu items!")

if __name__ == "__main__":
    add_images()
