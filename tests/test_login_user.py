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

    @allure.title("Логин с неверным логином")
    @pytest.mark.negative
    def test_login_with_wrong_email(self, create_user):
        correct_email, correct_password, _ = create_user
        wrong_email = "error@gmail.com"

        response = Methods.login_user(wrong_email, correct_password)
        assert Checker.check_status_code(response, UNAUTHORIZED_CODE) and \
               Checker.check_response_field(response, 'message', LOGIN_FAILED['message'])

    @allure.title("Логин с неверным паролем")
    @pytest.mark.negative
    def test_login_with_wrong_password(self, create_user):
        correct_email, correct_password, _ = create_user
        wrong_password = "errorpassword"

        response = Methods.login_user(correct_email, wrong_password)
        assert Checker.check_status_code(response, UNAUTHORIZED_CODE) and \
               Checker.check_response_field(response, 'message', LOGIN_FAILED['message'])
