import pytest

from Saucedemo.data.test_data import TestData

@pytest.mark.saucedemo
@pytest.mark.e2e
def test_e2e_standard_user_positive_order_flow(login_page):
    username = TestData.USERS['standard']['username']
    password = TestData.PASSWORDS
    item_name = TestData.ITEMS['backpack']['id']

    login_page.open_page()
    login_page.fill_username(username)
    login_page.fill_password(password)

    inventory_page = login_page.click_login_button()
    assert inventory_page.is_inventory_visible()  is True
    assert inventory_page.get_cart_count() == 0

    inventory_page.add_item_to_cart(item_name)
    assert inventory_page.get_cart_count() == 1

    cart_page = inventory_page.go_to_cart()
    assert cart_page.is_cart_empty() is False

    checkout_page = cart_page.go_to_checkout()
    checkout_page.fill_first_name("Name")
    checkout_page.fill_last_name("L name")
    checkout_page.fill_postal_code("133XL")

    checkout_overview_page = checkout_page.click_continue()
    
    checkout_complete_page = checkout_overview_page.click_finish()

    inventory_page = checkout_complete_page.click_back()
    assert inventory_page.is_inventory_visible()  is True
    assert inventory_page.get_cart_count() == 0