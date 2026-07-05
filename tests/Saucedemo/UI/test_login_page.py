import pytest
import allure
import time

from data.Saucedemo.test_data import TestData

from pages.Saucedemo.login_page import LoginPage

#TEST CASE 1: Login - Standard User
@pytest.mark.saucedemo
@pytest.mark.ui
def test_login_standard(login_page):
    login_page.fill_username(TestData.USERS['standard']['username'])
    login_page.fill_password(TestData.PASSWORDS)
    login_page.click_login_button()
    assert "inventory" in login_page.page.url 

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
            assert login_page.page.url == "https://www.saucedemo.com/"
            assert login_page.get_error_message() == 'Epic sadface: Sorry, this user has been locked out.'
            allure.attach(
                login_page.page.screenshot(),
                name="successful_login",
                attachment_type=allure.attachment_type.PNG
            )

    @allure.title("TC-3: problem_user login")
    @allure.description("locked login")
    @allure.tag("ui", "login", "problem_user")    
    def test_login_problem_user(self, login_page: LoginPage): 
        with allure.step("Fill username and password"):
            login_page.fill_username(TestData.USERS['problem']['username'])
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

    @allure.title("TC-4: performance_glitch_user login")
    @allure.description("performance login")
    @allure.tag("ui", "login", "performance_glitch_user", "performance")    
    def test_login_performance_glitch_user(self, login_page: LoginPage): 
        with allure.step("Fill username and password"):
            login_page.fill_username(TestData.USERS['glitch']['username'])
            login_page.fill_password(TestData.PASSWORDS)

        with allure.step("Press login and measure page load time"):
            start_time = time.time()
            inventory_page = login_page.click_login_button()
            inventory_page.page.wait_for_load_state("networkidle")
            load_time = time.time() - start_time
            
            allure.attach(
                f"{load_time:.2f} seconds",
                name="Page Load Time",
                attachment_type=allure.attachment_type.TEXT
            )
    
        with allure.step("Verify page loaded"):
            assert inventory_page.is_inventory_visible() is True
            allure.attach(
                inventory_page.page.screenshot(),
                name="Inventory Page Loaded",
                attachment_type=allure.attachment_type.PNG
            )

    @allure.title("TC-5: problem_user login")
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