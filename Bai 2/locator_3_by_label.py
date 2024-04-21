import asyncio

from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    # where we define all actions we control and action on browser
    browser = await playwright.chromium.launch(headless=False, slow_mo=1000)
    page = await browser.new_page()
    await page.goto("https://bootswatch.com/default/")

    ## Example get locator of element
    email_textbox = page.get_by_label("Password")
    await email_textbox.highlight()

    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())