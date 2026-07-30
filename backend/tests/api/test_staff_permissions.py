import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
@pytest.mark.parametrize(
    "url",
    [
        "/api/v1/staff/rooms/rooms/",
        "/api/v1/staff/engineering/services/",
        "/api/v1/staff/room-service/categories/",
        "/api/v1/staff/housekeeping/requests-get/",
    ],
)
def test_staff_management_endpoints_require_authentication(api_client, url):
    response = api_client.get(url)

    assert response.status_code == 401
