import pytest

from playwright.sync_api import sync_playwright

from data.Saucedemo.test_data import TestData
from pages.Saucedemo.login_page import LoginPage
from pages.Saucedemo.inventory_page import InventoryPage
from pages.Saucedemo.cart_page import CartPage
from pages.Saucedemo.checkout_page import CheckoutPage
from pages.Saucedemo.checkout_overview_page import CheckoutOverviewPage

@pytest.fixture
def browser_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture
def login_page(browser_page):
    return LoginPage(browser_page).open_page()

@pytest.fixture
def standard_login(login_page) -> InventoryPage:
    user = TestData.USERS['standard']['username']
    password = TestData.PASSWORDS
    return login_page.login(user, password)

@pytest.fixture
def add_backpack_to_cart(standard_login):
    item = TestData.ITEMS['backpack']['id']
    return standard_login.add_item_to_cart(item)

@pytest.fixture
def cart_with_backpack(add_backpack_to_cart) -> CartPage:
    return add_backpack_to_cart.go_to_cart()

@pytest.fixture
def checkout_with_backpack(cart_with_backpack) -> CheckoutPage:
    return cart_with_backpack.go_to_checkout()

@pytest.fixture
def checkout_with_backpack_complete(checkout_with_backpack) -> CheckoutOverviewPage:
    checkout_with_backpack.fill_checkout_info()
    return checkout_with_backpack.click_continue()