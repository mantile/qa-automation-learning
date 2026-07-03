import pytest
from api.endpoints.auth import AuthEndpoints
from api.endpoints.booking import BookingEndpoints
from data.api.test_data import get_booking_data

@pytest.fixture
def auth_endpoints():
    return AuthEndpoints()

@pytest.fixture
def booking_endpoints():
    return BookingEndpoints()

@pytest.fixture
def auth_booking_endpoints(auth_endpoints):
    token = auth_endpoints.get_token()
    return BookingEndpoints(token=token)

@pytest.fixture
def test_booking_data():
    return get_booking_data()

@pytest.fixture
def created_booking(booking_endpoints, test_booking_data):
    response = booking_endpoints.create_booking(test_booking_data)
    assert response.status_code == 200
    booking_id = response.json().get("bookingid")
    yield booking_id