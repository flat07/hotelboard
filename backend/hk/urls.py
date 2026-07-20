# backend/hk/urls.py
from django.urls import path

from .views import (
    CreateHousekeepingRequestAPIView,
)

urlpatterns = [
    path(
        "requests/",
        CreateHousekeepingRequestAPIView.as_view(),
        name="create-request",
    ),
]
