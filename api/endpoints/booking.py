from api.client import APIClient

class BookingEndpoints:
    
    def __init__(self, token=None):
        self.client = APIClient(token=token)
    
    def get_all_bookings(self):
        return self.client.get("/booking")
    
    def get_booking_by_id(self, booking_id):
        return self.client.get(f"/booking/{booking_id}")
    
    def create_booking(self, booking_data):
        return self.client.post("/booking", data=booking_data)
    
    def update_booking(self, booking_id, booking_data):
        return self.client.put(f"/booking/{booking_id}", data=booking_data)
    
    def partial_update_booking(self, booking_id, booking_data):
        return self.client.patch(f"/booking/{booking_id}", data=booking_data)
    
    def delete_booking(self, booking_id):
        return self.client.delete(f"/booking/{booking_id}")