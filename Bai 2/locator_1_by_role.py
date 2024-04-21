import asyncio

from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    # where we define all actions we control and action on browser
    browser = await playwright.chromium.launch(headless=False, slow_mo=1000)
    page = await browser.new_page()
    await page.goto("https://www.saucedemo.com/")
    ## Example get locator of element by role
    user_name = page.get_by_role("textbox", name="username")
    await user_name.highlight()
    await user_name.fill("standard_user")

    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())