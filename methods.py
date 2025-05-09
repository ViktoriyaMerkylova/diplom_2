import allure
import requests


from data import *


class Methods:
    @staticmethod
    @allure.step("Регистрация пользователя: {email}")
    def register_user(email, password, name):
        data = {"email": email, "password": password, "name": name}
        return requests.post(REGISTER, json=data)

    @staticmethod
    @allure.step("Авторизация пользователя")
    def login_user(email, password):
        data = {"email": email, "password": password}
        return requests.post(LOGIN, json=data)

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(token):
        headers = {'Authorization': token}
        return requests.delete(USER, headers=headers)
