import pytest

from data.Saucedemo.test_data import TestData

#TEST CASE 1: Empty Cart - ready to tests
@pytest.mark.xdist_group(name="inventory_page_group")
@pytest.mark.saucedemo
@pytest.mark.ui
def test_empty_cart(standard_login):
    assert standard_login.is_inventory_visible()  is True
    assert standard_login.get_cart_count() == 0

#TEST CASE 2: Add Single Item to Cart
@pytest.mark.xdist_group(name="inventory_page_group")
@pytest.mark.saucedemo
@pytest.mark.ui
def test_add_backpack_to_cart(standard_login):
    standard_login.add_item_to_cart(TestData.ITEMS['backpack']['id'])
    assert standard_login.page.locator('.shopping_cart_badge').is_visible()
    assert standard_login.page.locator('.shopping_cart_badge').text_content() == '1'

#TEST CASE 3: Go to Cart
@pytest.mark.xdist_group(name="inventory_page_group")
@pytest.mark.saucedemo
@pytest.mark.ui
def test_go_to_cart(add_backpack_to_cart):
    cart_page = add_backpack_to_cart.go_to_cart()
    assert "cart" in cart_page.page.url
    assert cart_page.cart_page_is_loaded() is True