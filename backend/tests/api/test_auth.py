import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_register_creates_user_with_hashed_password(api_client):
    response = api_client.post(
        "/api/v1/staff/auth/register/",
        {
            "username": "receptionist",
            "password": "strong-password-123",
        },
        format="json",
    )

    assert response.status_code == 201
    assert response.data["username"] == "receptionist"

    user = User.objects.get(username="receptionist")
    assert user.check_password("strong-password-123")


@pytest.mark.django_db
def test_login_returns_tokens_for_valid_credentials(api_client):
    User.objects.create_user(
        username="manager",
        password="strong-password-123",
    )

    response = api_client.post(
        "/api/v1/staff/auth/login/",
        {
            "username": "manager",
            "password": "strong-password-123",
        },
        format="json",
    )

    assert response.status_code == 200
    assert response.data["access"]
    assert response.data["refresh"]


@pytest.mark.django_db
def test_me_requires_authentication(api_client):
    response = api_client.get("/api/v1/staff/auth/me/")

    assert response.status_code == 401


@pytest.mark.django_db
def test_me_returns_authenticated_user(api_client):
    user = User.objects.create_user(
        username="housekeeping",
        password="strong-password-123",
    )
    api_client.force_authenticate(user=user)

    response = api_client.get("/api/v1/staff/auth/me/")

    assert response.status_code == 200
    assert response.data == {"id": user.id, "username": "housekeeping"}  # type: ignore
