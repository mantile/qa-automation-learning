import pytest

from playwright.sync_api import sync_playwright

from pages.Saucedemo.login_page import LoginPage

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