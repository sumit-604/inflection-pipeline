from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL = os.getenv("SCREENER_EMAIL")
PASSWORD = os.getenv("SCREENER_PASSWORD")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    print("Going to login page...")
    page.goto("https://www.screener.in/login/")

    print("Typing credentials...")
    page.fill('input[name="username"]', EMAIL)
    page.fill('input[name="password"]', PASSWORD)

    print("Clicking login...")
    page.click('button[type="submit"]')
    page.wait_for_load_state("domcontentloaded")

    if "login" not in page.url:
        print("✅ Logged in successfully!")
    else:
        print("❌ Login failed")

    input("Press Enter to close...")
    browser.close()