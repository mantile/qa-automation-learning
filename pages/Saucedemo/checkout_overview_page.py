from playwright.sync_api import Page
from pages.Saucedemo.base_page import BasePage


class CheckoutOverviewPage(BasePage):

    CART_ITEMS = '.cart_item'
    ITEM_NAME = '.inventory_item_name'
    ITEM_PRICE = '.inventory_item_price'
    ITEM_TOTAL = '.summary_subtotal_label'
    TAX = '.summary_tax_label'
    TOTAL = '.summary_total_label'
    FINISH_BUTTON = '#finish'
    CANCEL_BUTTON = '#cancel'

    URL = "https://www.saucedemo.com/checkout-step-two.html"

    def __init__(self, page: Page):
        super().__init__(page)
        self._expected_elements = [
            self.TAX,
            self.TOTAL,
            self.FINISH_BUTTON,
            self.CANCEL_BUTTON
        ]
    
    def get_items_count(self) -> int:
        return self.page.locator(self.CART_ITEMS).count
    
    def get_items_names(self) -> list:
        return self.page.locator(self.ITEM_NAME).all_text_contents()
    
    def get_items_prices(self) -> list:
        return self.page.locator(self.ITEM_PRICE).all_text_contents()
    
    def get_subtotal(self) -> float:
        text = self.page.locator(self.ITEM_TOTAL).text_content()
        return float(text.replace('Item total: $', ''))
    
    def get_tax(self) -> float:
        text = self.page.locator(self.TAX).text_content()
        return float(text.replace('Tax: $', ''))
    
    def get_total(self) -> float:
        text = self.page.locator(self.TOTAL).text_content()
        return float(text.replace('Total: $', ''))
    
    def click_finish(self) -> 'CheckoutCompletePage':
        self.page.click(self.FINISH_BUTTON)
        from pages.Saucedemo.checkout_complete_page import CheckoutCompletePage
        return CheckoutCompletePage(self.page)
    
    def click_cancel(self) -> 'InventoryPage':
        self.page.click(self.CANCEL_BUTTON)
        from pages.Saucedemo.inventory_page import InventoryPage
        return InventoryPage(self.page)
    
    def verify_total_calc(self) -> bool:
        subtotal = self.get_subtotal()
        tax = self.get_tax()
        total = self.get_total()
        expected_total = round(subtotal + tax, 2)
        return total == expected_total