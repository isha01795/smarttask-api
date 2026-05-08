def get_token(test_client):
    response = test_client.post("/auth/login", json={
        "email": "test@example.com",
        "password": "123456"
    })
    return response.json()["access_token"]


def test_create_task(test_client):
    token = get_token(test_client)

    response = test_client.post(
        "/tasks/",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "title": "Test Task",
            "description": "Testing"
        }
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"