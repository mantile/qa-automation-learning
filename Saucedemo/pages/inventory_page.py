import allure

from playwright.sync_api import Page

from pages.base_page import BasePage

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
        with allure.step("add item to cart"):
            self.page.click(f'[data-test="add-to-cart-{item_id}"]')
            return self
    
    def remove_item_from_card(self, item_id: str):
        with allure.step("remove item from cart"):
            self.page.click(f'[data-test="remove-{item_id}"]')
            return self
    
    def add_all_items_to_cart(self, items: list):
        with allure.step("add all items on page to cart"):
            for item in items:
                self.add_item_to_cart(item)
            return self
    
    def get_cart_count(self) -> int:
        with allure.step("get cart count"):
            if self.page.locator(self.CART_BADGE).is_visible():
                return int(self.page.locator(self.CART_BADGE).text_content())
            return 0
    
    def go_to_cart(self):
        with allure.step("opening cart page"):
            self.page.click(self.CART_LINK)
            from Saucedemo.pages.cart_page import CartPage
            return CartPage(self.page)
    
    def is_inventory_visible(self) -> bool:
        return self.page.locator(self.INVENTORY_LIST).is_visible()
    
    def get_item_name(self, index: int = 0) -> str:
        with allure.step("get item name"):
            return self.page.locator(self.ITEM_NAME).nth(index).text_content()
    
    def get_item_price(self, index: int = 0) -> str:
        with allure.step("get item price"):
            return self.page.locator(self.ITEM_PRICE).nth(index).text_content()
        
    def cart_badge(self):
        return self.page.locator('.shopping_cart_badge')
    
    def click_sort(self, option: str):
        with allure.step("pick needed sort type"):
            return self.get_by_datatest('product-sort-container').select_option(option)
        
    def get_prices_as_numbers(self):
        price_list = self.get_by_datatest(f"inventory-item-price").all_text_contents()
        return [float(price.replace("$", "")) for price in price_list]

    def open_item_page_by_id(self, item_id) -> 'InventoryItemPage':
        self.get_by_datatest(f'item-{item_id}-title-link').click()
        self.page.wait_for_load_state("networkidle")
        from Saucedemo.pages.inventory_item_page import InventoryItemPage
        return InventoryItemPage(self.page)