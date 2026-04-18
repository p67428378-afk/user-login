from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from backend.models import User
from backend.crud import get_password_hash

def test_read_main(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the User Login API"}

def test_register_user(client: TestClient):
    response = client.post(
        "/auth/register",
        json={
            "email": "test@example.com",
            "password": "password123"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data
    assert "is_active" in data
    assert "mfa_enabled" in data
    assert "created_at" in data

def test_register_existing_user(client: TestClient):
    client.post(
        "/auth/register",
        json={
            "email": "existing@example.com",
            "password": "password123"
        }
    )
    response = client.post(
        "/auth/register",
        json={
            "email": "existing@example.com",
            "password": "password123"
        }
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Email already registered"}

def test_login_for_access_token(client: TestClient, session: Session):
    # Create a user directly in the database for login test
    hashed_password = get_password_hash("password123")
    user = User(email="login@example.com", password_hash=hashed_password)
    session.add(user)
    session.commit()
    session.refresh(user)

    response = client.post(
        "/auth/token",
        data={
            "username": "login@example.com",
            "password": "password123"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_for_access_token_invalid_credentials(client: TestClient):
    response = client.post(
        "/auth/token",
        data={
            "username": "nonexistent@example.com",
            "password": "wrongpassword"
        }
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}

def test_read_users_me(client: TestClient, session: Session):
    # Create a user and get a token
    hashed_password = get_password_hash("password123")
    user = User(email="me@example.com", password_hash=hashed_password)
    session.add(user)
    session.commit()
    session.refresh(user)

    token_response = client.post(
        "/auth/token",
        data={
            "username": "me@example.com",
            "password": "password123"
        }
    )
    token = token_response.json()["access_token"]

    response = client.get(
        "/auth/users/me",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "me@example.com"
    assert "id" in data
