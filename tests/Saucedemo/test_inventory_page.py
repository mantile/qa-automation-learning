import pytest

from data.Saucedemo.test_data import TestData

#TEST CASE 1: Empty Cart - ready to tests
@pytest.mark.priority_medium
@pytest.mark.regression
def test_empety_cart(standard_login):
    assert standard_login.is_inventory_visible()  is True
    assert standard_login.get_cart_count() == 0

#TEST CASE 2: Add Single Item to Cart
@pytest.mark.priority_critical
@pytest.mark.smoke
def test_add_backpack_to_cart(standard_login):
    standard_login.add_item_to_cart(TestData.ITEMS['backpack']['id'])
    assert standard_login.page.locator('.shopping_cart_badge').is_visible()
    assert standard_login.page.locator('.shopping_cart_badge').text_content() == '1'

#TEST CASE 3: Go to Cart
@pytest.mark.priority_high
@pytest.mark.smoke
def test_go_to_cart(add_backpack_to_card):
    cart_page = add_backpack_to_card.go_to_cart()
    assert cart_page.page.url == "https://www.saucedemo.com/cart.html"
    assert cart_page.cart_page_is_loaded() == True