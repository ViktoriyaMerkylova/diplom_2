import allure
import pytest

from methods import Methods
from data import *
from helpers import Checker

@allure.feature("Логин пользователя")
class TestLoginUser:

    @allure.title("Логин под существующим пользователе")
    @pytest.mark.positive
    def test_login_user(self, create_user):
        email, password, _ = create_user
        response = Methods.login_user(email, password)
        assert Checker.check_status_code(response, SUCCESS_CODE) and \
               Checker.check_field_exists(response, 'accessToken')

