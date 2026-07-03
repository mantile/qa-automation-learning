import pytest

class TestAuth:
    
    @pytest.mark.api
    @pytest.mark.smoke
    def test_get_token_success(self, auth_endpoints):
        token = auth_endpoints.get_token()
        assert token is not None
        assert isinstance(token, str)
        assert len(token) > 0
    
    @pytest.mark.api
    @pytest.mark.smoke
    def test_get_token_wrong_password(self, auth_endpoints):
        token = auth_endpoints.get_token(username="admin", password="wrong")
        assert token is None