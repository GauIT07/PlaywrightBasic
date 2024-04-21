
import asyncio

from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    # where we define all actions we control and action on browser
    browser = await playwright.chromium.launch(headless=False, slow_mo=1000)
    page = await browser.new_page()

    await page.goto("https://bootswatch.com/default/")

    ## Example get locator of element
    search_box_example_1 = page.locator("xpath=//*[@id='navbarColor01']/form/input")
    await search_box_example_1.highlight()

    search_box_example_2 = page.locator("css=div[id='navbarColor02']>form>input[placeholder='Search']")
    await search_box_example_2.highlight()
    await page.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())