import requests

class APIClient:
    
    BASE_URL = "https://restful-booker.herokuapp.com"
    
    def __init__(self, token=None):
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })
        
        if token:
            self.session.headers.update({
                "Cookie": f"token={token}"
            })
    
    def _request(
            self,
            method,
            endpoint,
            data=None,
            params=None
    ):
        url = f"{self.BASE_URL}{endpoint}"
        
        response = self.session.request(
            method=method,
            url=url,
            json=data,
            params=params
        )
        return response
    
    def get(self, endpoint, params=None):
        return self._request("GET", endpoint, params=params)
    
    def post(self, endpoint, data=None, params=None):
        return self._request("POST", endpoint, data=data, params=params)
    
    def put(self, endpoint, data=None, params=None):
        return self._request("PUT", endpoint, data=data, params=params)
    
    def patch(self, endpoint, data=None, params=None):
        return self._request("PATCH", endpoint, data=data, params=params)
    
    def delete(self, endpoint, params=None):
        return self._request("DELETE", endpoint, params=params)