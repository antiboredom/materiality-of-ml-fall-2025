# Basic Web Scraping

## Dependencies

First, install [playwright](https://playwright.dev/python/docs/library)

```
uv add playwright
uv run playwright install
```

## Scraping text

```python

# import playwright
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # open a chrome browser
    # set headless to be true to hide the browser or false to show
    browser = p.chromium.launch(headless=false)

    # open a new page
    page = browser.new_page()

    # go to reddit top
    page.goto("https://old.reddit.com/top/")

    titles = page.query_selector_all("a.title")
    for t in titles:
        print(t.text_content())

    # close the browser
    browser.close()

```

## Scraping text with pagination

```python

# import playwright
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # open a chrome browser
    # set headless to be true to hide the browser or false to show
    browser = p.chromium.launch(headless=false)

    # open a new page
    page = browser.new_page()

    # go to reddit top
    page.goto("https://old.reddit.com/top/")

    # print the first 10 pages of post titles
    page_number = 0
    while page_number < 10:
        titles = page.query_selector_all("a.title")
        for t in titles:
            print(t.text_content())
        page.locator(".next-button").click()
        page_number += 1

        # pause for 1 second
        page.wait_for_timeout(1000)

    browser.close()

```

## Scraping images

Similar to text!

First, install requests:

```
uv add requests
```

Here's a generic function to download images (or other files):

```python
def download_file(url, local_filename=None):
    if local_filename is None:
        local_filename = url.split("/")[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

```

Combine this with code similar to our previous example:

```python

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(
        "https://www.alibaba.com/trade/search?spm=a2700.galleryofferlist.the-new-header_fy23_pc_search_bar.keydown__Enter&tab=all&SearchText=coal&has4Tab=true&from=pcHomeContent"
    )
    page_number = 0
    while page_number < 5:
        images = page.query_selector_all(".searchx-product-e-slider__link img")
        for i in images:
            # get the src attribute
            src = i.get_attribute("src")
            print(src)
            download_file(src)
        page.locator(".searchx-pagination a").last.click()
        page_number += 1
    browser.close()

```
