import asyncio
from playwright.async_api import async_playwright

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 390, 'height': 844}, device_scale_factor=2)
        page = await context.new_page()
        
        print("Navigating to http://localhost:5000...")
        await page.goto('http://localhost:5000', wait_until='domcontentloaded')
        await page.wait_for_timeout(2000)
        
        # Scroll down to restaurant list
        await page.evaluate("window.scrollTo(0, 600)")
        await page.wait_for_timeout(1000)
        
        # Screenshot list view
        await page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/3eaf995e-e531-4703-8238-57e87cdc7f79/mobile_list_cards.png')
        print('Captured mobile_list_cards.png')

        # Open Canton Chinese Restaurant modal directly via JS
        await page.evaluate("openRestaurantModal('canton-chinese', 'menu')")
        await page.wait_for_timeout(2000)
        
        # Screenshot modal with soup
        await page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/3eaf995e-e531-4703-8238-57e87cdc7f79/canton_soup_modal.png')
        print('Captured canton_soup_modal.png')

        # Verify image src of Corn Chicken Soup
        soup_img = await page.eval_on_selector(
            'img[alt*="Corn Chicken Soup"]', 
            'el => el ? el.src : null'
        )
        print('Corn Chicken Soup image src:', soup_img)
        
        await browser.close()

if __name__ == '__main__':
    asyncio.run(verify())
