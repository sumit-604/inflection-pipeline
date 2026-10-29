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

    # --- Find ALL View Transcript links (not just the first) ---
    links = page.locator('a:has-text("View Transcript")').all()
    print(f"\nFound {len(links)} transcripts on the page")

    # --- Loop through and download the first 3 ---
    for i in range(min(3, len(links))):
        url = links[i].get_attribute("href")
        if url.startswith("/"):
            url = "https://www.screener.in" + url

        print(f"\nDownloading #{i+1}...")
        print(f"  URL: {url}")

        response = page.context.request.get(url)

        if response.ok:
            filename = f"transcript_{i+1}.pdf"
            with open(filename, "wb") as f:
                f.write(response.body())
            size_kb = len(response.body()) / 1024
            print(f"  ✅ Saved as {filename} ({size_kb:.0f} KB)")
        else:
            print(f"  ❌ Failed: HTTP {response.status}")

    print("\nAll done!")
    input("Press Enter to close browser...")
    browser.close()