from playwright.sync_api import sync_playwright
import json

items = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://old.reddit.com")

    page_number = 0

    while page_number < 1:
        entries = page.query_selector_all("div.entry")
        for e in entries:
            try:
                title = e.query_selector(".title").text_content()
                comments = e.query_selector("a.comments").text_content()
                # 1000 comments
                comments = comments.replace(" comments", "")
                comments = int(comments)
                items.append({"title": title, "comments": comments})
            except Exception as e:
                continue
        page.locator(".next-button").click()
        page_number = page_number + 1

    with open("top_reddit.json", "w") as outfile:
        json.dump(items, outfile, indent=2)
