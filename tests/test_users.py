import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from backend.main import app
from backend.database import Base, get_db
from backend.models import User
from backend.schemas import UserCreate
from backend.auth import get_password_hash, verify_password
from sqlalchemy.pool import StaticPool

# Setup for in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(name="db_session")
def db_session_fixture():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(name="client")
def client_fixture(db_session: Session):
    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as client:
        yield client


def test_create_user(client: TestClient, db_session: Session):
    user_data = {"email": "test@example.com", "password": "testpassword"}
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data
    assert data["is_active"] is True
    assert data["mfa_enabled"] is False
    assert "created_at" in data
    assert "updated_at" in data
    assert data["last_login_at"] is None

    # Verify user in database
    db_user = db_session.query(User).filter(User.email == "test@example.com").first()
    assert db_user is not None
    assert db_user.email == "test@example.com"
    assert verify_password("testpassword", db_user.password_hash)


def test_create_existing_user(client: TestClient, db_session: Session):
    # Create a user first
    user_data = {"email": "existing@example.com", "password": "password123"}
    client.post("/users/", json=user_data)

    # Try to create the same user again
    response = client.post("/users/", json=user_data)
    assert response.status_code == 400
    assert response.json() == {"detail": "Email already registered"}


def test_login_for_access_token(client: TestClient, db_session: Session):
    # Create a user
    user_data = {"email": "login@example.com", "password": "loginpassword"}
    client.post("/users/", json=user_data)

    # Attempt to login
    login_data = {"username": "login@example.com", "password": "loginpassword"}
    response = client.post("/token", data=login_data)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

    # Verify last_login_at is updated
    db_user = db_session.query(User).filter(User.email == "login@example.com").first()
    assert db_user.last_login_at is not None


def test_login_for_access_token_invalid_credentials(client: TestClient):
    login_data = {"username": "nonexistent@example.com", "password": "wrongpassword"}
    response = client.post("/token", data=login_data)
    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}


def test_login_for_access_token_inactive_user(client: TestClient, db_session: Session):
    # Create an inactive user
    user_data = {"email": "inactive@example.com", "password": "inactivepassword"}
    user = User(email=user_data["email"], password_hash=get_password_hash(user_data["password"]), is_active=False)
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    # Attempt to login with inactive user
    login_data = {"username": "inactive@example.com", "password": "inactivepassword"}
    response = client.post("/token", data=login_data)
    assert response.status_code == 400
    assert response.json() == {"detail": "Inactive user"}
