import re

from playwright.sync_api import expect

from pages.base_page import BasePage


class MacPage(BasePage):
    def main_content(self):
        return self.page.get_by_role("main")

    def mac_heading(self):
        return self.main_content().get_by_text("Mac").first

    def buy_link(self):
        return self.page.locator("a").filter(has_text="Buy").first

    def compare_link(self):
        return self.page.locator("a").filter(has_text="Compare").first

    def mac_product_links(self):
        return self.main_content().locator("a").filter(has_text="MacBook")

    def verify_mac_page_loaded(self):
        self.verify_url_contains("mac")
        expect(self.mac_heading()).to_be_visible()

    def verify_buy_button_visible(self):
        expect(self.buy_link()).to_be_visible()

    def scroll_to_compare(self):
        self.compare_link().scroll_into_view_if_needed()

    def get_mac_product_count(self) -> int:
        return self.mac_product_links().count()

    def open_mac_page(self):
        self.verify_mac_page_loaded()

    def open_macbook_air_product_page(self):
        self.main_content().get_by_text('MacBook Air', exact=False).first.click(force=True)
        self.page.wait_for_load_state('domcontentloaded')

    def open_macbook_air_closer_look(self):
        self.page.get_by_role('button', name='Take a closer look - MacBook Air').first.click(force=True)
        self.page.wait_for_load_state('domcontentloaded')

    def open_macbook_air_buy_page(self):
        self.page.get_by_role('link', name='Buy - MacBook Air 13″', exact=False).first.click(force=True)
        self.page.wait_for_load_state('domcontentloaded')

    def select_macbook_air_13_inch_configuration(self):
        self.page.locator('label#_r_d__label').first.click(force=True)
        self.page.locator('input[name="chassis-dimensionScreensize"]').first.check()

    def open_entertainment_section(self):
        self.page.get_by_role('link', name='Entertainment', exact=True).first.click(force=True)
        self.page.wait_for_load_state('domcontentloaded')

    def open_stream_now_the_dink_comedy(self):
        self.page.locator("a[href*='umc.cmc']:visible").filter(has_text="Stream now The Dink Comedy").first.click(force=True)
        self.page.wait_for_load_state('domcontentloaded')
