"""
API Fixtures for pytest
Provides reusable API client instances for testing
"""
from utilities.api_client import APIClient


class API:
    """Container for API client instances"""

    def __init__(self, base_url: str = ""):
        self.client = APIClient(base_url=base_url)
        self.base_url = base_url

    def set_base_url(self, base_url: str):
        """Update base URL"""
        self.base_url = base_url
        self.client.set_base_url(base_url)

    def set_auth_token(self, token: str):
        """Set Bearer authentication token"""
        self.client.set_bearer_token(token)

    def set_api_key(self, api_key: str, header_name: str = 'X-API-Key'):
        """Set API key authentication"""
        self.client.set_api_key(api_key, header_name)

    def close(self):
        """Close the API client session"""  
        self.client.close()
