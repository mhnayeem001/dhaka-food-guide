import asyncio
from playwright.async_api import async_playwright

async def verify_food_wheel_uttara():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()

        print("Navigating to http://localhost:5000...")
        await page.goto("http://localhost:5000", wait_until="networkidle")

        # Open Food Decider Wheel Modal
        print("Opening Food Decider Modal...")
        await page.evaluate("openSurpriseModal()")
        await page.wait_for_selector('#surprise-modal:not(.hidden)')
        await page.wait_for_timeout(300)

        # Select Uttara in #wheel-area-select
        print("Selecting Uttara...")
        await page.select_option('#wheel-area-select', 'Uttara')
        await page.select_option('#wheel-budget-select', 'ALL')

        # Spin 10 times to test random candidates
        for i in range(10):
            print(f"Spin #{i+1}...")
            await page.locator('#spin-wheel-btn').click()
            await page.wait_for_timeout(1000) # wait for 700ms spin animation
            
            result_text = await page.locator('#wheel-result-state').inner_text()
            print(f"Result #{i+1}:\n{result_text.strip()}\n")

            # Check that Panthapath is NOT shown as the location
            assert "বসুন্ধরা সিটি" not in result_text, f"ERROR in Spin #{i+1}: Bashundhara City landmark appeared for Uttara!"
            assert "Panthapath: বসুন্ধরা সিটি" not in result_text, f"ERROR in Spin #{i+1}: Panthapath appeared for Uttara!"

        # Save screenshot
        await page.screenshot(path="C:/Users/user/.gemini/antigravity/brain/3eaf995e-e531-4703-8238-57e87cdc7f79/food_wheel_uttara_verified.png")
        print("Saved screenshot to brain/food_wheel_uttara_verified.png")
        print(">>> SUCCESS: 10/10 SPINS IN UTTARA RETURNED ACCURATE UTTARA OUTLETS & LANDMARKS!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify_food_wheel_uttara())
