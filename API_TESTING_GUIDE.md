# API Testing Framework - User Guide

## Overview
The TAF framework now includes comprehensive API testing capabilities alongside UI testing. The API testing module is built on Python's `requests` library with additional utilities for validation, authentication, and data management.

## Features
- ✅ Support for all HTTP methods (GET, POST, PUT, PATCH, DELETE)
- ✅ Multiple authentication methods (Bearer Token, API Key, Basic Auth)
- ✅ Automatic request/response logging
- ✅ Built-in response validation (status code, response time, JSON schema)
- ✅ Dynamic test data generation
- ✅ Configurable base URL and timeout settings
- ✅ SSL verification control
- ✅ Session management with persistent headers

## Quick Start

### 1. Configuration
Edit `configurations/config.ini`:
```ini
[api]
base_url = https://jsonplaceholder.typicode.com
timeout = 30
verify_ssl = true
```

### 2. Basic API Test
```python
import pytest

class TestAPI:
    @pytest.mark.api
    def test_get_users(self, api):
        # Make GET request
        response = api.client.get('/users')
        
        # Validate response
        api.client.validate_status_code(response, 200)
        api.client.validate_response_time(response, 5.0)
        
        # Work with response data
        users = response.json()
        assert len(users) > 0
```

### 3. Run API Tests
```bash
# Run all API tests
python -m pytest test_api_examples.py -m api

# Run API sanity tests only
python -m pytest test_api_examples.py -m "api and sanity"

# Run specific test
python -m pytest test_api_examples.py -k "test_get_users"
```

Or use the batch file:
```bash
run_jobs\run_api_tests.cmd
```

## Core Components

### 1. API Client (`utilities/api_client.py`)
The main class for making API requests with built-in validation.

#### Basic Usage
```python
from utilities.api_client import APIClient

# Initialize client
client = APIClient(base_url="https://api.example.com", timeout=30)

# Make requests
response = client.get('/endpoint')
response = client.post('/endpoint', json_data={'key': 'value'})
response = client.put('/endpoint/{id}', json_data={'key': 'updated'})
response = client.patch('/endpoint/{id}', json_data={'key': 'patched'})
response = client.delete('/endpoint/{id}')
```

#### Authentication
```python
# Bearer Token
client.set_bearer_token("your-token-here")

# API Key
client.set_api_key("your-api-key", header_name='X-API-Key')

# Basic Auth
client.set_basic_auth("username", "password")

# Custom Headers
client.set_header("X-Custom-Header", "value")
client.set_headers({
    "X-Header-1": "value1",
    "X-Header-2": "value2"
})
```

#### Response Validation
```python
# Status code
client.validate_status_code(response, 200)

# Response time (in seconds)
client.validate_response_time(response, 2.0)

# Check key exists in response
client.validate_response_contains(response, 'id')

# Check key-value pair
client.validate_response_contains(response, 'status', 'active')

# Nested keys (dot notation)
client.validate_response_contains(response, 'data.user.email')

# JSON Schema validation
schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"}
    },
    "required": ["id", "name"]
}
client.validate_json_schema(response, schema)
```

### 2. API Utilities (`utilities/api_utils.py`)
Helper functions for common API testing tasks.

#### APIUtils Class
```python
from utilities.api_utils import APIUtils

# Generate random data
random_string = APIUtils.generate_random_string(10)
random_email = APIUtils.generate_random_email()

# Timestamps
current_time = APIUtils.generate_timestamp()
future_date = APIUtils.generate_future_date(days=30)
past_date = APIUtils.generate_past_date(days=7)

# Extract nested values
value = APIUtils.extract_value_from_json(
    json_data={'user': {'profile': {'email': 'test@test.com'}}},
    key_path='user.profile.email'
)
# Returns: 'test@test.com'

# Validate required fields
is_valid, missing = APIUtils.validate_required_fields(
    json_data={'id': 1, 'name': 'John'},
    required_fields=['id', 'name', 'email']
)
# Returns: (False, ['email'])

# Save response to file
APIUtils.save_response_to_file(response.json(), 'user_response.json')

# Mask sensitive data for logging
masked = APIUtils.mask_sensitive_data(
    data={'username': 'john', 'password': 'secret123'},
    sensitive_keys=['password', 'token']
)
# Returns: {'username': 'john', 'password': '***MASKED***'}
```

#### APITestData Class
```python
from utilities.api_utils import APITestData

# Generate test payloads
user = APITestData.user_payload(
    name="John Doe",
    email="john@test.com",
    age=30
)

product = APITestData.product_payload(
    name="Laptop",
    price=999.99,
    category="Electronics"
)

order = APITestData.order_payload(
    user_id=123,
    product_ids=[1, 2, 3],
    status="pending"
)
```

### 3. API Fixtures (`fixtures/api_fixtures.py`)
Pytest fixtures for API testing.

#### Usage in Tests
```python
def test_with_api_fixture(api):
    # api fixture automatically:
    # - Reads configuration from config.ini
    # - Initializes API client with base URL
    # - Cleans up after test completes
    
    response = api.client.get('/users')
    api.client.validate_status_code(response, 200)
```

## Test Examples

### Example 1: Basic CRUD Operations
```python
@pytest.mark.api
def test_crud_workflow(api):
    # CREATE
    new_user = {"name": "John", "email": "john@test.com"}
    create_resp = api.client.post('/users', json_data=new_user)
    api.client.validate_status_code(create_resp, 201)
    user_id = create_resp.json()['id']
    
    # READ
    get_resp = api.client.get(f'/users/{user_id}')
    api.client.validate_status_code(get_resp, 200)
    
    # UPDATE
    update_data = {"name": "John Updated"}
    put_resp = api.client.put(f'/users/{user_id}', json_data=update_data)
    api.client.validate_status_code(put_resp, 200)
    
    # DELETE
    delete_resp = api.client.delete(f'/users/{user_id}')
    api.client.validate_status_code(delete_resp, 200)
```

