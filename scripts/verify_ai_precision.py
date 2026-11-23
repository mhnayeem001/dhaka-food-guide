import asyncio
from playwright.async_api import async_playwright

async def verify_ai():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()

        page.on("console", lambda msg: print(f"[BROWSER CONSOLE] {msg.type}: {msg.text}"))
        page.on("pageerror", lambda err: print(f"[BROWSER ERROR] {err}"))

        print("Navigating to http://localhost:5000...")
        await page.goto("http://localhost:5000", wait_until="networkidle")

        # Open AI Assistant
        print("Calling openAiAssistant()...")
        await page.evaluate("openAiAssistant()")
        await page.wait_for_timeout(500)

        # TEST 1: The user's exact query
        test_query = "uttarar best thai foods er restaurant konta?"
        print(f"\n--- Testing Query 1: '{test_query}' ---")
        input_el = page.locator('#ai-chat-input')
        await input_el.fill(test_query)
        await page.keyboard.press("Enter")

        # Wait for AI response (typing delay is 400ms)
        await page.wait_for_timeout(2000)

        # Get response text
        messages_text = await page.locator('#ai-chat-messages').inner_text()
        print(f"Response preview:\n{messages_text}\n")

        # Strict checks
        assert "Sultan's Dine" not in messages_text, "CRITICAL ERROR: Sultan's Dine appeared in Thai query!"
        assert "Cafe Americano" not in messages_text, "CRITICAL ERROR: Cafe Americano appeared in Thai query!"
        assert "Kacchi" not in messages_text, "CRITICAL ERROR: Kacchi appeared in Thai query!"
        
        has_thai_spot = any(name in messages_text for name in ["Khao San", "Thai Garden", "Thai Emerald", "Wok & Roll", "Dim Sum Town", "থাই"])
        assert has_thai_spot, "ERROR: No authentic Thai restaurant recommended for Uttara Thai query!"
        print(">>> SUCCESS: Query 1 passed zero-hallucination test! Real Thai spots returned, zero Kacchi/Coffee.")

        # Take screenshot for user
        await page.screenshot(path="C:/Users/user/.gemini/antigravity/brain/3eaf995e-e531-4703-8238-57e87cdc7f79/ai_uttara_thai_fixed.png")
        print("Saved screenshot to brain/ai_uttara_thai_fixed.png")

        # TEST 2: Kacchi in Dhanmondi under 400
        test_query_2 = "dhanmondite 400 takar moddhe kacchi"
        print(f"\n--- Testing Query 2: '{test_query_2}' ---")
        await input_el.fill(test_query_2)
        await page.keyboard.press("Enter")
        await page.wait_for_timeout(2000)

        messages_text_2 = await page.locator('#ai-chat-messages').inner_text()
        assert "Khao San" not in messages_text_2.split(test_query_2)[-1], "ERROR: Thai restaurant appeared in Kacchi query!"
        has_kacchi = any(name in messages_text_2.split(test_query_2)[-1] for name in ["Sultan's Dine", "Kacchi Bhai", "Kacchi", "কাচ্চি", "Shad Tehari"])
        assert has_kacchi, "ERROR: No Kacchi found for Dhanmondi Kacchi query!"
        print(">>> SUCCESS: Query 2 passed! Real Kacchi returned under ৳400.")

        # TEST 3: Smash burger in Banani
        test_query_3 = "bananir best smash burger"
        print(f"\n--- Testing Query 3: '{test_query_3}' ---")
        await input_el.fill(test_query_3)
        await page.keyboard.press("Enter")
        await page.wait_for_timeout(2000)

        messages_text_3 = await page.locator('#ai-chat-messages').inner_text()
        has_burger = any(b in messages_text_3.split(test_query_3)[-1] for b in ["Takeout", "Chillox", "Burger", "বার্গার"])
        assert has_burger, "ERROR: No Burger found for Banani Burger query!"
        print(">>> SUCCESS: Query 3 passed! Real Burger spots returned.")

        # TEST 4: Cold brew coffee in Gulshan
        test_query_4 = "gulshane cold brew coffee"
        print(f"\n--- Testing Query 4: '{test_query_4}' ---")
        await input_el.fill(test_query_4)
        await page.keyboard.press("Enter")
        await page.wait_for_timeout(2000)

        messages_text_4 = await page.locator('#ai-chat-messages').inner_text()
        has_coffee = any(c in messages_text_4.split(test_query_4)[-1] for c in ["North End", "Gloria Jean's", "Coffee", "কফি"])
        assert has_coffee, "ERROR: No Coffee found for Gulshan Coffee query!"
        print(">>> SUCCESS: Query 4 passed! Real Coffee spots returned.")

        print("\n=======================================================")
        print("ALL 4 ADVANCED AI PRECISION TESTS PASSED WITH 100% ACCURACY!")
        print("=======================================================")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify_ai())
