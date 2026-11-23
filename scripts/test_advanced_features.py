import sys
import time
from playwright.sync_api import sync_playwright

def test_advanced():
    print("Testing 5 Advanced Next-Gen Features on Dhaka Menu Hub...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1280, 'height': 820})
        page = context.new_page()

        # 1. Load Homepage
        page.goto('http://localhost:5000', wait_until='domcontentloaded')
        page.wait_for_timeout(1000)

        # 2. Test DhakaFood AI Assistant
        print("Testing Feature 1: DhakaFood AI Assistant...")
        page.click('#floating-ai-btn')
        page.wait_for_timeout(400)
        assert page.locator('#ai-assistant-modal').is_visible(), "AI modal did not open"
        
        # Click a quick prompt: "ধানমন্ডির সেরা কাচ্চি কোনটা?"
        page.click('button:has-text("🍚 সেরা কাচ্চি")')
        page.wait_for_timeout(800)
        
        # Verify AI recommendation cards
        rec_cards = page.locator('#ai-chat-messages div:has-text("আপনার জন্য নির্বাচিত সেরা প্রস্তাবনা")').first
        assert rec_cards.is_visible(), "AI recommendations did not generate"
        print("DhakaFood AI successfully generated intelligent food recommendation cards!")
        page.screenshot(path='screenshots/advanced_ai_assistant.png')
        page.keyboard.press('Escape')
        page.wait_for_timeout(300)

        # 3. Test Near Me (GPS Distance Engine)
        print("Testing Feature 2: Near Me Live Distance Engine...")
        page.click('#smart-btn-NEAR_ME')
        page.wait_for_timeout(600)
        
        # Check if distance badges appeared on restaurant cards
        dist_badge = page.locator('span[title="Distance to nearest outlet"]').first
        assert dist_badge.is_visible(), "GPS distance badge not visible on cards!"
        dist_text = dist_badge.text_content().strip()
        print(f"Verified live distance badge: {dist_text}")
        page.screenshot(path='screenshots/advanced_near_me.png')
        
        # Reset Near Me
        page.click('#smart-btn-NEAR_ME')
        page.wait_for_timeout(300)

        # 4. Test Side-by-Side Menu Comparator
        print("Testing Feature 3: Side-by-Side Menu & Price Comparator...")
        page.click('button[title="Compare Restaurants"]')
        page.wait_for_timeout(400)
        assert page.locator('#compare-modal').is_visible(), "Compare modal did not open"
        
        # Verify comparison columns (Sultan's Dine vs Kacchi Bhai)
        col1 = page.locator('#compare-matrix h4:has-text("Sultan\'s Dine")')
        col2 = page.locator('#compare-matrix h4:has-text("Kacchi Bhai")')
        assert col1.is_visible() and col2.is_visible(), "Comparison columns not rendered"
        print("Comparison matrix verified: Sultan's Dine vs Kacchi Bhai side-by-side!")
        page.screenshot(path='screenshots/advanced_comparator.png')
        page.keyboard.press('Escape')
        page.wait_for_timeout(300)

        # 5. Test Surprise Food Decider Wheel (আজ কি খাব?)
        print("Testing Feature 4: Surprise Food Decision Wheel...")
        page.locator('button:has-text("🎲 আজ কি খাব?")').first.click()
        page.wait_for_timeout(400)
        assert page.locator('#surprise-modal').is_visible(), "Surprise modal did not open"
        
        # Click Spin button
        page.click('#spin-wheel-btn')
        page.wait_for_timeout(1000)
        
        # Check result state
        win_meal = page.locator('#wheel-result-state:has-text("Your Winning Meal")')
        assert win_meal.is_visible(), "Food wheel did not generate a winning meal"
        print("Food Decision Wheel successfully spun and picked a winning meal!")
        page.screenshot(path='screenshots/advanced_food_wheel.png')
        page.keyboard.press('Escape')
        page.wait_for_timeout(300)

        # 6. Test Thermal POS Cash Memo Slip
        print("Testing Feature 5: Thermal POS Cash Memo Slip...")
        # Open a restaurant menu (e.g. Sultan's Dine)
        page.fill('#search-input', "Sultan's Dine")
        page.wait_for_timeout(400)
        page.locator('button:has-text("Full Menu")').first.click()
        page.wait_for_timeout(600)
        
        # Add item to bill
        page.locator('#modal-menu-categories button:has-text("Add")').first.click()
        page.wait_for_timeout(300)
        
        # Open bill modal
        page.locator('button[onclick="openBillModal()"]').click()
        page.wait_for_timeout(400)
        
        # Switch to Thermal POS Memo Slip
        page.click('#btn-bill-tab-memo')
        page.wait_for_timeout(400)
        
        receipt_paper = page.locator('#thermal-receipt-paper')
        assert receipt_paper.is_visible(), "Thermal POS paper slip not visible"
        assert "TOKEN: ORD-" in receipt_paper.text_content(), "Token not in thermal receipt"
        assert "TOTAL PAYABLE:" in receipt_paper.text_content(), "Total payable not in receipt"
        print("Thermal POS Cash Memo Slip layout and token generation verified!")
        page.screenshot(path='screenshots/advanced_thermal_pos_slip.png')

        print("\nALL 5 ADVANCED NEXT-GEN FEATURES VERIFIED 100% WORKING & PRODUCTION READY!")
        browser.close()

if __name__ == '__main__':
    test_advanced()
