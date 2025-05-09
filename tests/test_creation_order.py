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

    @allure.title("Без авторизации с ингридиентами")
    @pytest.mark.negative
    def test_create_order_unauthorized(self, ingredients):
        order_data = generate_order(ingredients)
        response = Methods.create_order("", order_data)
        assert Checker.check_status_code(response, SUCCESS_CODE) and \
               Checker.check_response_field(response, 'success', CREATE_ORDER_SUCCESS['success'])

    @allure.title("Без ингридиентов")
    @pytest.mark.negative
    def test_create_order_without_ingredients(self, new_user):
        response = Methods.create_order(new_user['access_token'], [])
        assert Checker.check_status_code(response, BAD_REQUEST_CODE) and \
               Checker.check_response_field(response, 'message', CREATE_ORDER_NO_INGREDIENTS['message'])

    @allure.title("с неверным хешем ингридиентов")
    @pytest.mark.negative
    def test_create_order_with_invalid_ingredients(self, new_user):
        invalid_ingredients = ["invalid_hash_1", "invalid_hash_2"]
        response = Methods.create_order(new_user['access_token'], invalid_ingredients)
        assert Checker.check_status_code(response, SERVER_ERROR_CODE), \
            (f"Неожиданный ответ при попытке создания заказа с неверным хешем ингредиентов. "
             f"Код ответа: {response.status_code}, тело ответа: {response.json()}")