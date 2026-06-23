import pytest

#TEST CASE 4: Add Single Item to Cart
@pytest.mark.priority_high
@pytest.mark.smoke
def add_item_to_cart(user_standart_login):
    assert user_standart_login.locator('.shopping_cart_container').is_visible()
    user_standart_login.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    assert user_standart_login.locator('.shopping_cart_badge').is_visible()
    assert user_standart_login.text_content() == '1'

#TEST CASE 5: Remove Item from Cart
@pytest.mark.priority_medium
@pytest.mark.regression
def remove_item_from_cart(user_standart_login):
    assert user_standart_login.locator('.shopping_cart_badge').is_visible()
    user_standart_login.click('[data-test="remove-sauce-labs-backpack"]')
    assert not user_standart_login.locator('.shopping_cart_badge').is_visible()

#TEST CASE 6: Add Multiple Items to Cart
#@pytest.mark.priority_medium
#@pytest.mark.regression
#def add_multyple_items_to_card():