from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    print("Opening Screener...")
    page.goto("https://www.screener.in")
    
    print("Page title:", page.title())
    
    input("Press Enter to close the browser...")
    browser.close()
    print("Done!")