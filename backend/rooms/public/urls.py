# backend/rooms/public/urls.py
from django.urls import path

from .views import GuestRoomView

urlpatterns = [
    path(
        "guest/<str:token>/",
        GuestRoomView.as_view(),
        name="guest-room",
    ),
]

# GET    /api/v1/public/rooms/guest/<token>/
# {
#     "room_number": "1205",
#     "room_type": "DELUXE"
# }
