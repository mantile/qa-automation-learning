import pytest
from data.api.test_data import get_updated_booking_data

class TestBooking:
    
    @pytest.mark.api
    @pytest.mark.smoke
    def test_get_all_bookings(self, booking_endpoints):
        response = booking_endpoints.get_all_bookings()
        assert response.status_code == 200
        bookings = response.json()
        assert isinstance(bookings, list)
        assert len(bookings) > 0
    
    @pytest.mark.api
    @pytest.mark.smoke
    def test_create_booking(self, booking_endpoints, test_booking_data):
        response = booking_endpoints.create_booking(test_booking_data)
        assert response.status_code == 200
        data = response.json()
        assert "bookingid" in data
        assert data["booking"]["firstname"] == test_booking_data["firstname"]
        assert data["booking"]["lastname"] == test_booking_data["lastname"]
    
    @pytest.mark.api
    @pytest.mark.smoke
    def test_get_booking_by_id(self, booking_endpoints, created_booking):
        response = booking_endpoints.get_booking_by_id(created_booking)
        assert response.status_code == 200
        data = response.json()
        assert data["firstname"] is not None
        assert data["lastname"] is not None
    
    @pytest.mark.api
    @pytest.mark.smoke
    def test_update_booking(self, auth_booking_endpoints, created_booking):
        updated_data = get_updated_booking_data()
        response = auth_booking_endpoints.update_booking(created_booking, updated_data)
        assert response.status_code == 200
        data = response.json()
        assert data["firstname"] == updated_data["firstname"]
        assert data["lastname"] == updated_data["lastname"]
        assert data["totalprice"] == updated_data["totalprice"]
    
    @pytest.mark.api
    @pytest.mark.smoke
    def test_delete_booking(self, auth_booking_endpoints, booking_endpoints, created_booking):
        response = auth_booking_endpoints.delete_booking(created_booking)
        assert response.status_code == 201
        
        get_response = booking_endpoints.get_booking_by_id(created_booking)
        assert get_response.status_code == 404