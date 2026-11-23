import sys
import time
from playwright.sync_api import sync_playwright

def test_all():
    print("Starting Comprehensive UI/UX Upgrades Verification...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1280, 'height': 800})
        page = context.new_page()
        
        # 1. Load Homepage
        page.goto('http://localhost:5000', wait_until='domcontentloaded')
        page.wait_for_timeout(1000)
        
        # Verify initial counts
        badge_text = page.locator('#results-count-badge').text_content().strip()
        print(f"Initial badge: {badge_text}")
        assert "505" in badge_text, f"Expected 505 in badge, got {badge_text}"
        
        # 2. Test Smart Curations (e.g. Iconic Kacchi)
        print("Testing Smart Filter: ICONIC_KACCHI...")
        page.click('#smart-btn-ICONIC_KACCHI')
        page.wait_for_timeout(400)
        kacchi_badge = page.locator('#results-count-badge').text_content().strip()
        print(f"Kacchi Filter Badge: {kacchi_badge}")
        kacchi_count = int(kacchi_badge.split()[0])
        assert kacchi_count > 0, "No kacchi restaurants returned"
        page.screenshot(path='screenshots/smart_filter_kacchi.png')
        
        # Reset filter
        page.click('#smart-btn-ICONIC_KACCHI')
        page.wait_for_timeout(400)
        
        # 3. Test Under ৳250 Budget filter
        print("Testing Smart Filter: BUDGET (Under ৳250)...")
        page.click('#smart-btn-BUDGET')
        page.wait_for_timeout(400)
        budget_badge = page.locator('#results-count-badge').text_content().strip()
        print(f"Budget Filter Badge: {budget_badge}")
        page.screenshot(path='screenshots/smart_filter_budget.png')
        page.click('#smart-btn-BUDGET')
        page.wait_for_timeout(400)
        
        # 4. Test Favorites & Badge in Navbar
        print("Testing Favorites toggling and navbar badge...")
        first_fav_btn = page.locator('button[aria-label^="Favorite"]').first
        first_fav_btn.click()
        page.wait_for_timeout(300)
        nav_fav = page.locator('#nav-fav-count').text_content().strip()
        print(f"Navbar Saved Count: {nav_fav}")
        assert nav_fav == "1", f"Expected 1 saved spot, got {nav_fav}"
        page.screenshot(path='screenshots/favorite_saved_badge.png')
        
        # 5. Open Restaurant Modal (e.g. Sultan's Dine)
        print("Opening Restaurant Modal...")
        page.fill('#search-input', "Sultan's Dine")
        page.wait_for_timeout(400)
        page.locator('button:has-text("Full Menu")').first.click()
        page.wait_for_timeout(600)
        
        # Check Anti-Markup Guarantee Badge
        guarantee_badge = page.locator('text=১০০% রিয়েল কাউন্টার রেট নিশ্চয়তা').first
        assert guarantee_badge.is_visible(), "Anti-markup guarantee badge not visible!"
        print("Anti-Markup Guarantee Badge is visible and verified!")
        
        # Check Modal In-Menu Quick Filter: Bestsellers
        print("Testing Modal Quick Filter: Bestsellers...")
        page.click('#modal-qf-BESTSELLER')
        page.wait_for_timeout(300)
        page.screenshot(path='screenshots/modal_bestsellers_filter.png')
        page.click('#modal-qf-ALL')
        page.wait_for_timeout(300)
        
        # 6. Test Interactive Dish Quantity Stepper & Add to Bill
        print("Testing Dish Quantity Stepper...")
        add_btn = page.locator('#modal-menu-categories button:has-text("Add")').first
        dish_card = page.locator('#modal-menu-categories > div > div > div').first
        dish_name = dish_card.locator('span.font-bold').first.text_content().strip()
        print(f"Adding dish: {dish_name}")
        
        add_btn.click()
        page.wait_for_timeout(300)
        
        # Quantity stepper should now show [ - ] 1 [ + ]
        stepper = page.locator('#modal-menu-categories div:has(button:has-text("+"))').first
        assert stepper.is_visible(), "Quantity stepper did not appear!"
        qty_text = stepper.locator('span.font-black').text_content().strip()
        assert qty_text == "1", f"Expected quantity 1, got {qty_text}"
        print(f"Stepper verified with quantity: {qty_text}")
        
        # Click + on stepper
        stepper.locator('button:has-text("+")').click()
        page.wait_for_timeout(300)
        qty_text_2 = stepper.locator('span.font-black').text_content().strip()
        assert qty_text_2 == "2", f"Expected quantity 2, got {qty_text_2}"
        print(f"Stepper incremented to: {qty_text_2}")
        
        page.screenshot(path='screenshots/dish_stepper_active.png')
        
        # 7. Check Bill Estimator Floating Bar
        bill_bar = page.locator('#modal-bill-bar')
        assert bill_bar.is_visible(), "Bill estimator bar not visible"
        total_price = page.locator('#bill-total-price').text_content().strip()
        vat_amount = page.locator('#bill-vat-amount').text_content().strip()
        print(f"Bill Bar: Total={total_price}, VAT={vat_amount}")
        
        # 8. Open Bill Breakdown & Group Splitter Modal
        print("Opening Bill Breakdown & Group Splitter...")
        page.locator('button:has-text("হিসাব ও ভাগ")').click()
        page.wait_for_timeout(400)
        
        split_modal = page.locator('#bill-share-modal')
        assert split_modal.is_visible(), "Bill share modal did not open"
        
        split_people = page.locator('#split-people-count').text_content().strip()
        per_person = page.locator('#split-per-person').text_content().strip()
        print(f"Splitter: {split_people} people -> {per_person}")
        
        # Adjust people count to 3
        page.locator('#bill-share-modal button:has-text("+")').last.click()
        page.wait_for_timeout(200)
        split_people_3 = page.locator('#split-people-count').text_content().strip()
        per_person_3 = page.locator('#split-per-person').text_content().strip()
        print(f"Adjusted to {split_people_3} people -> {per_person_3}")
        assert split_people_3 == "3", f"Expected 3 people, got {split_people_3}"
        
        page.screenshot(path='screenshots/bill_breakdown_splitter_modal.png')
        
        # Test Escape key closes modal
        print("Testing Escape key...")
        page.keyboard.press('Escape')
        page.wait_for_timeout(300)
        assert not split_modal.is_visible(), "Split modal should be closed by Escape"
        
        page.keyboard.press('Escape')
        page.wait_for_timeout(300)
        assert not page.locator('#restaurant-modal').is_visible(), "Restaurant modal should be closed by Escape"
        
        # 9. Test Mobile Viewport
        print("Testing Mobile Viewport (iPhone 14 Pro 390x844)...")
        mobile_page = context.new_page()
        mobile_page.set_viewport_size({'width': 390, 'height': 844})
        mobile_page.goto('http://localhost:5000', wait_until='domcontentloaded')
        mobile_page.wait_for_timeout(800)
        mobile_page.screenshot(path='screenshots/mobile_v2_home.png')
        
        # Open a card on mobile
        mobile_page.locator('button:has-text("Full Menu")').first.click()
        mobile_page.wait_for_timeout(600)
        mobile_page.screenshot(path='screenshots/mobile_v2_modal.png')
        
        print("\nALL PRODUCTION UI/UX UPGRADES VERIFIED SUCCESSFULLY! 100% PASS!")
        browser.close()

if __name__ == '__main__':
    test_all()
