"""
Example API Tests using the TAF API Client
Demonstrates various API testing scenarios with JSONPlaceholder (fake REST API)
"""
import pytest
from utilities.api_utils import APIUtils, APITestData


class TestAPIExamples:
    """Example API tests demonstrating framework capabilities"""

    @pytest.mark.api
    @pytest.mark.sanity
    def test_get_all_users(self, api):
        """Test GET request to retrieve all users"""
        # Make GET request
        response = api.client.get('/users')
        
        # Validate response
        api.client.validate_status_code(response, 200)
        api.client.validate_response_time(response, 5.0)
        
        # Validate response data
        users = response.json()
        assert len(users) > 0, "No users found in response"
        assert isinstance(users, list), "Response should be a list"
        
        # Validate first user has required fields
        first_user = users[0]
        required_fields = ['id', 'name', 'email', 'username']
        is_valid, missing = APIUtils.validate_required_fields(first_user, required_fields)
        assert is_valid, f"Missing required fields: {missing}"
        
        print(f"\n✓ Retrieved {len(users)} users successfully")

    @pytest.mark.api
    @pytest.mark.sanity
    def test_get_single_user(self, api):
        """Test GET request to retrieve a specific user"""
        user_id = 1
        response = api.client.get(f'/users/{user_id}')
        
        # Validate response
        api.client.validate_status_code(response, 200)
        api.client.validate_response_contains(response, 'id', user_id)
        api.client.validate_response_contains(response, 'name')
        api.client.validate_response_contains(response, 'email')
        
        user = response.json()
        print(f"\n✓ User retrieved: {user['name']} ({user['email']})")

    @pytest.mark.api
    @pytest.mark.regression
    def test_get_user_posts(self, api):
        """Test GET request with query parameters"""
        user_id = 1
        response = api.client.get('/posts', params={'userId': user_id})
        
        api.client.validate_status_code(response, 200)
        
        posts = response.json()
        assert len(posts) > 0, "No posts found for user"
        
        # Verify all posts belong to the specified user
        for post in posts:
            assert post['userId'] == user_id, f"Post {post['id']} doesn't belong to user {user_id}"
        
        print(f"\n✓ User {user_id} has {len(posts)} posts")

    @pytest.mark.api
    @pytest.mark.regression
    def test_create_user(self, api):
        """Test POST request to create a new resource"""
        # Generate test payload
        new_user = APITestData.user_payload(
            name="John Doe",
            email="john.doe@test.com"
        )
        
        # Create user
        response = api.client.post('/users', json_data=new_user)
        
        # Validate response
        api.client.validate_status_code(response, 201)  # 201 Created
        
        created_user = response.json()
        assert created_user['name'] == new_user['name']
        assert created_user['email'] == new_user['email']
        assert 'id' in created_user, "Created user should have an ID"
        
        print(f"\n✓ User created with ID: {created_user.get('id')}")

    @pytest.mark.api
    @pytest.mark.regression
    def test_update_user(self, api):
        """Test PUT request to update a resource"""
        user_id = 1
        
        # Updated data
        updated_data = {
            "name": "Updated Name",
            "email": "updated.email@test.com"
        }
        
        # Update user
        response = api.client.put(f'/users/{user_id}', json_data=updated_data)
        
        # Validate response
        api.client.validate_status_code(response, 200)
        
        updated_user = response.json()
        assert updated_user['name'] == updated_data['name']
        assert updated_user['email'] == updated_data['email']
        
        print(f"\n✓ User {user_id} updated successfully")

    @pytest.mark.api
    @pytest.mark.regression
    def test_patch_user(self, api):
        """Test PATCH request to partially update a resource"""
        user_id = 1
        
        # Partial update data
        patch_data = {"name": "Patched Name"}
        
        # Patch user
        response = api.client.patch(f'/users/{user_id}', json_data=patch_data)
        
        # Validate response
        api.client.validate_status_code(response, 200)
        
        patched_user = response.json()
        assert patched_user['name'] == patch_data['name']
        
        print(f"\n✓ User {user_id} patched successfully")

    @pytest.mark.api
    @pytest.mark.regression
    def test_delete_user(self, api):
        """Test DELETE request to remove a resource"""
        user_id = 1
        
        # Delete user
        response = api.client.delete(f'/users/{user_id}')
        
        # Validate response
        api.client.validate_status_code(response, 200)
        
        print(f"\n✓ User {user_id} deleted successfully")

    @pytest.mark.api
    @pytest.mark.regression
    def test_invalid_endpoint(self, api):
        """Test handling of invalid endpoint (404)"""
        response = api.client.get('/invalid-endpoint', log=False)
        
        api.client.validate_status_code(response, 404)
        
        print("\n✓ 404 error handled correctly")

    @pytest.mark.api
    @pytest.mark.regression
    def test_json_schema_validation(self, api):
        """Test response JSON schema validation"""
        # Define expected schema
        user_schema = {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "username": {"type": "string"},
                "email": {"type": "string", "format": "email"}
            },
            "required": ["id", "name", "email"]
        }
        
        response = api.client.get('/users/1')
        api.client.validate_status_code(response, 200)
        api.client.validate_json_schema(response, user_schema)
        
        print("\n✓ JSON schema validation passed")

    @pytest.mark.api
    @pytest.mark.regression
    def test_nested_resources(self, api):
        """Test retrieving nested resources"""
        post_id = 1
        
        # Get comments for a specific post
        response = api.client.get(f'/posts/{post_id}/comments')
        
        api.client.validate_status_code(response, 200)
        
        comments = response.json()
        assert len(comments) > 0, "No comments found for post"
        
        # Validate nested data extraction
        first_comment_email = APIUtils.extract_value_from_json(comments[0], 'email')
        assert first_comment_email is not None, "Email not found in comment"
        
        print(f"\n✓ Post {post_id} has {len(comments)} comments")

    @pytest.mark.api
    @pytest.mark.regression
    def test_multiple_requests_workflow(self, api):
        """Test a complete workflow with multiple API calls"""
        # Step 1: Create a post
        new_post = {
            "title": "Test Post",
            "body": "This is a test post",
            "userId": 1
        }
        
        create_response = api.client.post('/posts', json_data=new_post)
        api.client.validate_status_code(create_response, 201)
        
        created_post = create_response.json()
        post_id = created_post.get('id', 101)  # JSONPlaceholder returns mock ID
        
        # Step 2: Retrieve the created post
        get_response = api.client.get(f'/posts/{post_id}')
        api.client.validate_status_code(get_response, 200)
        
        # Step 3: Update the post
        updated_data = {"title": "Updated Test Post"}
        update_response = api.client.patch(f'/posts/{post_id}', json_data=updated_data)
        api.client.validate_status_code(update_response, 200)
        
        # Step 4: Delete the post
        delete_response = api.client.delete(f'/posts/{post_id}')
        api.client.validate_status_code(delete_response, 200)
        
        print(f"\n✓ Complete workflow executed: Create → Read → Update → Delete")

    @pytest.mark.api
    @pytest.mark.regression
    def test_data_driven_api_calls(self, api):
        """Test data-driven API testing"""
        user_ids = [1, 2, 3, 4, 5]
        
        for user_id in user_ids:
            response = api.client.get(f'/users/{user_id}', log=False)
            api.client.validate_status_code(response, 200)
            
            user = response.json()
            assert user['id'] == user_id
        
        print(f"\n✓ Successfully validated {len(user_ids)} users")

    @pytest.mark.api
    @pytest.mark.performance
    def test_response_time_validation(self, api):
        """Test API response time is within acceptable limits"""
        max_response_time = 3.0  # seconds
        
        response = api.client.get('/users')
        api.client.validate_status_code(response, 200)
        api.client.validate_response_time(response, max_response_time)
        
        actual_time = response.elapsed.total_seconds()
        print(f"\n✓ Response time: {actual_time:.3f}s (limit: {max_response_time}s)")


# Example of how to use with authentication
class TestAPIWithAuthentication:
    """Examples demonstrating API authentication"""

    @pytest.mark.api
    @pytest.mark.skip(reason="Requires actual API with authentication")
    def test_bearer_token_auth(self, api):
        """Example: Test with Bearer token authentication"""
        # Set authentication token
        api.set_auth_token("your-bearer-token-here")
        
        # Make authenticated request
        response = api.client.get('/protected-endpoint')
        api.client.validate_status_code(response, 200)

    @pytest.mark.api
    @pytest.mark.skip(reason="Requires actual API with authentication")
    def test_api_key_auth(self, api):
        """Example: Test with API key authentication"""
        # Set API key
        api.set_api_key("your-api-key-here", header_name='X-API-Key')
        
        # Make authenticated request
        response = api.client.get('/protected-endpoint')
        api.client.validate_status_code(response, 200)
