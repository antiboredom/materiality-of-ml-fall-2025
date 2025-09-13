from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://old.reddit.com/top/")
    page_number = 0
    while page_number < 10:
        titles = page.query_selector_all("a.title")
        for t in titles:
            print(t.text_content())
        page.locator(".next-button").click()
        page_number += 1
        page.wait_for_timeout(1000)
    browser.close()
