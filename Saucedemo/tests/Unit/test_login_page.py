import pytest
import allure

from pages.login_page import LoginPage

from data.factories import DataFactory

@allure.epic("Saucedemo UI")
@allure.feature("Authorization")
@pytest.mark.saucedemo
@pytest.mark.ui
class TestUsersLogin:
    
    @allure.title("TC-1: valid users login")
    @allure.description("login all valid users")
    @allure.tag("ui", "login", "standard_user", "problem_user", "error_user", "visual_user")
    @pytest.mark.parametrize(
        "username", 
        [
            DataFactory.user.standart(),
            DataFactory.user.problem(),
            DataFactory.user.error(),
            DataFactory.user.visual()
        ]
    )
    def test_login_valid_users(self, username, login_page: LoginPage):
        with allure.step("Standart user"):
            inventory_page = login_page.login(username, DataFactory.user.password())

        with allure.step("Check URL"):
            assert "inventory" in inventory_page.page.url
            allure.attach(
                inventory_page.page.screenshot(),
                name=f"login_success_{username}",
                attachment_type=allure.attachment_type.PNG
            )

    @allure.title("TC-2: locked_out_user login")
    @allure.description("locked login")
    @allure.tag("ui", "login", "locked_out_user")    
    def test_login_locked_out_user(self, login_page: LoginPage): 
        with allure.step("Locked user"):
            login_page.login(DataFactory.user.locked(), DataFactory.user.password())

        with allure.step("Check URL and error"):
            assert login_page.get_error_message() == 'Epic sadface: Sorry, this user has been locked out.'
            assert "inventory" not in login_page.page.url
            allure.attach(
                login_page.page.screenshot(),
                name="locked_error_login",
                attachment_type=allure.attachment_type.PNG
            )   
        
    @allure.title("TC-3: login with empty fills combination")
    @allure.description("login without filled username, password or password and username")
    @allure.tag("ui", "login", "negative")
    @pytest.mark.parametrize(
        "username, password, error",
        [
            pytest.param("", DataFactory.user.password(), "Epic sadface: Username is required", id="password only"),
            pytest.param(DataFactory.user.standart(), "", "Epic sadface: Password is required", id="login only"),
            pytest.param("", "", "Epic sadface: Username is required", id="empty fills")
        ]
    )
    def test_login_negative_scenarios(self, username, password, error, login_page: LoginPage):
        login_page.login(username, password)

        with allure.step("Check error and URL"):
            assert login_page.get_error_message() == error
            assert "inventory" not in login_page.page.url
            allure.attach(
                login_page.page.screenshot(),
                name=f"login_error_{password}_{username}",
                attachment_type=allure.attachment_type.PNG
            )

    @allure.title("TC-4: close the error message")
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