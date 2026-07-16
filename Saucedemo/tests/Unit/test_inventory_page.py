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
    def test_check_empty_cart(self, standard_login):

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
    @allure.tag("ui", "cart", "standard_user", "inventory")
    def test_go_to_cart(self, add_backpack_to_cart):

        cart_page = add_backpack_to_cart.go_to_cart()

        with allure.step("Check cart page"):
            assert "cart" in cart_page.page.url
            assert cart_page.cart_page_is_loaded() is True
            allure.attach(
                cart_page.page.screenshot(),
                name="cart page is loaded",
                attachment_type=allure.attachment_type.PNG
            )

    @allure.title("TC-3: add items to cart")
    @allure.description("add all items by one")
    @allure.tag("ui", "cart", "standard_user", "inventory")
    @pytest.mark.parametrize(
        "item",
        [
            DataFactory.item.backpack(),
            DataFactory.item.bike_light(),
            DataFactory.item.t_shirt(),
            DataFactory.item.fleece(),
            DataFactory.item.onesie(),
            DataFactory.item.red_t_shirt()
        ]
    )
    def test_add_item_to_cart_by_one(self, item, standard_login):
        standard_login.add_item_to_cart(item)

        with allure.step("Check carts badge"):
            assert standard_login.cart_badge().is_visible()
            assert standard_login.cart_badge().text_content() == '1'
            allure.attach(
                standard_login.page.screenshot(),
                name=f"{item} was added to cart",
                attachment_type=allure.attachment_type.PNG
            )

    # @allure.title("TC-3: add items to cart")
    # @allure.description("add all items by one")
    # @allure.tag("ui", "cart", "standard_user", "inventory")
    # @pytest.mark.parametrize(
    #     "sort_func", "object", "expect"
    #     [
    #         DataFactory.item.backpack(),
    #         DataFactory.item.bike_light(),
    #         DataFactory.item.t_shirt(),
    #         DataFactory.item.fleece(),
    #         DataFactory.item.onesie(),
    #         DataFactory.item.red_t_shirt()
    #     ]
    # )