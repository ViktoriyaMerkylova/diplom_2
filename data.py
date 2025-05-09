from random import sample

from faker import Faker


BASE_URL = "https://stellarburgers.nomoreparties.site"

REGISTER = f"{BASE_URL}/api/auth/register"
LOGIN = f"{BASE_URL}/api/auth/login"
USER = f"{BASE_URL}/api/auth/user"
ORDERS = f"{BASE_URL}/api/orders"
INGREDIENTS = f"{BASE_URL}/api/ingredients"


fake = Faker()


def generate_user():
    return {
        "email": f'val{fake.email()}',
        "password": fake.password(),
        "name": fake.name()
    }

# Коды ответов
SUCCESS_CODE = 200
BAD_REQUEST_CODE = 400
UNAUTHORIZED_CODE = 401
FORBIDDEN_CODE = 403
SERVER_ERROR_CODE = 500

# Ожидаемые ответы
REGISTER_SUCCESS = "accessToken"
REGISTER_USER_EXISTS = {"success": False, "message": "User already exists"}
REGISTER_MISSING_FIELD = {"success": False, "message": "Email, password and name are required fields"}

LOGIN_SUCCESS = {"success": True}
LOGIN_FAILED = {"success": False, "message": "email or password are incorrect"}

UPDATE_USER_SUCCESS = {"success": True}
UPDATE_USER_UNAUTHORIZED = {"success": False, "message": "You should be authorised"}
UPDATE_USER_EXISTS = {"success": False, "message": "User with such email already exists"}

CREATE_ORDER_SUCCESS = {"success": True}
CREATE_ORDER_UNAUTHORIZED = {"success": False, "message": "You should be authorised"}
CREATE_ORDER_NO_INGREDIENTS = {"success": False, "message": "Ingredient ids must be provided"}

GET_ORDERS_SUCCESS = {"success": True}
GET_ORDERS_UNAUTHORIZED = {"success": False, "message": "You should be authorised"}

def generate_order(ingredients, count=3):
    return sample([ing['_id'] for ing in ingredients], count)