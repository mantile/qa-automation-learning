import pytest

from data.Saucedemo.test_data import TestData

#TEST CASE 1: Check backpack in cart
@pytest.mark.priority_high
@pytest.mark.regression
def test_check_backpack_in_card(cart_with_backpack):
    assert cart_with_backpack.is_card_is_empty() == False

#TEST CASE 2: Remove backpack
@pytest.mark.priority_critical
@pytest.mark.smoke
def test_remove_backpack_in_card(cart_with_backpack):
    cart_with_backpack.remove_item(TestData.ITEMS['backpack']['id'])
    assert cart_with_backpack.is_card_is_empty() == True

#TEST CASE 3: Checkout continue shopping
@pytest.mark.priority_high
@pytest.mark.smoke
def test_checkout_continue_shopping(cart_with_backpack):
    inventory_page = cart_with_backpack.continue_shopping()
    assert inventory_page.page.url == "https://www.saucedemo.com/inventory.html"

#TEST CASE 4: Checkout backpack
@pytest.mark.priority_cricial
@pytest.mark.smoke
def test_checkout_backpack(cart_with_backpack):
    checkout_page = cart_with_backpack.go_to_checkout()
    assert checkout_page.page.url == "https://www.saucedemo.com/checkout-step-one.html"
    assert checkout_page.is_checkout_page_loaded() == True