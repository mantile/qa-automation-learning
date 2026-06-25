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
    assert user_standart_login.text_content() == '1'
    user_standart_login.click('[data-test="remove-sauce-labs-backpack"]')
    assert not user_standart_login.locator('.shopping_cart_badge').is_visible()

#TEST CASE 6: Add Multiple Items to Cart
@pytest.mark.priority_medium
@pytest.mark.regression
def add_multyple_items_to_card(user_standart_login):
    assert add_multyple_items_to_card.locator('.shopping_cart_badge').is_visible()
    user_standart_login.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    user_standart_login.click('[data-test="add-to-cart-sauce-labs-bike-light"]')
    user_standart_login.click('[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]')
    assert user_standart_login.text_content() == '3'

#TEST CASE 7: Complete Checkout Process
@pytest.mark.priority_hight
@pytest.mark.smoke
def checkout_prices(add_multyple_items_to_card, checkout_data_input):
    add_multyple_items_to_card.click('.shopping_cart_badge')
