import allure
import pytest

from methods import UserMethods
from data import *
from helpers import Checker


@allure.feature("Изменение данных пользователя")
class TestUpdateUser:

    @allure.title("С авторизацией")
    @pytest.mark.positive
    @pytest.mark.parametrize('update_field', ['email', 'name'])
    def test_update_authorized_user(self, new_user, update_field):
        new_data = generate_user()
        payload = {update_field: new_data[update_field]}
        response = UserMethods.update_user(new_user['access_token'], **payload)
        assert Checker.check_status_code(response, SUCCESS_CODE) and \
               Checker.check_user_field(response, update_field, new_data[update_field])


    @allure.title("Без авторизации")
    @pytest.mark.negative
    @pytest.mark.parametrize("field", ["email", "name"])
    def test_update_unauthorized_user(self, field):
        new_data = generate_user()
        response = UserMethods.update_user("", **{field: new_data[field]})
        assert Checker.check_status_code(response, UNAUTHORIZED_CODE) and \
               Checker.check_response_field(response, 'message', UPDATE_USER_UNAUTHORIZED['message'])
