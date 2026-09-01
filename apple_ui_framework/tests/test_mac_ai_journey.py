from pages.home_page import HomePage
from pages.mac_page import MacPage
from test_script_helpers import _run_genai_validation


def test_recorded_flow(page):
    home_page = HomePage(page)

    home_page.open_external_url("https://www.google.com/")
    home_page.open_external_url("chrome-error://chromewebdata/")
    home_page.open_external_url("https://www.apple.com/in/?cid-oas-in-domains-apple.in/")
    _run_genai_validation(page, 'is site loaded?')
    home_page.bring_to_front()

    home_page.open_mac_page()
    _run_genai_validation(page, 'has mac site been loaded?')

    mac_page = MacPage(page)

    mac_page.scroll_vertical(2400)
    mac_page.open_learn_more_mac_ai()
    mac_page.close_built_for_ai_section()
    mac_page.scroll_vertical(960)
    mac_page.open_learn_more_macbook_air()
    _run_genai_validation(page, 'is mac book air site loaded?')
