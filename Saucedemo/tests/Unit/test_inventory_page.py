import allure
import pytest

from data.factories import DataFactory

@allure.epic("Saucedemo UI")
@allure.feature("Inventory page")
@pytest.mark.saucedemo
@pytest.mark.ui
class TestInventoryPageFast:

    @allure.title("TC-6: open item page")
    @allure.description("check items personal pages")
    @allure.tag("ui", "inventory", "standard_user", "item page")
    @pytest.mark.parametrize(
        "item_id",
        [
            pytest.param(DataFactory.item.backpack_id(), id="backpack"),
            pytest.param(DataFactory.item.bike_light_id(), id="bike_light"),
            pytest.param(DataFactory.item.t_shirt_id(), id="bolt_t_shirt"),
            pytest.param(DataFactory.item.fleece_id(), id="fleece_jacket"),
            pytest.param(DataFactory.item.onesie_id(), id="onesie"),
            pytest.param(DataFactory.item.red_t_shirt_id(), id="red_t_shirt")
        ]
    )
    def test_open_items_page(self, standard_login_session, item_id):
        item_page = standard_login_session.open_item_page_by_id(item_id)
        with allure.step("checking item page"):
            assert "inventory-item" in item_page.page.url
            allure.attach(
            standard_login_session.page.screenshot(),
            name=f"{item_id} page",
            attachment_type=allure.attachment_type.PNG
        )
        standard_login_session.page.go_back()
        standard_login_session.page.wait_for_load_state("networkidle")

@allure.epic("Saucedemo UI")
@allure.feature("Inventory page")
@pytest.mark.saucedemo
@pytest.mark.ui
class TestInventoryPageSafe:

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
            assert "cart.html" in cart_page.page.url
            assert cart_page.cart_page_is_loaded() is True
            allure.attach(
                cart_page.page.screenshot(),
                name="cart page is loaded",
                attachment_type=allure.attachment_type.PNG
            )

    @allure.title("TC-3: TC-3: add each item to cart individually")
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
        with allure.step(f"Adding item with id {item}"):
            standard_login.add_item_to_cart(item)
            with allure.step("Check carts badge"):
                assert standard_login.cart_badge().is_visible()
                assert standard_login.cart_badge().text_content() == '1'
                allure.attach(
                    standard_login.page.screenshot(),
                    name=f"{item} was added to cart",
                    attachment_type=allure.attachment_type.PNG
                )

    @allure.title("TC-4: filter tests")
    @allure.description("check all type of filters")
    @allure.tag("ui", "inventory", "standard_user", "filter")
    @pytest.mark.parametrize(
        "sort_func, find_obj, expect", 
        [
            pytest.param("az", "name", True , id="A to Z sort"),
            pytest.param("za", "name", False , id="Z to A sort"),
            pytest.param("lohi", "price", True , id="Low to High sort"),
            pytest.param("hilo", "price", False , id="High to Low sort")
        ]
    )
    def test_inventory_page_filters(self, standard_login, sort_func, find_obj, expect):
        standard_login.click_sort(sort_func)
        if find_obj == "price":
            inv_obj_list = standard_login.get_prices_as_numbers()
        else:
            inv_obj_list = standard_login.get_by_datatest(f"inventory-item-{find_obj}").all_text_contents()
        with allure.step("checking the sort"):
            if expect is True:
                assert inv_obj_list == sorted(inv_obj_list)
            else:
                assert inv_obj_list == sorted(inv_obj_list, reverse=True)
        allure.attach(
                standard_login.page.screenshot(),
                name=f"{sort_func}",
                attachment_type=allure.attachment_type.PNG
            )
        
    @allure.title("TC-5: cart count 3/6")
    @allure.description("check avg and max items add to cart")
    @allure.tag("ui", "inventory", "standard_user", "cart")
    @pytest.mark.parametrize(
        "count",
        [
            pytest.param(3, id="3 items"),
            pytest.param(6, id="6 items")
        ]
    )
    def test_add_3_and_6_items_to_cart(self, standard_login, count):
        items = DataFactory.item.random_items(count)
        for item in items:
            with allure.step(f"{item} was added"):
                standard_login.add_item_to_cart(item)
        with allure.step("checking items cart count"):
            assert standard_login.get_cart_count() == count
            allure.attach(
                standard_login.page.screenshot(),
                name=f"item count is {count}",
                attachment_type=allure.attachment_type.PNG
            )

    