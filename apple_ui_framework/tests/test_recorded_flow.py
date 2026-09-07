from pages.home_page import HomePage
from pages.iphone_page import IPhonePage
from pages.mac_page import MacPage
from pages.search_page import SearchPage
from pages.store_page import StorePage


def test_recorded_flow(page):
    # Initialize page objects (even if not used directly, for consistency with repo pattern)
    home_page = HomePage(page)
    iphone_page = IPhonePage(page)
    mac_page = MacPage(page)
    search_page = SearchPage(page)
    store_page = StorePage(page)

    # Preserve original navigation and interactions exactly, via page objects
    home_page.open_external_url("https://www.google.com/")
    home_page.open_external_url("https://www.apple.com/in/?cid-oas-in-domains-apple.in/")
    home_page.bring_to_front()
    home_page.open_watch_page()
    home_page.open_accessories_page_from_watch()
    home_page.open_entertainment_category()
    home_page.open_apple_music_page()
