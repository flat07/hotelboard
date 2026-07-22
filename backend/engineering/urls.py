# backend/engineering/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    EngineeringRequestItemViewSet,
    EngineeringRequestListAPIView,
    EngineeringRequestViewSet,
    EngineeringServiceViewSet,
)

router = DefaultRouter()

router.register(
    "services",
    EngineeringServiceViewSet,
)

router.register(
    "requests",
    EngineeringRequestViewSet,
)

router.register(
    "request-items",
    EngineeringRequestItemViewSet,
)

urlpatterns = [
    path(
        "requests-get/",
        EngineeringRequestListAPIView.as_view(),
        name="engineering-request-list",
    ),
    path(
        "",
        include(router.urls),
    ),
]

# GET /api/v1/staff/engineering/requests-get/
# GET /api/v1/staff/engineering/requests-get/?status=PENDING
# GET /api/v1/staff/engineering/requests-get/?assigned_to=3
# GET /api/v1/staff/engineering/requests-get/?search=101
# GET /api/v1/staff/engineering/requests-get/?ordering=-created_at
