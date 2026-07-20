import pytest
import allure

@allure.epic("Restful-booker")
@allure.feature("Authorization")
@pytest.mark.restfulbooker
@pytest.mark.api
class TestAuth:
    
    @allure.title("TC-1: get token")
    @allure.description("get token with valid data")
    @allure.tag("api", "token", "get", "valid")
    def test_get_token_success(self, auth_endpoints):
        token = auth_endpoints.get_token()
        assert token is not None
        assert isinstance(token, str)
        assert len(token) > 0
    
    @allure.title("TC-2: get token with wrong pass")
    @allure.description("get token with out valid data by username only")
    @allure.tag("api", "token", "get")
    @pytest.mark.api
    @pytest.mark.restfulbooker
    def test_get_token_wrong_password(self, auth_endpoints):
        token = auth_endpoints.get_token(username="admin", password="wrong")
        assert token is None

    @allure.title("TC-3: get token with wrong username")
    @allure.description("get token with out valid data by password only")
    @allure.tag("api", "token", "get")
    @pytest.mark.api
    @pytest.mark.restfulbooker
    def test_get_token_wrong_password(self, auth_endpoints):
        token = auth_endpoints.get_token(username="wrong", password="password123")
        assert token is None