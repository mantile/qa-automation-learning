import pytest

from data.Saucedemo.test_data import TestData

#TEST CASE 1: Login - Standard User
@pytest.mark.saucedemo
@pytest.mark.ui
def test_login_standard(login_page):
    login_page.fill_username(TestData.USERS['standard']['username'])
    login_page.fill_password(TestData.PASSWORDS)
    login_page.click_login_button()
    assert "inventory" in login_page.page.url 

