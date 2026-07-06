from playwright.sync_api import Page
from pages.Saucedemo.base_page import BasePage

class InventoryPage(BasePage):

    INVENTORY_LIST = '.inventory_list'
    CART_BADGE = '.shopping_cart_badge'
    CART_LINK = '.shopping_cart_link'
    ITEM_NAME = '.inventory_item_name'
    ITEM_PRICE = '.inventory_item_price'
    
    URL = "https://www.saucedemo.com/inventory.html"

    def __iadd__(self, page: Page):
        super().__init__(page)
        self._expected_elements = [
            self.INVENTORY_LIST,
            self.CART_LINK
        ]

    def add_item_to_cart(self, item_id: str):
        self.page.click(f'[data-test="add-to-cart-{item_id}"]')
        return self
    
    def remove_item_from_card(self, item_id: str):
        self.page.click(f'[data-test="remove-{item_id}"]')
        return self
    
    def add_all_items_to_cart(self, items: list):
        for item in items:
            self.add_item_to_cart(item)
        return self
    
    def get_cart_count(self) -> int:
        if self.page.locator(self.CART_BADGE).is_visible():
            return int(self.page.locator(self.CART_BADGE).text_content())
        return 0
    
    def go_to_cart(self):
        self.page.click(self.CART_LINK)
        from pages.Saucedemo.cart_page import CartPage
        return CartPage(self.page)
    
    def is_inventory_visible(self) -> bool:
        return self.page.locator(self.INVENTORY_LIST).is_visible()
    
    def get_item_name(self, index: int = 0) -> str:
        return self.page.locator(self.ITEM_NAME).nth(index).text_content()
    
    def get_item_price(self, index: int = 0) -> str:
        return self.page.locator(self.ITEM_PRICE).nth(index).text_content()
    
    # def get_all_datatest_items(self, datatest_name: str):
    #     return self.page.locator(f'[data-test="{datatest_name}"]').all()
    
