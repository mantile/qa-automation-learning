from api.client import APIClient

class AuthEndpoints:
    
    def __init__(self):
        self.client = APIClient()
    
    def get_token(self, username="admin", password="password123"):
        """Получение токена для авторизации"""
        data = {
            "username": username,
            "password": password
        }
        response = self.client.post("/auth", data=data)
        if response.status_code == 200:
            return response.json().get("token")
        return None