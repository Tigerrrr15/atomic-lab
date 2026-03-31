import requests

def validate_user(user_data):
    if not user_data.get('email'):
        print("Email is required")
        return False
    if not user_data.get('age') or user_data['age'] < 18:
        print("User must be 18+")
        return False
    return True

def process_user(user_data):
    print(f"Processing user: {user_data.get('name', 'Unknown')}")
    response = requests.post('https://api.example.com/users', json=user_data)
    print(f"API response status: {response.status_code}")
    return response


def main():
    user = {"name": "John", "email": "john@example.com", "age": 25}
    if validate_user(user):
        result = process_user(user)
        print("User processed successfully")
    else:
        print("Validation failed")

if __name__ == "__main__":
    main()