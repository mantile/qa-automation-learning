import pytest

from data.factories import DataFactory


#TEST CASE 1: Check backpack in cart
@pytest.mark.xdist_group(name="cart_page_group")
@pytest.mark.saucedemo
@pytest.mark.ui
def test_check_backpack_in_cart(cart_with_backpack):
    assert cart_with_backpack.is_cart_empty() is False

#TEST CASE 2: Remove backpack
@pytest.mark.xdist_group(name="cart_page_group")
@pytest.mark.saucedemo
@pytest.mark.ui
def test_remove_backpack_in_cart(cart_with_backpack):
    cart_with_backpack.remove_item(DataFactory.item.backpack())
    assert cart_with_backpack.is_cart_empty() is True

#TEST CASE 3: Checkout continue shopping
@pytest.mark.xdist_group(name="cart_page_group")
@pytest.mark.saucedemo
@pytest.mark.ui
def test_checkout_continue_shopping(cart_with_backpack):
    inventory_page = cart_with_backpack.continue_shopping()
    assert "inventory" in inventory_page.page.url

#TEST CASE 4: Checkout backpack
@pytest.mark.saucedemo
@pytest.mark.ui
def test_checkout_backpack(cart_with_backpack):
    checkout_page = cart_with_backpack.go_to_checkout()
    assert "checkout-step-one" in checkout_page.page.url
    assert checkout_page.is_checkout_page_loaded() is True