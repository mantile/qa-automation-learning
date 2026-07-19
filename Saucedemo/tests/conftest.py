import pytest
import allure

from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage

from data.factories import DataFactory

@pytest.fixture
def browser_page():
    with allure.step("creat browser page"):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            yield page
            browser.close()

@pytest.fixture
def login_page(browser_page):
    with allure.step("go to login page"):
        return LoginPage(browser_page).open_page()

@pytest.fixture
def standard_login(login_page) -> InventoryPage:
    with allure.step("standart user login"):
        user = DataFactory.user.standart()
        password = DataFactory.user.password()
        return login_page.login(user, password)

@pytest.fixture
def add_backpack_to_cart(standard_login):
    with allure.step("add backpack to cart"):
        item = DataFactory.item.backpack()
        return standard_login.add_item_to_cart(item)

@pytest.fixture
def cart_with_backpack(add_backpack_to_cart) -> CartPage:
    with allure.step("go to cart with backpack"):
        return add_backpack_to_cart.go_to_cart()

@pytest.fixture
def checkout_with_backpack(cart_with_backpack) -> CheckoutPage:
    with allure.step("go to checkout with backpack"):
        return cart_with_backpack.go_to_checkout()

@pytest.fixture
def checkout_with_backpack_complete(checkout_with_backpack) -> CheckoutOverviewPage:
    with allure.step("go to complite checkout with backpack"):
        checkout_with_backpack.fill_checkout_info()
        return checkout_with_backpack.click_continue()

@pytest.fixture(scope="session")
def browser_page_session():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture(scope="session")
def standard_login_session(browser_page_session):
    login_page = LoginPage(browser_page_session).open_page()
    user = DataFactory.user.standart()
    password = DataFactory.user.password()
    return login_page.login(user, password)
