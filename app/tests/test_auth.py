import random

def test_signup(test_client):
    email = f"test{random.randint(1,100000)}@example.com"

    response = test_client.post("/auth/signup", json={
        "email": email,
        "password": "123456"
    })

    assert response.status_code == 200


def test_login(test_client):
    email = f"test{random.randint(1,100000)}@example.com"

    # first signup
    test_client.post("/auth/signup", json={
        "email": email,
        "password": "123456"
    })

    # then login
    response = test_client.post("/auth/login", json={
        "email": email,
        "password": "123456"
    })

    assert response.status_code == 200
    assert "access_token" in response.json()