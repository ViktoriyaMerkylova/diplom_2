import allure
import pytest

from methods import Methods
from data import *
from helpers import Checker


@allure.feature("Создание пользователя")
class TestCreationUser:

    @allure.title("Успешное создание нового пользователя")
    @pytest.mark.positive
    def test_create_new_user(self):
        data = generate_user()
        response = Methods.register_user(**data)
        assert Checker.check_status_code(response, SUCCESS_CODE) and \
               Checker.check_field_exists(response, REGISTER_SUCCESS)