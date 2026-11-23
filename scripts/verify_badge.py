import sys
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('http://localhost:5000', wait_until='domcontentloaded')
    page.wait_for_timeout(1000)
    badge = page.locator('#results-count-badge').text_content().strip()
    stat = page.locator('#stat-restaurants-count').text_content().strip()
    branches = page.locator('#stat-branches-count').text_content().strip()
    print(f"VERIFIED_BADGE: {badge}")
    print(f"VERIFIED_STAT_RESTAURANTS: {stat}")
    print(f"VERIFIED_STAT_BRANCHES: {branches}")
    page.screenshot(path='screenshots/verified_505_screen.png')
    browser.close()
