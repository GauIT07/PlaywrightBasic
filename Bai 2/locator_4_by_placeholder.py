import asyncio

from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    # where we define all actions we control and action on browser
    browser = await playwright.chromium.launch(headless=False, slow_mo=1000)
    page = await browser.new_page()

    #await page.goto("https://www.saucedemo.com/")

    ## Example get locator of element
    # username_textbox = page.get_by_placeholder("Username")
    # await username_textbox.highlight()
    # await username_textbox.fill("testing4everyone")

    # password_textbox = page.get_by_placeholder("Password")
    # await password_textbox.highlight()
    # await password_textbox.fill("Password ahihi")

    # await browser.close()


    ## Example get locator of element - but issues
    await page.goto("https://bootswatch.com/default")
    username_textbox = page.get_by_placeholder("Password")
    await username_textbox.highlight()
    await username_textbox.fill("testing")

    await browser.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())