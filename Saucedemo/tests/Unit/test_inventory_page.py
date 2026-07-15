import allure
import pytest

from data.factories import DataFactory

@allure.epic("Saucedemo UI")
@allure.feature("Inventory page")
@pytest.mark.saucedemo
@pytest.mark.ui
class TestInventoryPage:

    @allure.title("TC-1: check does cart is empty")
    @allure.description("empty cart")
    @allure.tag("ui", "cart", "standard_user", "inventory")
    def test_check_empty_cart(standard_login):

        with allure.step("Check cart"):
            assert standard_login.is_inventory_visible()  is True
            assert standard_login.get_cart_count() == 0
            allure.attach(
                standard_login.page.screenshot(),
                name="empty cart",
                attachment_type=allure.attachment_type.PNG
            )

    @allure.title("TC-2: cart count check")
    @allure.description("add random item for cart count check")
    @allure.tag("ui", "cart", "standard_user", "inventory", "badge")
    def test_add_random_item_to_cart(standard_login):

        standard_login.add_item_to_cart(DataFactory.item.random_item)

        with allure.step("Check carts badge"):
            assert standard_login.page.locator('.shopping_cart_badge').is_visible()
            assert standard_login.page.locator('.shopping_cart_badge').text_content() == '1'
            allure.attach(
                standard_login.page.screenshot(),
                name="cart badge wirh one item",
                attachment_type=allure.attachment_type.PNG
            )

    @allure.title("TC-3: cart count check")
    @allure.description("add random item for cart count check")
    @allure.tag("ui", "cart", "standard_user", "inventory")
    def test_go_to_cart(add_backpack_to_cart):

        cart_page = add_backpack_to_cart.go_to_cart()

        with allure.step("Check cart page"):
            assert "cart" in cart_page.page.url
            assert cart_page.cart_page_is_loaded() is True
            allure.attach(
                cart_page.page.screenshot(),
                name="cart page is loaded",
                attachment_type=allure.attachment_type.PNG
            )
