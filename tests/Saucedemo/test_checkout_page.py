import pytest

#TEST CASE 1: Cancel - back to cart
@pytest.mark.priority_high
@pytest.mark.regression
def test_checkout_cancel(checkout_with_backpack):
    cart_page = checkout_with_backpack.click_cancel()
    assert "cart" in cart_page.page.url

#TEST CASE 2: Fill data and continue
@pytest.mark.priority_critical
@pytest.mark.smoke
def test_continue_checkout(checkout_with_backpack):
    checkout_with_backpack.fill_first_name("First")
    checkout_with_backpack.fill_last_name("Person")
    checkout_with_backpack.fill_postal_code("777X")
    cart_page = checkout_with_backpack.click_continue()
    assert "checkout-step-two" in cart_page.page.url