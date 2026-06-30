from playwright.sync_api import Page
from pages.Saucedemo.base_page import BasePage
from pages.Saucedemo.checkout_page import CheckoutPage
from pages.Saucedemo.inventory_page import InventoryPage

class CardPage(BasePage):

    CART_ITEMS = '.cart_item'
    CHECKOUT_BUTTON = '#checkout'
    CONTINUE_SHOPPING_BUTTON = '#continue-shopping'
    REMOVE_BUTTON = '[data-test^="remove-"]'
    
    URL = "https://www.saucedemo.com/cart.html"

    def __init__(self, page: Page):
        super().__init__(page)
        self._expected_elements = [
            self.CHECKOUT_BUTTON,
            self.CONTINUE_SHOPPING_BUTTON,
        ]

    def get_item_count(self) -> int:
        return self.page.locator(self.CART_ITEMS).count()
    
    def remove_item(self, item_id: str):
        self.page.click(f'[data-test="remove-{item_id}"]')
        return self
    
    def remove_all_items(self):
        remove_button = self.page.locator(self.REMOVE_BUTTON)
        for i in range(remove_button.count()):
            remove_button.nth(i).click()
        return self
    
    def go_to_checkout(self):
        self.page.locator(self.CHECKOUT_BUTTON).click()
        return CheckoutPage(self.page)
    
    def continue_shopping(self):
        self.page.click(self.CONTINUE_SHOPPING_BUTTON)
        return InventoryPage(self.page)
    
    def is_card_is_empty(self) -> bool:
        return self.get_item_count() == 0
