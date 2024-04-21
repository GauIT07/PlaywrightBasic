
import asyncio
from playwright.async_api import async_playwright, expect, Playwright

async def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False, slow_mo=300)
    page = await browser.new_page()
    await page.goto('https://bootstrap-datepicker.readthedocs.io/en/latest/')

    # Define selectors for day, month, and year
    day_selector = 'td.day'
    month_selector = 'span.month'
    year_selector = 'span.year'

    # Click on the input field to open the datepicker
    await page.click('input#sandbox-container input')

    # Select a day
    await page.click(day_selector)

    # Select a month
    await page.click(month_selector)

    # Select a year
    await page.click(year_selector)

    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())