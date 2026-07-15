import allure
import pytest

from pages.login_page import LoginPage

from data.factories import DataFactory

@allure.epic("Saucedemo UI")
@allure.feature("Menu")
@pytest.mark.saucedemo
@pytest.mark.ui
class TestMenu:
    @allure.title("TC-1: open vertical menu")
    @allure.description("menu")
    @allure.tag("ui", "menu")
    def test_open_menu(self, login_page: LoginPage):
        with allure.step("Logining as standart user"):
            inventory_page = login_page.login(DataFactory.user.standart, DataFactory.user.password)
            assert "inventory" in inventory_page.page.url

        with allure.step("Open menu"):
            inventory_page.page.get_by_role('button', name="Open Menu").click()
            assert inventory_page.get_by_datatest('inventory-sidebar-link').is_visible() is True
            allure.attach(
                login_page.page.screenshot(),
                name="menu is visible",
                attachment_type=allure.attachment_type.PNG
            )
