import pytest

#TEST CASE 1: Cancel
@pytest.mark.priority_high
@pytest.mark.regression
def test_cancel_checkout_owerview(checkout_with_backpack_complite):
    inventory_page = checkout_with_backpack_complite.click_cancel()
    assert inventory_page.page.url == "https://www.saucedemo.com/inventory.html"


#TEST CASE 2: Finish
@pytest.mark.priority_critical
@pytest.mark.smoke
def test_complite_checkout(checkout_with_backpack_complite):
    complite_page = checkout_with_backpack_complite.click_finish()
    assert complite_page.page.url == "https://www.saucedemo.com/checkout-complete.html"
    assert complite_page.complite_page_is_loaded() is True