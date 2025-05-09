import allure
import pytest

from methods import Methods
from data import *
from helpers import Checker


@allure.feature("Создание пользователя")
class TestCreationUser:

    @allure.title("Успешное создание уникального пользователя")
    @pytest.mark.positive
    def test_create_new_user(self):
        data = generate_user()
        response = Methods.register_user(**data)
        assert Checker.check_status_code(response, SUCCESS_CODE) and \
               Checker.check_field_exists(response, REGISTER_SUCCESS)

    @allure.title("Создание пользователя, который уже зарегистрирован")
    @pytest.mark.negative
    def test_create_user_existing(self, create_user):
        email, password, name = create_user
        response = Methods.register_user(email=email, password=password, name=name)
        assert Checker.check_status_code(response, FORBIDDEN_CODE) and \
               Checker.check_response_field(response, 'message', REGISTER_USER_EXISTS['message'])

    @allure.title("Создание пользователя без одного обязательного поля")
    @pytest.mark.negative
    @pytest.mark.parametrize("field", ["email", "password", "name"])
    def test_create_user_field(self, field):
        data = generate_user()
        data[field] = ""
        response = Methods.register_user(**data)
        assert Checker.check_status_code(response, FORBIDDEN_CODE) and \
               Checker.check_response_field(response, 'message', REGISTER_MISSING_FIELD['message'])