import requests
import pytest
import allure

# Функции для работы с API
def fetch_user_details():
    """Получить детали одного пользователя."""
    response = requests.get("https://reqres.in/api/users/2")
    return response

def create_new_user(name, job):
    """Создать нового пользователя."""
    response = requests.post("https://reqres.in/api/users", json={"name": name, "job": job})
    return response

def update_existing_user(user_id, name, job):
    """Обновить существующего пользователя."""
    response = requests.put(f"https://reqres.in/api/users/{user_id}", json={"name": name, "job": job})
    return response

def remove_user(user_id):
    """Удалить пользователя."""
    response = requests.delete(f"https://reqres.in/api/users/{user_id}")
    return response

# Тесты для API
@allure.feature("Робота з користувачами")
@allure.epic("API тести")
def test_SINGL_USER():
    with allure.step("Отримати деталі користувача"):
        response = fetch_user_details()
        assert response.status_code == 200
        assert 'application/json; charset=utf-8' in response.headers['Content-Type']
        user_data = response.json().get("data", {})
        assert set(["id", "email", "first_name", "last_name", "avatar"]).issubset(user_data.keys())

@allure.feature("Робота з користувачами")
@allure.epic("API тести")
def test_CREATE():
    with allure.step("Створити нового користувача"):
        response = create_new_user("morpheus", "leader")
        assert response.status_code == 201
        assert 'application/json; charset=utf-8' in response.headers['Content-Type']
        user_data = response.json()
        assert "id" in user_data and user_data["name"] == "morpheus" and user_data["job"] == "leader"

@allure.feature("Робота з користувачами")
@allure.epic("API тести")
def test_UPDATE():
    with allure.step("Оновити існуючого користувача"):
        response = update_existing_user(2, "morpheus", "zion resident")
        assert response.status_code == 200
        assert 'application/json; charset=utf-8' in response.headers['Content-Type']
        user_data = response.json()
        assert user_data["name"] == "morpheus" and user_data["job"] == "zion resident"

@allure.feature("Робота з користувачами")
@allure.epic("API тести")
def test_DELETE():
    with allure.step("Видалити користувача"):
        response = remove_user(2)
        assert response.status_code == 204
