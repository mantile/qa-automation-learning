import pytest
import allure
import time

from Saucedemo.data.test_data import TestData

from Saucedemo.pages.login_page import LoginPage

@allure.epic("Saucedemo Performance")
@allure.feature("Authorization")
@pytest.mark.saucedemo
@pytest.mark.performance
class TestUsersLoginPerformance:

    @allure.title("TC-1: performance_glitch_user login")
    @allure.description("performance login")
    @allure.tag("login", "performance_glitch_user", "performance")    
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