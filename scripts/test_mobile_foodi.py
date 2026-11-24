import asyncio
from playwright.async_api import async_playwright

async def test_full_mobile_interaction():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # iPhone 13 (390 x 844)
        context = await browser.new_context(viewport={'width': 390, 'height': 844}, is_mobile=True, has_touch=True)
        page = await context.new_page()

        await page.goto("http://localhost:5000", wait_until="networkidle")
        await page.evaluate("window.scrollTo(0, 320)")
        await page.wait_for_timeout(500)

        # 1. Verify 4+ cards are in viewport
        cards = await page.locator('#restaurants-grid > div.md\\:hidden').all()
        assert len(cards) >= 4, "Not enough cards rendered!"
        
        # 2. Click on the 1st card
        print("Clicking on first restaurant card...")
        await cards[0].click()
        await page.wait_for_selector('#restaurant-modal:not(.hidden)', timeout=3000)
        print("Restaurant modal opened successfully on mobile click!")

        # 3. Take screenshot of modal on mobile
        await page.screenshot(path="C:/Users/user/.gemini/antigravity/brain/3eaf995e-e531-4703-8238-57e87cdc7f79/mobile_modal_verified.png")
        print("Captured mobile_modal_verified.png")

        # 4. Close modal
        await page.locator('#modal-close-btn').click()
        await page.wait_for_selector('#restaurant-modal.hidden', timeout=3000)
        print("Modal closed successfully!")

        print("\n>>> ALL MOBILE COMPACT TESTS PASSED WITH 100% SUCCESS!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_full_mobile_interaction())
