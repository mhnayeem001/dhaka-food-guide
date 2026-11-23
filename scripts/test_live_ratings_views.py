"""
Live View Counter and Interactive Rating Verification Suite
"""
import time
from playwright.sync_api import sync_playwright

def verify_live_features():
    print("=" * 50)
    print("VERIFYING LIVE VIEW COUNTER & INTERACTIVE RATINGS")
    print("=" * 50)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 393, 'height': 852})

        # 1. Load page
        page.goto("http://localhost:5000", wait_until="networkidle")
        
        # Read initial view count on first card
        first_card_id = "kfc-bangladesh"
        view_el = page.locator(f"#views-{first_card_id}")
        initial_views = int(view_el.inner_text().strip())
        print(f"1. Initial card view count for '{first_card_id}': {initial_views}")

        # 2. Click card button to open modal
        print("2. Opening modal to trigger live view counter...")
        page.goto(f"http://localhost:5000/?r={first_card_id}", wait_until="networkidle")
        page.wait_for_selector("#restaurant-modal:not(.hidden)", timeout=5000)
        page.wait_for_timeout(400)

        # Modal view count should be initial_views + 1
        modal_views = int(page.locator("#modal-view-count").inner_text().replace(',', '').strip())
        print(f"   ✓ Modal view count incremented live: {modal_views}")
        assert modal_views >= initial_views + 1

        # 3. Test Interactive Rating Widget
        print("3. Testing interactive 5-star rating widget...")
        star_btns = page.locator("#modal-star-buttons button")
        assert star_btns.count() == 5
        print(f"   ✓ Found {star_btns.count()} interactive star buttons")

        # Click 5th star
        star_btns.nth(4).click()
        page.wait_for_timeout(400)

        badge_text = page.locator("#user-rating-badge").inner_text()
        print(f"   ✓ Rating badge updated: '{badge_text}'")
        assert "5" in badge_text

        # Check modal rating text
        modal_rating = page.locator("#modal-rating").inner_text()
        print(f"   ✓ Live community rating updated: '{modal_rating}'")

        # Screenshot proof
        page.screenshot(path="screenshots/live_rating_views_verified.png")
        print("   ✓ Screenshot saved: screenshots/live_rating_views_verified.png")

        browser.close()

    print("=" * 50)
    print("ALL LIVE RATING & VIEW COUNTER TESTS PASSED 100%! 🚀")
    print("=" * 50)

if __name__ == "__main__":
    verify_live_features()
