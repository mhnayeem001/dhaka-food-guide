import asyncio
from playwright.async_api import async_playwright

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 390, 'height': 844}, device_scale_factor=2)
        page = await context.new_page()
        
        await page.goto('http://localhost:5000', wait_until='domcontentloaded')
        await page.wait_for_timeout(2000)
        
        # Search Sao Paulo
        await page.evaluate("""
            currentSearchQuery = 'Sao Paulo';
            renderRestaurants();
        """)
        await page.wait_for_timeout(1000)
        await page.evaluate("window.scrollTo(0, 450)")
        await page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/3eaf995e-e531-4703-8238-57e87cdc7f79/sao_paulo_card.png')
        print('Captured sao_paulo_card.png')

        # Open Cafe Sao Paulo modal
        await page.evaluate("openRestaurantModal('cafe-sao-paulo', 'menu')")
        await page.wait_for_timeout(1500)
        await page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/3eaf995e-e531-4703-8238-57e87cdc7f79/sao_paulo_modal.png')
        print('Captured sao_paulo_modal.png')
        
        await browser.close()

if __name__ == '__main__':
    asyncio.run(verify())
