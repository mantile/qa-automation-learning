import pytest
import allure

from restful_booker.data.api.api_test_data import get_updated_booking_data

@allure.epic("Restful-booker")
@allure.feature("Booking")
@pytest.mark.restfulbooker
@pytest.mark.api
class TestBooking:
    
    @allure.title("TC-1: get all booking")
    @allure.description("get all booking")
    @allure.tag("api", "booking", "get")
    def test_get_all_bookings(self, booking_endpoints):
        response = booking_endpoints.get_all_bookings()
        assert response.status_code == 200
        bookings = response.json()
        print(bookings)
        assert isinstance(bookings, list)
        assert len(bookings) > 0
    
    @allure.title("TC-2: create new booking")
    @allure.description("creating new booking")
    @allure.tag("api", "booking", "post")
    def test_create_booking(self, booking_endpoints, test_booking_data):
        response = booking_endpoints.create_booking(test_booking_data)
        assert response.status_code == 200
        data = response.json()
        assert "bookingid" in data
        assert data["booking"]["firstname"] == test_booking_data["firstname"]
        assert data["booking"]["lastname"] == test_booking_data["lastname"]
    
    @allure.title("TC-3: get booking by id")
    @allure.description("get created booking by id")
    @allure.tag("api", "booking", "get")
    def test_get_booking_by_id(self, booking_endpoints, created_booking):
        response = booking_endpoints.get_booking_by_id(created_booking)
        assert response.status_code == 200
        data = response.json()
        assert data["firstname"] is not None
        assert data["lastname"] is not None
    
    @allure.title("TC-4: update booking")
    @allure.description("update created booking")
    @allure.tag("api", "booking", "post")
    def test_update_booking(self, auth_booking_endpoints, created_booking):
        updated_data = get_updated_booking_data()
        response = auth_booking_endpoints.update_booking(created_booking, updated_data)
        assert response.status_code == 200
        data = response.json()
        assert data["firstname"] == updated_data["firstname"]
        assert data["lastname"] == updated_data["lastname"]
        assert data["totalprice"] == updated_data["totalprice"]
    
    @allure.title("TC-5: delete booking")
    @allure.description("delete created booking")
    @allure.tag("api", "booking", "delete", "valid")
    def test_delete_booking(self, auth_booking_endpoints, booking_endpoints, created_booking):
        response = auth_booking_endpoints.delete_booking(created_booking)
        assert response.status_code == 201
        
        get_response = booking_endpoints.get_booking_by_id(created_booking)
        assert get_response.status_code == 404

    @allure.title("TC-6: get unreal booking")
    @allure.description("delete created booking")
    @allure.tag("api", "booking", "delete", "negative")
    def test_get_invalid_booking_by_id(self, auth_booking_endpoints):
        response = auth_booking_endpoints.get_booking_by_id("s07gfd239m87")
        assert response.status_code == 404

    @allure.title("TC-7: create booking with empty fills")
    @allure.description("delete created booking")
    @allure.tag("api", "booking", "post", "negative")
    @pytest.mark.parametrize(
        "firstname, lastname, checkin, checkout", 
        [
            pytest.param("Test first name", "Test last name", "2030-10-15", "", id="empty checkout"),
            pytest.param("Test first name", "Test last name", "", "2030-10-20", id="empty checkin"),
            pytest.param("Test first name", "", "2030-10-15", "2030-10-20", id="empty lastname"),
            pytest.param("", "Test last name", "2030-10-15", "2030-10-20", id="empty firstname")
        ]
    )
    def test_create_booking_with_diff_params(self, auth_booking_endpoints, firstname, lastname, checkin, checkout):
        responce = auth_booking_endpoints.create_booking(
            {
                "firstname": firstname,
                "lastname": lastname,
                "totalprice": 200,
                "depositpaid": False,
                "bookingdates": {
                    "checkin": checkin,
                    "checkout": checkout
                },
                "additionalneeds": "Dinner"
            }
        )
        assert responce.status_code == 200

    @allure.title("TC-8: create booking with negative price")
    @allure.description("create new booking with negative price")
    @allure.tag("api", "booking", "post", "negative")
    @pytest.mark.xfail(reason="restful have no price check")
    def test_create_boocking_negative_price(self, auth_booking_endpoints, test_booking_negative_price, ):
        response = auth_booking_endpoints.create_booking(test_booking_negative_price)
        assert response.status_code == 400

    @allure.title("TC-9: double delete")
    @allure.description("delete already deleted booking")
    @allure.tag("api", "booking", "delete")
    def test_delete_deleted_booking(self, auth_booking_endpoints, test_booking_data, booking_endpoints):
        response = booking_endpoints.create_booking(test_booking_data)
        assert response.status_code == 200
        data = response.json()
        booking_id = data["bookingid"]

        delete_response_1 = auth_booking_endpoints.delete_booking(booking_id)
        assert delete_response_1.status_code == 201

        delete_response_2 = auth_booking_endpoints.delete_booking(booking_id)
        assert delete_response_2.status_code == 405

        get_response = booking_endpoints.get_booking_by_id(booking_id)
        assert get_response.status_code == 404
