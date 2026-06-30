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
        self._expected_elements = [
            self.USERNAME_INPUT,
            self.PASSWORD_INPUT,
            self.LOGIN_BUTTON
        ]

    def fill_username(self, username: str):
        self.page.fill(self.USERNAME_INPUT, username)
        return self

    def fill_password(self, password: str):
        self.page.fill(self.PASSWORD_INPUT, password)
        return self
    
    def click_login_button(self):
        self.page.click(self.LOGIN_BUTTON)
        return self
    
    def login(self, username: str, password: str):
        self.fill_username(username)
        self.fill_password(password)
        self.click_login_button()

        if self.is_error_visible():
            return self
        return InventoryPage(self.page)
    
    def is_login_page_loaded(self) -> bool:
        return (self.is_element_visible(self.USERNAME_INPUT) and
                self.is_element_visible(self.PASSWORD_INPUT) and
                self.is_element_visible(self.LOGIN_BUTTON))