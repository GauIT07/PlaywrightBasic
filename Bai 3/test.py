import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
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

asyncio.run(main())