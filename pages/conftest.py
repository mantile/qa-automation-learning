import pytest

from playwright.sync_api import sync_playwright

@pytest.fixture
def browser_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture
def user_logins():
    return {
        'standard' : 'standard_user',
        'locked' : 'locked_out_user',
        'problem' : 'problem_user',
        'glitch' : 'performance_glitch_user',
        'error' : 'error_user',
        'visual' : 'visual_user'
    }

@pytest.fixture
def user_passwords():
    return 'secret_sauce'

@pytest.fixture
def main_page(browser_page):
    browser_page.goto("https://www.saucedemo.com/")
    return browser_page

@pytest.fixture
def user_standart_login(main_page):
    main_page.fill('#user-name', user_logins['standard'])
    main_page.fill('#password', user_passwords)
    main_page.click('#login-button')
    return main_page