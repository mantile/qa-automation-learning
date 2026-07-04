import pytest

#TEST CASE 1: Cancel
@pytest.mark.priority_high
@pytest.mark.regression
def test_cancel_checkout_overview(checkout_with_backpack_complete):
    inventory_page = checkout_with_backpack_complete.click_cancel()
    assert "inventory" in inventory_page.page.url


#TEST CASE 2: Finish
@pytest.mark.priority_critical
@pytest.mark.smoke
def test_complete_checkout(checkout_with_backpack_complete):
    complete_page = checkout_with_backpack_complete.click_finish()
    assert "checkout-complete" in complete_page.page.url
    assert complete_page.complete_page_is_loaded() is True