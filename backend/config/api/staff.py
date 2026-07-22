# backend/config/api/staff.py
from django.urls import include, path

urlpatterns = [
    path(
        "rooms/",
        include("rooms.urls"),
    ),
    path(
        "housekeeping/",
        include("hk.urls"),
    ),
    path(
        "auth/",
        include(
            "staff.urls",
        ),
    ),
    path(
        "engineering/",
        include("engineering.urls"),
    ),
    path(
        "room-service/",
        include("room_service.urls"),
    ),
]

# /api/v1/staff/housekeeping/
# /api/v1/staff/auth/
