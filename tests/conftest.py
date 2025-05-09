import allure
import pytest

from methods import Methods
from data import generate_user


@pytest.fixture
def create_user():
    user_data = generate_user()
    with allure.step("Создание тестового пользователя"):
        Methods.register_user(**user_data)
    yield user_data['email'], user_data['password'], user_data['name']
    with allure.step("Удаление тестового пользователя"):
        response = Methods.login_user(user_data['email'], user_data['password'])
        Methods.delete_user(response.json()['accessToken'])

@pytest.fixture
def new_user():
    user_data = generate_user()

    with allure.step("Создание тестового пользователя"):
        Methods.register_user(**user_data)

    with allure.step("Получение токена авторизации"):
        login_response =Methods.login_user(user_data['email'], user_data['password'])

    access_token = login_response.json()['accessToken']
    user = {
        "email": user_data['email'],
        "password": user_data['password'],
        "name": user_data['name'],
        "access_token": access_token
    }

    yield user

    with allure.step("Удаление тестового пользователя"):
        Methods.delete_user(access_token)

@pytest.fixture
def ingredients():
    with allure.step("Получение списка ингредиентов"):
        response = Methods.get_ingredients()
    return response.json()['data']