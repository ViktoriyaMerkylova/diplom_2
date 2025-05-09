import allure
import pytest

from methods import Methods
from data import generate_user


@pytest.fixture
def create_user():
    user_data = generate_user()
    yield user_data['email'], user_data['password'], user_data['name']
    with allure.step("Удаление тестового пользователя"):
        response = Methods.login_user(user_data['email'], user_data['password'])
        Methods.delete_user(response.json()['accessToken'])