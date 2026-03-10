import requests
import json
import logging
from typing import Dict, Any, Optional, Union
from requests.exceptions import RequestException

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class APIClient:
    """
    A reusable API client for making HTTP requests with built-in features:
    - Support for all HTTP methods (GET, POST, PUT, PATCH, DELETE)
    - Automatic header management
    - Authentication support (Bearer token, Basic Auth, API Key)
    - Request/Response logging
    - Error handling with detailed messages
    - Response validation
    """

    def __init__(self, base_url: str = "", timeout: int = 30, verify_ssl: bool = True):
        """
        Initialize the API client
        
        Args:
            base_url: Base URL for all API requests
            timeout: Request timeout in seconds (default: 30)
            verify_ssl: Whether to verify SSL certificates (default: True)
        """
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.verify_ssl = verify_ssl
        self.session = requests.Session()
        self.default_headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.session.headers.update(self.default_headers)
        logger.info(f"API Client initialized with base URL: {self.base_url}")

    def set_base_url(self, base_url: str):
        """Update the base URL"""
        self.base_url = base_url.rstrip('/')
        logger.info(f"Base URL updated to: {self.base_url}")

    def set_header(self, key: str, value: str):
        """Set a custom header for all requests"""
        self.session.headers[key] = value
        logger.debug(f"Header set: {key} = {value}")

    def set_headers(self, headers: Dict[str, str]):
        """Set multiple headers at once"""
        self.session.headers.update(headers)
        logger.debug(f"Headers updated: {headers}")

    def remove_header(self, key: str):
        """Remove a header"""
        if key in self.session.headers:
            del self.session.headers[key]
            logger.debug(f"Header removed: {key}")

    def set_bearer_token(self, token: str):
        """Set Bearer token for authentication"""
        self.session.headers['Authorization'] = f'Bearer {token}'
        logger.info("Bearer token set for authentication")

    def set_api_key(self, api_key: str, header_name: str = 'X-API-Key'):
        """Set API key for authentication"""
        self.session.headers[header_name] = api_key
        logger.info(f"API key set in header: {header_name}")

    def set_basic_auth(self, username: str, password: str):
        """Set Basic authentication"""
        from requests.auth import HTTPBasicAuth
        self.session.auth = HTTPBasicAuth(username, password)
        logger.info("Basic authentication configured")

    def _build_url(self, endpoint: str) -> str:
        """Build complete URL from base URL and endpoint"""
        endpoint = endpoint.lstrip('/')
        if self.base_url:
            return f"{self.base_url}/{endpoint}"
        return endpoint

    def _log_request(self, method: str, url: str, **kwargs):
        """Log request details"""
        logger.info(f"\n{'='*80}")
        logger.info(f"REQUEST: {method.upper()} {url}")
        if 'headers' in kwargs and kwargs['headers']:
            logger.info(f"Headers: {json.dumps(dict(kwargs['headers']), indent=2)}")
        if 'params' in kwargs and kwargs['params']:
            logger.info(f"Params: {json.dumps(kwargs['params'], indent=2)}")
        if 'json' in kwargs and kwargs['json']:
            logger.info(f"Body: {json.dumps(kwargs['json'], indent=2)}")
        elif 'data' in kwargs and kwargs['data']:
            logger.info(f"Data: {kwargs['data']}")

    def _log_response(self, response: requests.Response):
        """Log response details"""
        logger.info(f"\nRESPONSE: {response.status_code} {response.reason}")
        logger.info(f"Headers: {json.dumps(dict(response.headers), indent=2)}")
        try:
            if response.text:
                logger.info(f"Body: {json.dumps(response.json(), indent=2)}")
        except json.JSONDecodeError:
            logger.info(f"Body (text): {response.text[:500]}")
        logger.info(f"{'='*80}\n")

    def _make_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict] = None,
        data: Optional[Union[Dict, str]] = None,
        json_data: Optional[Dict] = None,
        headers: Optional[Dict] = None,
        auth: Optional[tuple] = None,
        files: Optional[Dict] = None,
        timeout: Optional[int] = None,
        allow_redirects: bool = True,
        log: bool = True
    ) -> requests.Response:
        """
        Make an HTTP request
        
        Args:
            method: HTTP method (GET, POST, PUT, PATCH, DELETE)
            endpoint: API endpoint (will be appended to base_url)
            params: URL parameters
            data: Form data or raw body
            json_data: JSON data to send in request body
            headers: Additional headers for this request
            auth: Authentication tuple (username, password)
            files: Files to upload
            timeout: Request timeout (overrides default)
            allow_redirects: Whether to follow redirects
            log: Whether to log request/response details
            
        Returns:
            requests.Response object
        """
        url = self._build_url(endpoint)
        timeout = timeout or self.timeout

        # Merge headers
        request_headers = self.session.headers.copy()
        if headers:
            request_headers.update(headers)

        # Remove Content-Type for file uploads
        if files and 'Content-Type' in request_headers:
            del request_headers['Content-Type']

        kwargs = {
            'params': params,
            'data': data,
            'json': json_data,
            'headers': request_headers,
            'auth': auth or self.session.auth,
            'files': files,
            'timeout': timeout,
            'allow_redirects': allow_redirects,
            'verify': self.verify_ssl
        }

        # Remove None values
        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        try:
            if log:
                self._log_request(method, url, **kwargs)
            
            response = self.session.request(method, url, **kwargs)
            
            if log:
                self._log_response(response)
            
            return response

        except RequestException as e:
            logger.error(f"Request failed: {str(e)}")
            raise

    def get(self, endpoint: str, params: Optional[Dict] = None, **kwargs) -> requests.Response:
        """Make a GET request"""
        return self._make_request('GET', endpoint, params=params, **kwargs)

    def post(self, endpoint: str, json_data: Optional[Dict] = None, data: Optional[Union[Dict, str]] = None, **kwargs) -> requests.Response:
        """Make a POST request"""
        return self._make_request('POST', endpoint, json_data=json_data, data=data, **kwargs)

    def put(self, endpoint: str, json_data: Optional[Dict] = None, data: Optional[Union[Dict, str]] = None, **kwargs) -> requests.Response:
        """Make a PUT request"""
        return self._make_request('PUT', endpoint, json_data=json_data, data=data, **kwargs)

    def patch(self, endpoint: str, json_data: Optional[Dict] = None, data: Optional[Union[Dict, str]] = None, **kwargs) -> requests.Response:
        """Make a PATCH request"""
        return self._make_request('PATCH', endpoint, json_data=json_data, data=data, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        """Make a DELETE request"""
        return self._make_request('DELETE', endpoint, **kwargs)

    def get_json(self, endpoint: str, **kwargs) -> Dict:
        """Make a GET request and return JSON response"""
        response = self.get(endpoint, **kwargs)
        return response.json()

    def post_json(self, endpoint: str, json_data: Optional[Dict] = None, **kwargs) -> Dict:
        """Make a POST request and return JSON response"""
        response = self.post(endpoint, json_data=json_data, **kwargs)
        return response.json()

    def validate_status_code(self, response: requests.Response, expected_code: int):
        """Validate response status code"""
        assert response.status_code == expected_code, \
            f"Expected status code {expected_code}, got {response.status_code}. Response: {response.text}"
        logger.info(f"✓ Status code validation passed: {expected_code}")

    def validate_response_time(self, response: requests.Response, max_time: float):
        """Validate response time is within acceptable limit"""
        response_time = response.elapsed.total_seconds()
        assert response_time <= max_time, \
            f"Response time {response_time}s exceeded maximum {max_time}s"
        logger.info(f"✓ Response time validation passed: {response_time:.3f}s <= {max_time}s")

    def validate_json_schema(self, response: requests.Response, schema: Dict):
        """Validate response JSON against a schema"""
        from jsonschema import validate, ValidationError
        try:
            validate(instance=response.json(), schema=schema)
            logger.info("✓ JSON schema validation passed")
        except ValidationError as e:
            raise AssertionError(f"JSON schema validation failed: {e.message}")

    def validate_response_contains(self, response: requests.Response, key: str, value: Any = None):
        """Validate response JSON contains a key and optionally validate its value"""
        json_response = response.json()
        
        # Handle nested keys with dot notation (e.g., "data.id")
        keys = key.split('.')
        current = json_response
        
        for k in keys:
            assert k in current, f"Key '{k}' not found in response. Available keys: {list(current.keys())}"
            current = current[k]
        
        if value is not None:
            assert current == value, f"Expected '{key}' to be '{value}', got '{current}'"
            logger.info(f"✓ Response contains '{key}' = '{value}'")
        else:
            logger.info(f"✓ Response contains key '{key}'")

    def close(self):
        """Close the session"""
        self.session.close()
        logger.info("API Client session closed")
