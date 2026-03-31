import requests
import logging  # ДОБАВЛЕНО: для обработки ошибок

# ИЗМЕНЕНО: переименованы переменные для ясности
def validate_user(user_info):  # было: user_data
    if not user_info.get('email'):
        logging.error("Email is required")  # ИЗМЕНЕНО: print -> logging
        return False
    if not user_info.get('age') or user_info['age'] < 18:
        logging.error("User must be 18+")  # ИЗМЕНЕНО: print -> logging
        return False
    return True

# НОВОЕ: функция для проверки статуса пользователя
def get_user_status(user_info):
    """feat: add user status function"""
    age = user_info.get('age', 0)
    if age >= 18:
        return "adult"
    else:
        return "minor"

def process_user(user_info):  # было: user_data
    # Бизнес-логика
    print(f"Processing user: {user_info.get('name', 'Unknown')}")
    
    # ДОБАВЛЕНО: обработка ошибок
    try:
        response = requests.post('https://api.example.com/users', json=user_info, timeout=5)
        print(f"API response status: {response.status_code}")
        return response
    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        return None

def main():
    user = {"name": "John", "email": "john@example.com", "age": 25}
    if validate_user(user):
        status = get_user_status(user)  # НОВОЕ: вызов новой функции
        print(f"User status: {status}")
        result = process_user(user)
        if result:  # ДОБАВЛЕНО: проверка результата
            print("User processed successfully")
        else:
            print("Failed to process user")
    else:
        print("Validation failed")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)  # ДОБАВЛЕНО: настройка логирования
    main()