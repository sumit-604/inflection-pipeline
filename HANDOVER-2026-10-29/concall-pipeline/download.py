from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL = os.getenv("SCREENER_EMAIL")
PASSWORD = os.getenv("SCREENER_PASSWORD")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # --- Login ---
    print("Logging in...")
    page.goto("https://www.screener.in/login/")
    page.fill('input[name="username"]', EMAIL)
    page.fill('input[name="password"]', PASSWORD)
    page.click('button[type="submit"]')
    page.wait_for_load_state("domcontentloaded")
    print("✅ Logged in")

    # --- Go to concalls page ---
    print("\nGoing to concalls page...")
    page.goto("https://www.screener.in/concalls/")
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(3000)

    # --- Find the first View Transcript link ---
    print("Looking for first transcript link...")
    transcript_link = page.locator('a:has-text("View Transcript")').first
    transcript_url = transcript_link.get_attribute("href")

    if transcript_url.startswith("/"):
        transcript_url = "https://www.screener.in" + transcript_url

    print("Found URL:", transcript_url)

    # --- Download the PDF ---
    print("\nDownloading...")
    response = page.context.request.get(transcript_url)

    if response.ok:
        with open("first_transcript.pdf", "wb") as f:
            f.write(response.body())
        size_kb = len(response.body()) / 1024
        print(f"✅ Saved as first_transcript.pdf ({size_kb:.0f} KB)")
    else:
        print(f"❌ Download failed: HTTP {response.status}")

    input("\nPress Enter to close browser...")
    browser.close()