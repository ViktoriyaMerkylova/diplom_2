import allure
import pytest

from methods import OrderMethods
from data import *
from helpers import Checker


@allure.feature("Получение заказов конкретного пользователя")
class TestGetUserOrders:

    @allure.title("авторизованный пользователь")
    @pytest.mark.positive
    def test_get_orders_authorized(self, new_user, create_new_order):
        response = OrderMethods.get_user_orders(new_user['access_token'])
        assert Checker.check_status_code(response, SUCCESS_CODE) and \
            Checker.check_field_exists(response, 'orders') and \
            len(response.json()['orders']) > 0

    @allure.title("неавторизованный пользователь")
    @pytest.mark.negative
    def test_get_orders_unauthorized(self):
        response = OrderMethods.get_user_orders("")
        assert Checker.check_status_code(response, UNAUTHORIZED_CODE) and \
               Checker.check_response_field(response, 'message', GET_ORDERS_UNAUTHORIZED['message'])