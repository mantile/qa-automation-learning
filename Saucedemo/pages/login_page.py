import allure

from playwright.sync_api import Page

from Saucedemo.pages.base_page import BasePage
from Saucedemo.pages.inventory_page import InventoryPage

from Saucedemo.data.test_data import TestData

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
        with allure.step("Fill username"):
            self.page.fill(self.USERNAME_INPUT, username)
            return self

    def fill_password(self, password: str):
        with allure.step("Fill password"):
            self.page.fill(self.PASSWORD_INPUT, password)
            return self
    
    def click_login_button(self):
        with allure.step("Press login"):
            self.page.click(self.LOGIN_BUTTON)
            return InventoryPage(self.page)
    
    def login(self, username: str, password: str):
        with allure.step("Fill username and password"):
            self.fill_username(username)
            self.fill_password(password)
            self.click_login_button()

            if self.is_error_visible():
                return self
            from Saucedemo.pages.inventory_page import InventoryPage
            return InventoryPage(self.page)
    
    def is_login_page_loaded(self) -> bool:
        return (self.is_element_visible(self.USERNAME_INPUT) and
                self.is_element_visible(self.PASSWORD_INPUT) and
                self.is_element_visible(self.LOGIN_BUTTON))
    
    def close_error_message(self):
        with allure.step("Close errors message"):
            self.page.locator('.error-button').click()
    