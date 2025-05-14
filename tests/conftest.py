import allure
import pytest

from methods import UserMethods, IngredientsMethods, OrderMethods
from data import generate_user, generate_order


@pytest.fixture
def create_user():
    user_data = generate_user()
    with allure.step("Создание тестового пользователя"):
        UserMethods.register_user(**user_data)
    yield user_data['email'], user_data['password'], user_data['name']
    with allure.step("Удаление тестового пользователя"):
        response = UserMethods.login_user(user_data['email'], user_data['password'])
        UserMethods.delete_user(response.json()['accessToken'])

@pytest.fixture
def new_user():
    user_data = generate_user()

    with allure.step("Создание тестового пользователя"):
        UserMethods.register_user(**user_data)

    with allure.step("Получение токена авторизации"):
        login_response = UserMethods.login_user(user_data['email'], user_data['password'])

    access_token = login_response.json()['accessToken']
    user = {
        "email": user_data['email'],
        "password": user_data['password'],
        "name": user_data['name'],
        "access_token": access_token
    }

    yield user

    with allure.step("Удаление тестового пользователя"):
        UserMethods.delete_user(access_token)

@pytest.fixture
def ingredients():
    with allure.step("Получение списка ингредиентов"):
        response = IngredientsMethods.get_ingredients()
    return response.json()['data']

@pytest.fixture
def create_new_order(new_user, ingredients):
    order_data = generate_order(ingredients)
    with allure.step("Создание тестового заказа"):
        response = OrderMethods.create_order(new_user['access_token'], order_data)
    return response.json()
