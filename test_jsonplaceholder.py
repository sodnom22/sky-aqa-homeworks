import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_create_post():
    """
    Успешное создание поста (POST /posts).
    Ожидаемый статус-код: 201.
    """
    payload = {
        "title": "Test Post",
        "body": "This is a test post created via pytest.",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"
    
    json_data = response.json()
    # Проверяем, что в ответе появился новый ID
    assert "id" in json_data, "Response JSON does not contain 'id'"
    # Проверяем соответствие переданных данных
    assert json_data["title"] == payload["title"], "Title does not match"
    assert json_data["body"] == payload["body"], "Body does not match"
    assert json_data["userId"] == payload["userId"], "UserId does not match"

def test_update_post():
    """
    Успешное изменение поста (PUT /posts/{id}).
    Ожидаемый статус-код: 200.
    """
    post_id = 1
    updated_payload = {
        "title": "Updated Title",
        "body": "Updated body content.",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=updated_payload)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    json_data = response.json()
    # Проверяем, что id не изменился и данные обновлены
    assert json_data["id"] == post_id, f"Expected post id {post_id}, got {json_data['id']}"
    assert json_data["title"] == updated_payload["title"], "Title was not updated correctly"
    assert json_data["body"] == updated_payload["body"], "Body was not updated correctly"
    assert json_data["userId"] == updated_payload["userId"], "UserId was not updated correctly"

def test_delete_post():
    """
    Успешное удаление поста (DELETE /posts/{id}).
    Ожидаемый статус-код: 200 или 204.
    """
    post_id = 1
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code in [200, 204], f"Expected status code 200 or 204, got {response.status_code}"
