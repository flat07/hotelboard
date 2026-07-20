# backend/config/api/public.py
from django.urls import include, path

urlpatterns = [
    path(
        "rooms/",
        include("rooms.public.urls"),
    ),
    path(
        "housekeeping/",
        include("hk.public.urls"),
    ),
    path(
        "engineering/",
        include("engineering.public.urls"),
    ),
    path(
        "room-service/",
        include("room_service.public.urls"),
    ),
]

# GET    /api/v1/public/engineering/services/<token>/
# POST   /api/v1/public/engineering/requests/<token>/
# GET    /api/v1/public/housekeeping/services/<token>/
# POST   /api/v1/public/housekeeping/requests/<token>/
# GET    /api/v1/public/room-service/menu/<token>/
# POST   /api/v1/public/room-service/orders/<token>/
# GET    /api/v1/public/rooms/guest/<token>/
