def get_booking_data():
    return {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-01-10"
        },
        "additionalneeds": "Breakfast"
    }

def get_updated_booking_data():
    return {
        "firstname": "Jane",
        "lastname": "Smith",
        "totalprice": 200,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2025-02-01",
            "checkout": "2025-02-15"
        },
        "additionalneeds": "Dinner"
    }

def get_booking_negative_price():
    return {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": -150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-01-10"
        },
        "additionalneeds": "Breakfast"
    }