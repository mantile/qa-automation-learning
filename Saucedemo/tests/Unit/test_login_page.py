import pytest
import allure

from pages.login_page import LoginPage

from data.factories import DataFactory

@allure.epic("Saucedemo UI")
@allure.feature("Authorization")
@pytest.mark.saucedemo
@pytest.mark.ui
class TestUsersLogin:
    
    @allure.title("TC-1: standard_user login")
    @allure.description("standard login")
    @allure.tag("ui", "login", "standard_user")
    def test_login_standard_user(self, login_page: LoginPage):
        with allure.step("Standart user"):
            inventory_page = login_page.login(DataFactory.user.standart(), DataFactory.user.password())

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
        with allure.step("Locked user"):
            login_page.login(DataFactory.user.locked, DataFactory.user.password())

        with allure.step("Check URL and error"):
            assert login_page.get_error_message() == 'Epic sadface: Sorry, this user has been locked out.'
            assert "inventory" not in login_page.page.url
            allure.attach(
                login_page.page.screenshot(),
                name="locked_error_login",
                attachment_type=allure.attachment_type.PNG
            )   

    @allure.title("TC-3: problem_user login")
    @allure.description("locked login")
    @allure.tag("ui", "login", "problem_user")    
    def test_login_problem_user(self, login_page: LoginPage): 
        with allure.step("Problem user"):
            inventory_page = login_page.login(DataFactory.user.problem(), DataFactory.user.password())

        with allure.step("Check item img"):
            assert "inventory" in inventory_page.page.url
            allure.attach(
                inventory_page.page.screenshot(),
                name="problem_user_login",
                attachment_type=allure.attachment_type.PNG
            )
        
    @allure.title("TC-4: login only with password")
    @allure.description("login without filled username")
    @allure.tag("ui", "login")
    def test_login_with_password(self, login_page: LoginPage):
        login_page.fill_password(DataFactory.user.password())
        login_page.click_login_button()

        with allure.step("Check error and URL"):
            assert login_page.get_error_message() == "Epic sadface: Username is required"
            assert "inventory" not in login_page.page.url
            allure.attach(
                login_page.page.screenshot(),
                name="username_missing_error",
                attachment_type=allure.attachment_type.PNG
            )

    @allure.title("TC-5: login only with username")
    @allure.description("login without filled password")
    @allure.tag("ui", "login")
    def test_login_with_username(self, login_page: LoginPage):
        login_page.fill_username(DataFactory.user.standart())
        login_page.click_login_button()

        with allure.step("Check error and URL"):
            assert login_page.get_error_message() == "Epic sadface: Password is required"
            assert "inventory" not in login_page.page.url
            allure.attach(
                login_page.page.screenshot(),
                name="password_missing_error",
                attachment_type=allure.attachment_type.PNG
            )

    @allure.title("TC-6: login without fills")
    @allure.description("login without any fills")
    @allure.tag("ui", "login")
    def test_login_without_fills(self, login_page: LoginPage):
        login_page.click_login_button()

        with allure.step("Check error and URL"):
            assert login_page.is_error_visible() is True
            assert "inventory" not in login_page.page.url
            allure.attach(
                login_page.page.screenshot(),
                name="username_password_missing_error",
                attachment_type=allure.attachment_type.PNG
            )

    @allure.title("TC-7: close the error message")
    @allure.description("check the close of error message")
    @allure.tag("ui", "login")
    def test_login_error_closing(self, login_page: LoginPage):
        login_page.click_login_button()

        with allure.step("Check error"):
            assert login_page.is_error_visible() is True
            login_page.close_error_message()
            allure.attach(
                login_page.page.screenshot(),
                name="closed_error",
                attachment_type=allure.attachment_type.PNG
            )