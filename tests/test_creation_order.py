import allure
import pytest

from methods import Methods
from data import *
from helpers import Checker


@allure.feature("Создание заказа")
class TestOrderCreation:

    @allure.title("c авторизацией и ингридиентами")
    @pytest.mark.positive
    def test_create_order_authorized(self, new_user, ingredients):
        order_data = generate_order(ingredients)
        response = Methods.create_order(new_user['access_token'], order_data)
        assert Checker.check_status_code(response, SUCCESS_CODE) and \
               Checker.check_field_exists(response, 'order')
