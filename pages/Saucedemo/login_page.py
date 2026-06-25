from playwright.sync_api import Page
from pages.Saucedemo.base_page import BasePage
from pages.Saucedemo.inventory_page import InventoryPage

class LoginPage(BasePage):
    USERNAME_INPUT = '#user-name'
    PASSWORD_INPUT = '#password'
    LOGIN_BUTTON = '#login-button'
    ERROR_MESSAGE = '[data-test="error"]'

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        self.navigate_to("https://www.saucedemo.com/")
        self.wait_for_element(self.LOGIN_BUTTON)
        return self
    
    def fill_username(self, username: str):
        self.page.fill(self.USERNAME_INPUT, username)
        return self

    def fill_password(self, password: str):
        self.page.fill(self.PASSWORD_INPUT, password)
        return self
    
    def click_login_button(self):
        self.page.click(self.LOGIN_BUTTON)
        return self
    
    