"""
API Testing Utilities
Common helper functions for API testing
"""
import json
import random
import string
from typing import Dict, Any, List
from datetime import datetime, timedelta


class APIUtils:
    """Utility functions for API testing"""

    @staticmethod
    def generate_random_string(length: int = 10) -> str:
        """Generate a random string of specified length"""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    @staticmethod
    def generate_random_email() -> str:
        """Generate a random email address"""
        username = APIUtils.generate_random_string(8).lower()
        domain = random.choice(['test.com', 'example.com', 'demo.com'])
        return f"{username}@{domain}"

    @staticmethod
    def generate_timestamp() -> str:
        """Generate current timestamp in ISO format"""
        return datetime.now().isoformat()

    @staticmethod
    def generate_future_date(days: int = 30) -> str:
        """Generate future date in ISO format"""
        future_date = datetime.now() + timedelta(days=days)
        return future_date.isoformat()

    @staticmethod
    def generate_past_date(days: int = 30) -> str:
        """Generate past date in ISO format"""
        past_date = datetime.now() - timedelta(days=days)
        return past_date.isoformat()

    @staticmethod
    def compare_json_objects(obj1: Dict, obj2: Dict, ignore_keys: List[str] = None) -> bool:
        """
        Compare two JSON objects, optionally ignoring specific keys
        
        Args:
            obj1: First JSON object
            obj2: Second JSON object
            ignore_keys: List of keys to ignore in comparison
            
        Returns:
            True if objects match, False otherwise
        """
        if ignore_keys:
            obj1 = {k: v for k, v in obj1.items() if k not in ignore_keys}
            obj2 = {k: v for k, v in obj2.items() if k not in ignore_keys}
        
        return obj1 == obj2

    @staticmethod
    def extract_value_from_json(json_data: Dict, key_path: str) -> Any:
        """
        Extract value from nested JSON using dot notation
        
        Args:
            json_data: JSON object
            key_path: Path to the key (e.g., "data.user.id")
            
        Returns:
            Value at the specified path
        """
        keys = key_path.split('.')
        current = json_data
        
        for key in keys:
            if isinstance(current, dict):
                current = current.get(key)
            elif isinstance(current, list) and key.isdigit():
                current = current[int(key)]
            else:
                return None
        
        return current

    @staticmethod
    def validate_required_fields(json_data: Dict, required_fields: List[str]) -> tuple:
        """
        Validate that all required fields are present in JSON
        
        Args:
            json_data: JSON object to validate
            required_fields: List of required field names
            
        Returns:
            Tuple of (is_valid, missing_fields)
        """
        missing_fields = []
        
        for field in required_fields:
            if APIUtils.extract_value_from_json(json_data, field) is None:
                missing_fields.append(field)
        
        return len(missing_fields) == 0, missing_fields

    @staticmethod
    def save_response_to_file(response_data: Dict, filename: str, directory: str = "reports"):
        """Save API response to a JSON file"""
        import os
        
        # Create directory if it doesn't exist
        os.makedirs(directory, exist_ok=True)
        
        filepath = os.path.join(directory, filename)
        with open(filepath, 'w') as f:
            json.dump(response_data, f, indent=2)
        
        print(f"Response saved to: {filepath}")
        return filepath

    @staticmethod
    def load_json_from_file(filepath: str) -> Dict:
        """Load JSON data from a file"""
        with open(filepath, 'r') as f:
            return json.load(f)

    @staticmethod
    def create_basic_json_schema(sample_data: Dict) -> Dict:
        """
        Create a basic JSON schema from sample data
        
        Args:
            sample_data: Sample JSON object
            
        Returns:
            Basic JSON schema
        """
        schema = {
            "type": "object",
            "properties": {},
            "required": []
        }
        
        for key, value in sample_data.items():
            if isinstance(value, str):
                schema["properties"][key] = {"type": "string"}
            elif isinstance(value, int):
                schema["properties"][key] = {"type": "integer"}
            elif isinstance(value, float):
                schema["properties"][key] = {"type": "number"}
            elif isinstance(value, bool):
                schema["properties"][key] = {"type": "boolean"}
            elif isinstance(value, list):
                schema["properties"][key] = {"type": "array"}
            elif isinstance(value, dict):
                schema["properties"][key] = {"type": "object"}
            
            schema["required"].append(key)
        
        return schema

    @staticmethod
    def print_json_pretty(data: Dict):
        """Print JSON data in a readable format"""
        print(json.dumps(data, indent=2, sort_keys=True))

    @staticmethod
    def mask_sensitive_data(data: Dict, sensitive_keys: List[str] = None) -> Dict:
        """
        Mask sensitive data in JSON for logging
        
        Args:
            data: JSON object
            sensitive_keys: List of keys containing sensitive data
            
        Returns:
            JSON object with masked sensitive values
        """
        if sensitive_keys is None:
            sensitive_keys = ['password', 'token', 'api_key', 'secret', 'authorization']
        
        masked_data = data.copy()
        
        def mask_recursive(obj):
            if isinstance(obj, dict):
                for key, value in obj.items():
                    if any(sensitive in key.lower() for sensitive in sensitive_keys):
                        obj[key] = "***MASKED***"
                    elif isinstance(value, (dict, list)):
                        mask_recursive(value)
            elif isinstance(obj, list):
                for item in obj:
                    if isinstance(item, (dict, list)):
                        mask_recursive(item)
        
        mask_recursive(masked_data)
        return masked_data


class APITestData:
    """Test data generators for API testing"""

    @staticmethod
    def user_payload(name: str = None, email: str = None, **kwargs) -> Dict:
        """Generate user payload with optional custom fields"""
        payload = {
            "name": name or f"Test User {APIUtils.generate_random_string(5)}",
            "email": email or APIUtils.generate_random_email(),
            "status": kwargs.get("status", "active")
        }
        payload.update(kwargs)
        return payload

    @staticmethod
    def product_payload(name: str = None, price: float = None, **kwargs) -> Dict:
        """Generate product payload with optional custom fields"""
        payload = {
            "name": name or f"Product {APIUtils.generate_random_string(5)}",
            "price": price or round(random.uniform(10.0, 1000.0), 2),
            "description": kwargs.get("description", "Test product description"),
            "inStock": kwargs.get("inStock", True)
        }
        payload.update(kwargs)
        return payload

    @staticmethod
    def order_payload(user_id: int = None, product_ids: List[int] = None, **kwargs) -> Dict:
        """Generate order payload with optional custom fields"""
        payload = {
            "userId": user_id or random.randint(1, 1000),
            "productIds": product_ids or [random.randint(1, 100) for _ in range(random.randint(1, 5))],
            "orderDate": APIUtils.generate_timestamp(),
            "status": kwargs.get("status", "pending")
        }
        payload.update(kwargs)
        return payload
