"""
Production Features Verification Suite:
- Deep linking: http://localhost:5000/?r=kfc-bangladesh
- Bookmarking / Favorites (LocalStorage)
- In-menu Bill & VAT Estimator
- PWA manifest and SEO metadata
"""
import sys
from playwright.sync_api import sync_playwright

def run_production_tests():
    print("=" * 50)
    print("DHAKA MENU HUB - PRODUCTION VERIFICATION SUITE")
    print("=" * 50)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 393, 'height': 852})
        page = context.new_page()

        # 1. Test Base Load & PWA tags
        print("\n1. Verifying PWA Manifest & SEO Tags...")
        page.goto("http://localhost:5000", wait_until="networkidle")
        
        manifest_href = page.locator('link[rel="manifest"]').get_attribute('href')
        print(f"   ✓ Manifest link detected: {manifest_href}")
        assert manifest_href == "./manifest.json"

        og_title = page.locator('meta[property="og:title"]').get_attribute('content')
        print(f"   ✓ OpenGraph title: '{og_title}'")
        assert "505+" in og_title

        # 2. Test Deep Linking: ?r=sultans-dine
        print("\n2. Testing Deep Linking (?r=sultans-dine)...")
        page.goto("http://localhost:5000/?r=sultans-dine", wait_until="networkidle")
        page.wait_for_selector("#restaurant-modal:not(.hidden)", timeout=5000)
        modal_title = page.locator("#modal-title").inner_text()
        print(f"   ✓ Deep-linked modal opened automatically: '{modal_title}'")
        assert "Sultan's Dine" in modal_title

        # 3. Test Bill Estimator inside Modal
        print("\n3. Testing In-Menu Bill & VAT Estimator...")
        add_btn = page.locator("#modal-menu-categories button:has-text('Add')").first
        add_btn.click()
        page.wait_for_selector("#modal-bill-bar:not(.hidden)", timeout=3000)
        
        bill_count = page.locator("#bill-item-count").inner_text()
        bill_total = page.locator("#bill-total-price").inner_text()
        bill_vat = page.locator("#bill-vat-amount").inner_text()
        print(f"   ✓ Bill Estimator Active: {bill_count} item(s) -> Total: {bill_total} (VAT: {bill_vat})")
        assert int(bill_count) >= 1

        # Close modal
        page.locator("#modal-top-close-btn").click()
        page.wait_for_selector("#restaurant-modal", state="hidden", timeout=3000)
        print("   ✓ Modal closed cleanly")

        # 4. Test Favorites / Bookmarking
        print("\n4. Testing Bookmark / Favorite System...")
        fav_btn = page.locator("button[aria-label*='Favorite']").first
        fav_btn.click()
        
        page.wait_for_timeout(300)
        saved_pill = page.locator("button:has-text('Saved')")
        saved_text = saved_pill.inner_text()
        print(f"   ✓ Saved pill updated: '{saved_text}'")
        assert "Saved" in saved_text and "1" in saved_text

        # Click saved pill to filter
        saved_pill.click()
        page.wait_for_timeout(300)
        badge_text = page.locator("#results-count-badge").inner_text()
        print(f"   ✓ Filtered by Saved spots: '{badge_text}'")
        assert "1 Available" in badge_text

        # Screenshot proof
        page.screenshot(path="screenshots/production_verified.png")
        print("\n   ✓ Saved verification screenshot: screenshots/production_verified.png")

        browser.close()

    print("\n" + "=" * 50)
    print("ALL PRODUCTION FEATURE TESTS PASSED 100%! 🚀✨")
    print("=" * 50)

if __name__ == "__main__":
    run_production_tests()
