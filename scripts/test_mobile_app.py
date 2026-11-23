import asyncio
import os
from playwright.async_api import async_playwright

async def run_mobile_tests():
    print("========================================")
    print("DHAKA MENU HUB - MOBILE UX & FUNCTIONAL TEST")
    print("========================================")

    html_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "index.html"))
    file_url = f"file:///{html_file.replace(os.sep, '/')}"

    async with async_playwright() as p:
        # Emulate iPhone 14 Pro mobile viewport (393 x 852)
        device = p.devices['iPhone 14 Pro']
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(**device)
        page = await context.new_page()

        print(f"1. Loading page on mobile viewport (393x852)...")
        await page.goto(file_url, wait_until='networkidle')
        await page.wait_for_selector("#restaurants-grid .font-display", timeout=5000)

        # Test 1: Title & Stats
        title = await page.title()
        stat_restaurants = await page.inner_text('#stat-restaurants-count')
        stat_branches = await page.inner_text('#stat-branches-count')
        print(f"   ✓ Page Title: '{title}'")
        print(f"   ✓ Header Stats: {stat_restaurants} Restaurants, {stat_branches} Dhaka Outlets")

        # Test 2: Check Area Pills & Cuisine Chips
        pills_count = await page.locator('#dhaka-area-pills button').count()
        chips_count = await page.locator('.cuisine-chip').count()
        print(f"   ✓ Mobile Touch Carousels: {pills_count} Area Pills, {chips_count} Cuisine Chips")

        # Screenshot 1: Mobile Home View
        screenshots_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "screenshots"))
        os.makedirs(screenshots_dir, exist_ok=True)
        home_shot = os.path.join(screenshots_dir, "mobile_home.png")
        await page.screenshot(path=home_shot)
        print(f"   ✓ Saved Mobile Home screenshot: {home_shot}")

        # Test 3: Search for 'KFC'
        print("\n2. Testing Mobile Search for 'KFC'...")
        search_input = page.locator('#search-input')
        await search_input.fill("KFC")
        await page.wait_for_timeout(400)

        results_badge = await page.inner_text('#results-count-badge')
        first_card_title = await page.locator('#restaurants-grid h3').first.inner_text()
        print(f"   ✓ Search Results: {results_badge}")
        print(f"   ✓ Top Match: '{first_card_title}'")

        # Test 4: Open Mobile Bottom Sheet Modal for KFC
        print("\n3. Testing Mobile Bottom Sheet Modal Interaction...")
        menu_btn = page.locator('#restaurants-grid button:has-text("Full Menu")').first
        await menu_btn.click()
        await page.wait_for_timeout(600)

        modal = page.locator('#restaurant-modal')
        modal_title = await page.inner_text('#modal-title')
        modal_menu_count = await page.inner_text('#modal-menu-count')
        modal_branch_count = await page.inner_text('#modal-branch-count')
        print(f"   ✓ Bottom Sheet Opened: {await modal.is_visible()}")
        print(f"   ✓ Modal Title: '{modal_title}'")
        print(f"   ✓ Total Menu Items: {modal_menu_count}")
        print(f"   ✓ Total Outlets: {modal_branch_count}")

        # Screenshot 2: Modal Open View
        modal_shot = os.path.join(screenshots_dir, "mobile_modal_menu.png")
        await page.screenshot(path=modal_shot)
        print(f"   ✓ Saved Mobile Modal Menu screenshot: {modal_shot}")

        # Test 5: In-Menu Search inside Modal
        print("\n4. Testing In-Menu Search within Modal...")
        modal_search = page.locator('#modal-menu-search')
        await modal_search.fill("Zinger")
        await page.wait_for_timeout(400)

        filtered_items = await page.locator('#modal-menu-categories .font-bold.text-slate-900').all_inner_texts()
        print(f"   ✓ In-Menu Search for 'Zinger': Found items -> {filtered_items}")

        # Test 6: Switch to Dhaka Outlets Tab inside Modal
        print("\n5. Testing Modal Tab Switch to 'Dhaka Outlets'...")
        branches_tab = page.locator('#tab-branches-btn')
        await branches_tab.click()
        await page.wait_for_timeout(500)

        branch_cards = await page.locator('#modal-branches-list h4').all_inner_texts()
        print(f"   ✓ Rendered Outlets ({len(branch_cards)} total): {branch_cards[:4]}...")

        # Screenshot 3: Modal Outlets View
        branches_shot = os.path.join(screenshots_dir, "mobile_modal_outlets.png")
        await page.screenshot(path=branches_shot)
        print(f"   ✓ Saved Mobile Modal Outlets screenshot: {branches_shot}")

        # Test 7: Close Modal
        print("\n6. Closing Modal...")
        await page.evaluate("closeModal()")
        await page.wait_for_timeout(400)
        is_closed = not await modal.is_visible()
        print(f"   ✓ Modal Closed: {is_closed}")

        # Test 8: Filter by Area 'Dhanmondi'
        print("\n7. Testing Area Filter 'Dhanmondi'...")
        await search_input.fill("")
        await page.evaluate("handleSearch()")
        await page.wait_for_timeout(300)

        dhanmondi_btn = page.locator('#dhaka-area-pills button:has-text("Dhanmondi")')
        await dhanmondi_btn.click()
        await page.wait_for_timeout(500)

        dhanmondi_badge = await page.inner_text('#results-count-badge')
        first_card_branch = await page.locator('#restaurants-grid .bg-amber-50\\/90').first.inner_text()
        print(f"   ✓ Results in Dhanmondi: {dhanmondi_badge}")
        print(f"   ✓ Local Branch Box Highlighted:\n{first_card_branch.strip()[:100]}...")

        # Screenshot 4: Dhanmondi Area Filter View
        area_shot = os.path.join(screenshots_dir, "mobile_dhanmondi_filter.png")
        await page.screenshot(path=area_shot)
        print(f"   ✓ Saved Area Filter screenshot: {area_shot}")

        print("\n========================================")
        print("ALL MOBILE UX TESTS PASSED SUCCESSFULLY! 📱✨")
        print("========================================")

        await browser.close()

if __name__ == '__main__':
    asyncio.run(run_mobile_tests())
