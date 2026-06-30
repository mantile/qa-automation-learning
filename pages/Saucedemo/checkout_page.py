from playwright.sync_api import Page
from pages.Saucedemo.base_page import BasePage
from pages.Saucedemo.checkout_overview_page import CheckoutOverviewPage
from pages.Saucedemo.cart_page import CartPage

class CheckoutPage(BasePage):

    FIRST_NAME_INPUT = '#first-name'
    LAST_NAME_INPUT = '#last-name'
    POSTAL_CODE_INPUT = '#postal-code'
    CONTINUE_BUTTON = '#continue'
    CANCEL_BUTTON = '#cancel'
    ERROR_MESSAGE = '[data-test="error"]'

    DEFAULT_FIRST_NAME = "John"
    DEFAULT_LAST_NAME = "Doe"
    DEFAULT_POSTAL_CODE = "12345"

    URL = "https://www.saucedemo.com/checkout-step-one.html"

    def __init__(self, page: Page):
        super().__init__(page)
        self._expected_elements = [
            self.FIRST_NAME_INPUT,
            self.LAST_NAME_INPUT,
            self.POSTAL_CODE_INPUT,
            self.CONTINUE_BUTTON,
            self.CANCEL_BUTTON
        ]

    def fill_first_name(self, first_name: str) -> 'CheckoutPage':
        self.page.fill(self.FIRST_NAME_INPUT, first_name)
        return self
    
    def fill_last_name(self, last_name: str) -> 'CheckoutPage':
        self.page.fill(self.LAST_NAME_INPUT, last_name)
        return self
    
    def fill_postal_code(self, postal_code: str) -> 'CheckoutPage':
        self.page.fill(self.POSTAL_CODE_INPUT, postal_code)
        return self
    
    def fill_checkout_info(
            self,
            first_name: str | None = None,
            last_name: str | None = None,
            postal_code: str | None = None
    ) -> 'CheckoutPage':
        self.fill_first_name(first_name or self.DEFAULT_FIRST_NAME)
        self.fill_last_name(last_name or self.DEFAULT_LAST_NAME)
        self.fill_postal_code(postal_code or self.DEFAULT_POSTAL_CODE)

    def click_continue(self) -> CheckoutOverviewPage:
        self.page.click(self.CONTINUE_BUTTON)
        return CheckoutOverviewPage(self.page)
    
    def click_cancel(self) -> CartPage:
        self.page.click(self.CANCEL_BUTTON)
        return CartPage(self.page)
    
    def continue_with_deafult_info(self) -> CheckoutOverviewPage:
        self.fill_checkout_info()
        return self.click_continue()
    
    def is_checkout_page_loaded(self) -> bool:
        return (self.is_element_visible(self.FIRST_NAME_INPUT) and
                self.is_element_visible(self.LAST_NAME_INPUT) and
                self.is_element_visible(self.POSTAL_CODE_INPUT) and
                self.is_element_visible(self.CONTINUE_BUTTON))
    
    