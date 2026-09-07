from pages.home_page import HomePage
from pages.iphone_page import IPhonePage
from pages.mac_page import MacPage
from pages.search_page import SearchPage
from pages.store_page import StorePage


def test_recorded_flow(page):
    home_page = HomePage(page)

    # Step 1: Navigate to Google
    page.goto("https://www.google.com/", wait_until="domcontentloaded")

    # Step 2: Navigate to Apple India homepage
    page.goto("https://www.apple.com/in/?cid-oas-in-domains-apple.in/", wait_until="domcontentloaded")
    page.bring_to_front()

    # Step 3: Click "Mac"
    page.locator('a[aria-label="Mac"]').nth(1).click(force=True)

    # Step 4: Click "MacBook Air"
    page.locator("a[href*='macbook-air']:visible").filter(has_text="MacBook Air").nth(1).click(force=True)

    # Step 5: Click "Buy, MacBook Air"
    page.locator('a[aria-label="Buy, MacBook Air"]').first.click(force=True)

    # Step 6: Click "Entertainment"
    page.get_by_role("link", name="Entertainment", exact=True).first.click(force=True)

    # Step 7: Click "Apple Music"
    page.locator("a[href*='apple-music']:visible").filter(has_text="Apple Music").nth(3).click(force=True)

    # Keep scroll step from original script
    page.evaluate("window.scrollTo(0, 1080)")

    # Step 8: Click "Try it free*"
    page.get_by_role("link", name="Try it free*", exact=False).first.click(force=True)

    # Step 9: Navigate to Apple Music home
    page.goto("https://music.apple.com/in/home", wait_until="domcontentloaded")