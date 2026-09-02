from pages.home_page import HomePage
from pages.mac_page import MacPage
from test_script_helpers import _run_genai_validation


def test_recorded_flow(page, create_allure_artifact_dirs):
    home_page = HomePage(page)
    mac_page = MacPage(page)

    home_page.open_url("https://www.apple.com/in/?cid-oas-in-domains-apple.in/")
    _run_genai_validation(page, 'is the site loaded?')

    home_page.open_mac_page_from_global_nav()

    mac_page.open_macbook_air_product_page()
    mac_page.open_macbook_air_closer_look()
    _run_genai_validation(page, 'is macbook air 13 visible')
    mac_page.open_macbook_air_buy_page()

    mac_page.select_macbook_air_13_inch_configuration()
    mac_page.open_entertainment_section()
    mac_page.open_stream_now_the_dink_comedy()
