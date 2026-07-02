from playwright.sync_api import Page
from pages.Saucedemo.base_page import BasePage


class InventoryItemPage(BasePage):

    BACK_TO_PRODUCTS_BUTTON = '#back-to-products'
    
    ITEM_NAME = '[data-test="inventory-item-name"]'
    ITEM_DESC = '[data-test="inventory-item-desc"]'
    ITEM_PRICE = '[data-test="inventory-item-price"]'
    ITEM_IMAGE = '[data-test^="item-"]'
    
    ADD_TO_CART_BUTTON = '[data-test="add-to-cart"]'
    REMOVE_BUTTON = '[data-test="remove"]'
    
    CART_BADGE = '.shopping_cart_badge'
    CART_LINK = '.shopping_cart_link'
    
    SECONDARY_HEADER = '[data-test="secondary-header"]'

    def __init__(self, page: Page):
        super().__init__(page)
        self._expected_elements = [
            self.BACK_TO_PRODUCTS_BUTTON,
            self.ITEM_NAME,
            self.ITEM_DESC,
            self.ITEM_PRICE,
            self.ITEM_IMAGE,
            self.ADD_TO_CART_BUTTON,
            self.CART_LINK,
        ]

    def get_item_name(self) ->str:
        return self.page.locator(self.ITEM_NAME).text_content()
    
    def get_item_desc(self) ->str:
        return self.page.locator(self.ITEM_DESC).text_content()
    
    def get_item_price(self) ->str:
        return self.page.locator(self.ITEM_PRICE).text_content()

    def add_to_card(self):
        self.page.click(self.ADD_TO_CART_BUTTON)
        return self
    
    def remove_item_from_card(self):
        self.page.click(self.REMOVE_BUTTON)
        return self
    
    def back_to_products(self):
        self.page.click(self.BACK_TO_PRODUCTS_BUTTON)
        return self
    
    def get_card_count(self) -> int:
        if self.page.locator(self.CART_BADGE).is_visible():
            return self.page.locator(self.CART_BADGE).text_content()
        return 0
    
    def go_to_card(self) -> 'CartPage':
        self.page.click(self.CART_LINK)
        from pages.Saucedemo.cart_page import CartPage
        return CartPage(self.page)