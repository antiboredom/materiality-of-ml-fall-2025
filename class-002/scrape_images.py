from playwright.sync_api import sync_playwright
import requests


def download_file(url, local_filename=None):
    if local_filename is None:
        local_filename = url.split("/")[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename


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
            src = i.get_attribute("src")
            print(src)
            download_file(src)
        page.locator(".searchx-pagination a").last.click()
        page_number += 1
    browser.close()