### Example 2: Query Parameters
```python
@pytest.mark.api
def test_with_query_params(api):
    params = {
        'userId': 1,
        'status': 'active',
        'limit': 10
    }
    response = api.client.get('/posts', params=params)
    api.client.validate_status_code(response, 200)
    
    posts = response.json()
    for post in posts:
        assert post['userId'] == 1
```

### Example 3: File Upload
```python
@pytest.mark.api
def test_file_upload(api):
    files = {
        'file': open('test_file.txt', 'rb'),
        'document': open('test_doc.pdf', 'rb')
    }
    
    response = api.client.post('/upload', files=files)
    api.client.validate_status_code(response, 200)
```

### Example 4: Data-Driven Testing
```python
@pytest.mark.api
@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
def test_multiple_users(api, user_id):
    response = api.client.get(f'/users/{user_id}')
    api.client.validate_status_code(response, 200)
    
    user = response.json()
    assert user['id'] == user_id
```

### Example 5: Performance Testing
```python
@pytest.mark.api
@pytest.mark.performance
def test_response_time(api):
    import time
    
    start_time = time.time()
    response = api.client.get('/users')
    end_time = time.time()
    
    api.client.validate_status_code(response, 200)
    api.client.validate_response_time(response, max_time=2.0)
    
    print(f"Response time: {end_time - start_time:.3f}s")
```

### Example 6: Chained Requests
```python
@pytest.mark.api
def test_chained_requests(api):
    # Step 1: Get all users
    users_resp = api.client.get('/users')
    users = users_resp.json()
    first_user_id = users[0]['id']
    
    # Step 2: Get posts for first user
    posts_resp = api.client.get(f'/users/{first_user_id}/posts')
    posts = posts_resp.json()
    first_post_id = posts[0]['id']
    
    # Step 3: Get comments for first post
    comments_resp = api.client.get(f'/posts/{first_post_id}/comments')
    api.client.validate_status_code(comments_resp, 200)
```

## Configuration Options

### API Settings in config.ini
```ini
[api]
# Base URL for all API requests
base_url = https://api.example.com

# Request timeout in seconds
timeout = 30

# SSL certificate verification (true/false)
verify_ssl = true
```

### Pytest Markers
Add to `pytest.ini`:
```ini
[pytest]
markers=
    api: API tests
    sanity: Sanity tests
    regression: Regression tests
    performance: Performance tests
```

## Best Practices

### 1. Use Fixtures for Setup/Teardown
```python
@pytest.fixture
def test_user(api):
    # Setup: Create test user
    user = api.client.post('/users', json_data={'name': 'Test User'})
    user_id = user.json()['id']
    
    yield user_id
    
    # Teardown: Delete test user
    api.client.delete(f'/users/{user_id}')

def test_with_test_user(api, test_user):
    response = api.client.get(f'/users/{test_user}')
    api.client.validate_status_code(response, 200)
```

### 2. Organize Tests by Resource
```
test_cases/
├── test_users_api.py       # User-related API tests
├── test_posts_api.py       # Post-related API tests
├── test_comments_api.py    # Comment-related API tests
└── test_auth_api.py        # Authentication tests
```

### 3. Use Descriptive Test Names
```python
def test_get_user_returns_200_for_valid_id(api):
    pass

def test_create_user_fails_with_400_for_invalid_email(api):
    pass

def test_delete_user_returns_404_for_nonexistent_id(api):
    pass
```

### 4. Validate Both Success and Error Cases
```python
@pytest.mark.api
def test_user_not_found(api):
    response = api.client.get('/users/99999', log=False)
    api.client.validate_status_code(response, 404)
    
    error = response.json()
    assert 'error' in error or 'message' in error
```

### 5. Use Environment-Specific Configuration
```ini
[api_dev]
base_url = https://dev-api.example.com

[api_staging]
base_url = https://staging-api.example.com

[api_prod]
base_url = https://api.example.com
```

## Troubleshooting

### Issue: SSL Certificate Errors
**Solution**: Set `verify_ssl = false` in config.ini (not recommended for production)

### Issue: Timeout Errors
**Solution**: Increase timeout value in config.ini or per request:
```python
response = api.client.get('/slow-endpoint', timeout=60)
```

### Issue: Authentication Failures
**Solution**: Verify token/credentials and check header format:
```python
# Debug headers
print(api.client.session.headers)
```

### Issue: Response Parsing Errors
**Solution**: Check if response is valid JSON:
```python
try:
    data = response.json()
except json.JSONDecodeError:
    print(f"Response text: {response.text}")
```

## Advanced Usage

### Custom API Client Extension
```python
from utilities.api_client import APIClient

class CustomAPIClient(APIClient):
    def __init__(self, base_url):
        super().__init__(base_url)
        self.set_custom_behavior()
    
    def set_custom_behavior(self):
        # Add custom headers
        self.set_header('X-Custom-App', 'TAF')
    
    def custom_endpoint(self, resource_id):
        """Custom method for specific endpoint"""
        return self.get(f'/custom/{resource_id}/details')
```

### Dynamic Base URL
```python
def test_with_different_env(api):
    # Change base URL dynamically
    api.set_base_url("https://staging-api.example.com")
    
    response = api.client.get('/users')
    api.client.validate_status_code(response, 200)
```

## Summary
The API testing framework provides a complete solution for testing REST APIs with:
- Simple, intuitive interface
- Comprehensive validation methods
- Built-in logging and debugging
- Easy integration with existing pytest infrastructure
- Support for various authentication methods
- Flexible configuration options

For more examples, see `test_cases/test_api_examples.py`
