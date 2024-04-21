
import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False, slow_mo=1000)
    page = await browser.new_page()
    await page.goto("https://demoqa.com/text-box")
    # Example Click
    fullname_texbox = page.locator("//*[@id='userName']")
    await fullname_texbox.fill("Testing4Everyone")
    # await page.locator("//*[@id='userName']").fill("Test fill username")
    # await fullname_texbox.clear() = await fullname_textbox.fill("")

    email_textbox = page.locator("//input[@id='userEmail']")
    await email_textbox.fill("testing4everyone@gmail.com")

    address_textarea = page.locator("//textarea[@id='currentAddress']")
    await address_textarea.fill("123 ABC, Block Z, Amazon Building, A City")

    btn_submit = page.locator("//button[@id='submit']")
    await btn_submit.highlight()
    await btn_submit.click()


    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())