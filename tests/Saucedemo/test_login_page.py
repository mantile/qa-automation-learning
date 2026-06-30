import pytest

#TEST CASE 1: Login - Standard User
@pytest.mark.priority_high
@pytest.mark.smoke
def login_standart(maiin_page, user_logins, user_passwords):
    maiin_page.fill('#user-name', user_logins['standard'])
    maiin_page.fill('#password', user_passwords)
    maiin_page.click('#login-button')

    assert maiin_page.url == 'https://www.saucedemo.com/inventory.html'

#TEST CASE 2: Login - Locked Out User
@pytest.mark.priority_medium
@pytest.mark.regression
def login_locked(main_page, user_logins, user_passwords):
    main_page.fill('#user-name', user_logins['locked'])
    main_page.fill('#password', user_passwords)
    main_page.click('#login-button')

    error_message = main_page.locator('[data-test="error"]')
    assert error_message.is_visible()
    assert error_message.has_text("Epic sadface: Sorry, this user has been locked out.")

#TEST CASE 3: Login - Invalid Credentials
@pytest.mark.priority_medium
@pytest.mark.functional
def login_wrong_password(main_page, user_logins):
    main_page.fill('#user-name', user_logins['locked'])
    main_page.fill('#password', '123')
    main_page.click('#login-button')

    error_message = main_page.locator('[data-test="error"]')
    assert error_message.is_visible()
    assert error_message.has_text("Epic sadface: Username and password do not match any user in this service")

#TEST CASE 4: Add Single Item to Cart
@pytest.mark.priority_medium
@pytest.mark.functional
def login_wrong_login(main_page, user_passwords):
    main_page.fill('#user-name', '123')
    main_page.fill('#password', user_passwords)
    main_page.click('#login-button')

    error_message = main_page.locator('[data-test="error"]')
    assert error_message.is_visible()
    assert error_message.has_text("Epic sadface: Username and password do not match any user in this service")