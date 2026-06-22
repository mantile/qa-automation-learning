import pytest

from playwright.sync_api import sync_playwright

@pytest.fixture
def browser_page():
    '''creating the fixture'''
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        yield page
        browser.close()

def test_github_title(browser_page):
    browser_page.goto("https://github.com")
    assert browser_page.title() == "GitHub"