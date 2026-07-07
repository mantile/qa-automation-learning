import pytest
import allure
import hashlib

from data.Saucedemo.test_data import TestData

from pages.Saucedemo.login_page import LoginPage

@allure.epic("Saucedemo UI")
@allure.feature("Authorization")
@pytest.mark.saucedemo
@pytest.mark.ui
class TestUsersLogin:
    
    @allure.title("TC-1: standard_user login")
    @allure.description("standart login")
    @allure.tag("ui", "login", "standard_user")
    def test_login_standart_user(self, login_page: LoginPage):
        with allure.step("Fill username"):
            login_page.fill_username(TestData.USERS['standard']['username'])

        with allure.step("Fill password"):
            login_page.fill_password(TestData.PASSWORDS)

        with allure.step("Press login"):
            inventory_page = login_page.click_login_button()

        with allure.step("Check URL"):
            assert "inventory" in inventory_page.page.url
            allure.attach(
                inventory_page.page.screenshot(),
                name="successful_login",
                attachment_type=allure.attachment_type.PNG
            )

    @allure.title("TC-2: locked_out_user login")
    @allure.description("locked login")
    @allure.tag("ui", "login", "locked_out_user")    
    def test_login_locked_out_user(self, login_page: LoginPage): 
        with allure.step("Fill username and password"):
            login_page.fill_username(TestData.USERS['locked']['username'])
            login_page.fill_password(TestData.PASSWORDS)

        with allure.step("Press login"):
            login_page.click_login_button()

        with allure.step("Check URL"):
            assert login_page.get_error_message() == 'Epic sadface: Sorry, this user has been locked out.'
            allure.attach(
                login_page.page.screenshot(),
                name="successful_login",
                attachment_type=allure.attachment_type.PNG
            )

    # @allure.title("TC-3: problem_user login")
    # @allure.description("check items unique image")
    # @allure.tag("ui", "items", "problem_user", "image")    
    # def test_login_problem_user(self, login_page: LoginPage): 
    #     with allure.step("Fill username and password"):
    #         login_page.fill_username(TestData.USERS['problem']['username'])
    #         login_page.fill_password(TestData.PASSWORDS)

    #     with allure.step("Press login"):
    #         inventory_page = login_page.click_login_button()

    #     with allure.step("Check items images for unique"):
    #         items = inventory_page.get_all_datatest_items("inventory-item")
    #         for item in items:
                
            
            
    #         allure.attach(
    #             inventory_page.page.screenshot(),
    #             name="successful_login",
    #             attachment_type=allure.attachment_type.PNG
    #         )       

    @allure.title("TC-3: problem_user login")
    @allure.description("locked login")
    @allure.tag("ui", "login", "problem_user")    
    def test_login_problem_user(self, login_page: LoginPage): 
        with allure.step("Fill username and password"):
            login_page.fill_username(TestData.USERS['problem']['username'])
            login_page.fill_password(TestData.PASSWORDS)

        with allure.step("Press login"):
            inventory_page = login_page.click_login_button()

        with allure.step("Check item img"):
            assert "inventory" in inventory_page.page.url
            allure.attach(
                inventory_page.page.screenshot(),
                name="successful_login",
                attachment_type=allure.attachment_type.PNG
            )
        
    @allure.title("TC-4: login only with password")
    @allure.description("login without filled username")
    @allure.tag("ui", "login")
    def test_login_with_password(self, login_page: LoginPage):
        with allure.step("Fill password"):
            login_page.fill_password(TestData.PASSWORDS)

        with allure.step("Press login"):
            login_page.click_login_button()

        with allure.step("Check error"):
            assert login_page.get_error_message() == "Epic sadface: Username is required"
            allure.attach(
                login_page.page.screenshot(),
                name="successful_login",
                attachment_type=allure.attachment_type.PNG
            )

    @allure.title("TC-5: login only with username")
    @allure.description("login without filled password")
    @allure.tag("ui", "login")
    def test_login_with_username(self, login_page: LoginPage):
        with allure.step("Fill username"):
            login_page.fill_username(TestData.USERS['problem']['username'])

        with allure.step("Press login"):
            login_page.click_login_button()

        with allure.step("Check error"):
            assert login_page.get_error_message() == "Epic sadface: Password is required"
            allure.attach(
                login_page.page.screenshot(),
                name="successful_login",
                attachment_type=allure.attachment_type.PNG
            )

    @allure.title("TC-6: login without fills")
    @allure.description("login without any fills")
    @allure.tag("ui", "login")
    def test_login_without_fills(self, login_page: LoginPage):
        with allure.step("Press login"):
            login_page.click_login_button()

        with allure.step("Check error"):
            assert login_page.is_error_visible() is True
            allure.attach(
                login_page.page.screenshot(),
                name="successful_login",
                attachment_type=allure.attachment_type.PNG
            )

    @allure.title("TC-7: close the error message")
    @allure.description("chek the close of error message")
    @allure.tag("ui", "login")
    def test_login_error_closing(self, login_page: LoginPage):
        with allure.step("Press login"):
            login_page.click_login_button()

        with allure.step("Check error"):
            assert login_page.is_error_visible() is True
            login_page.page.locator('.error-button').click()
            allure.attach(
                login_page.page.screenshot(),
                name="successful_login",
                attachment_type=allure.attachment_type.PNG
            )