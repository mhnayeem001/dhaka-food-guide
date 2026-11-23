import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        device = p.devices['iPhone 14 Pro']
        context = await browser.new_context(**device)
        page = await context.new_page()
        await page.goto("file:///E:/menu restaurant/index.html")
        await page.wait_for_selector("#restaurants-grid button")
        
        # Click menu button
        first_btn = page.locator("#restaurants-grid button:has-text('Full Menu')").first
        await first_btn.click()
        await page.wait_for_timeout(600)
        
        modal = page.locator("#restaurant-modal")
        print("Modal visible after open:", await modal.is_visible())

        # Click top close button
        close_btn = page.locator("#modal-top-close-btn")
        await close_btn.click()
        await page.wait_for_timeout(500)
        print("Modal visible after top close button click:", await modal.is_visible())
        print("Classes on modal:", await modal.get_attribute("class"))

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
