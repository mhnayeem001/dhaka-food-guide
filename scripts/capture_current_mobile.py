import asyncio
from playwright.async_api import async_playwright

async def capture_current_mobile():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # iPhone 13 viewport (390 x 844)
        context = await browser.new_context(viewport={'width': 390, 'height': 844}, is_mobile=True, has_touch=True)
        page = await context.new_page()

        await page.goto("http://localhost:5000", wait_until="networkidle")
        # scroll down slightly so restaurants are in view
        await page.evaluate("window.scrollTo(0, 350)")
        await page.wait_for_timeout(500)

        await page.screenshot(path="C:/Users/user/.gemini/antigravity/brain/3eaf995e-e531-4703-8238-57e87cdc7f79/mobile_current_before.png")
        print("Captured mobile_current_before.png")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture_current_mobile())
