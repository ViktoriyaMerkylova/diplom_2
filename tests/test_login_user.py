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

    @allure.title("Логин с неверным логином и паролем")
    @pytest.mark.negative
    @pytest.mark.parametrize("email,password", [
        ("error@gmail.com", "correctpassword"),
        ("correct@gmail.com", "errorpassword"),
    ])
    def test_login_failed(self, create_user, email, password):
        correct_email, correct_password, _ = create_user
        if email == "correct@email.com":
            email = correct_email
        if password == "correctpassword":
            password = correct_password

        response = Methods.login_user(email, password)
        assert Checker.check_status_code(response, UNAUTHORIZED_CODE) and \
               Checker.check_response_field(response, 'message', LOGIN_FAILED['message'])