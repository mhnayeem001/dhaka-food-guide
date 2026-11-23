import asyncio
from playwright.async_api import async_playwright

async def debug():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        device = p.devices['iPhone 14 Pro']
        page = await browser.new_page(**device)
        page.on("console", lambda msg: print(f"BROWSER CONSOLE: {msg.text}"))
        page.on("pageerror", lambda err: print(f"PAGE ERROR: {err}"))
        await page.goto("file:///E:/menu restaurant/index.html")
        await page.wait_for_selector("#restaurants-grid button")
        
        # Call openRestaurantModal directly via evaluate
        print("Calling openRestaurantModal('kfc-bangladesh', 'menu')...")
        await page.evaluate("openRestaurantModal('kfc-bangladesh', 'menu')")
        await page.wait_for_timeout(500)

        modal = page.locator("#restaurant-modal")
        print("Modal classList after open:", await modal.get_attribute("class"))
        print("Modal is_visible:", await modal.is_visible())

        await browser.close()

asyncio.run(debug())
