from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # launch a browser
    browser = playwright.chromium.launch(headless=False,slow_mo=1000)
    # creat a new tab
    page = browser.new_page()
    # navigate to "http://playwright.dev"
    page.goto("https://playwright.dev")
    doc_link = page.get_by_role("link", name="Docs")
    doc_link.click()
    print("Docs: ", page.url)
    page.close()