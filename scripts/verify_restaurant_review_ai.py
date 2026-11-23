import asyncio
from playwright.async_api import async_playwright

async def verify_chillox_and_reviews():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()

        page.on("console", lambda msg: print(f"[CONSOLE] {msg.type}: {msg.text}"))
        page.on("pageerror", lambda err: print(f"[PAGEERROR] {err}"))

        print("Navigating to http://localhost:5000...")
        await page.goto("http://localhost:5000", wait_until="networkidle")

        # Open AI Assistant
        print("Opening modal...")
        await page.locator('#floating-ai-btn').click()
        await page.wait_for_selector('#ai-assistant-modal:not(.hidden)')
        await page.wait_for_timeout(500)

        # TEST 1: The user's exact query: 'chillox er burger kemon?'
        test_query = "chillox er burger kemon?"
        print(f"\n--- Testing Query 1: '{test_query}' ---")
        input_el = page.locator('#ai-chat-input')
        await input_el.fill(test_query)
        await page.keyboard.press("Enter")

        # Wait for AI response
        await page.wait_for_timeout(2000)

        # Get response text
        messages_text = await page.locator('#ai-chat-messages').inner_text()
        print(f"Response preview:\n{messages_text}\n")

        # Strict Assertions:
        assert "Woodhouse Grill" not in messages_text, "ERROR: Woodhouse Grill appeared in Chillox query!"
        assert "Farmhouse Burger" not in messages_text, "ERROR: Farmhouse Burger appeared in Chillox query!"
        assert "Chillox" in messages_text, "ERROR: Chillox not mentioned in response!"
        assert "4.6" in messages_text, "ERROR: Chillox rating not mentioned!"
        
        print(">>> SUCCESS: Query 1 passed! Chillox-specific review returned.")

        # Take screenshot for user
        await page.screenshot(path="C:/Users/user/.gemini/antigravity/brain/3eaf995e-e531-4703-8238-57e87cdc7f79/ai_chillox_review_fixed.png")
        print("Saved screenshot to brain/ai_chillox_review_fixed.png")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify_chillox_and_reviews())
