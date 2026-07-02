from playwright.sync_api import Page
from pages.Saucedemo.base_page import BasePage


class CheckoutCompletePage(BasePage):

    COMPLETE_HEADER = '.complete-header'
    COMPLETE_TEXT = '.complete-text'
    COMPLETE_IMAGE = '.pony_express'
    BACK_HOME_BUTTON = '#back-to-products'

    URL = "https://www.saucedemo.com/checkout-complete.html"

    def __init__(self, page: Page):
        super().__init__(page)
        self._expected_elements = [
            self.COMPLETE_HEADER,
            self.COMPLETE_TEXT,
            self.COMPLETE_IMAGE,
            self.BACK_HOME_BUTTON
        ]

    def get_complete_header(self) -> str:
        return self.page.locator(self.COMPLETE_HEADER).text_content()
    
    def get_complete_text(self) -> str:
        return self.page.locator(self.COMPLETE_TEXT).text_content()
    
    def click_back(self) -> 'InventoryPage':
        self.page.click(self.BACK_HOME_BUTTON)
        from pages.Saucedemo.inventory_page import InventoryPage
        return InventoryPage(self.page)
    
    def complite_page_is_loaded(self):
        return (self.is_element_visible(self.COMPLETE_HEADER) and
                self.is_element_visible(self.COMPLETE_TEXT) and
                self.is_element_visible(self.COMPLETE_IMAGE) and
                self.is_element_visible(self.BACK_HOME_BUTTON))