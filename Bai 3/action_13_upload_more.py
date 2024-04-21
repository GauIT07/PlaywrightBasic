
import asyncio
from playwright.async_api import async_playwright, expect, Playwright

async def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch.persistent_context(user_dir,headless=False, slow_mo=500, args=['--start-maximized'], no_viewport=True)

    page = await browser.new_page()
    await page.goto("https://demoqa.com/upload-download")

    # Start waiting for the download
    async with page.expect_download() as download_info:
        # Perform the action that initiates download
        await page.locator("//a[@id='dowmloadButton']").click()
        download = await download_info.value

    # Wait for the download process to complete and save the downloaded file somewhere
    await download.save_as("./download_folder" + download.suggested_filename)

    await btnDownload.click()


    print(page)

    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())