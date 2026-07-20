# backend/hk/public/urls.py
from django.urls import path

from .views import (
    GuestCreateHousekeepingRequestView,
    GuestHousekeepingServicesView,
)

urlpatterns = [
    path(
        "services/<str:token>/",
        GuestHousekeepingServicesView.as_view(),
        name="guest-housekeeping-services",
    ),
    path(
        "requests/<str:token>/",
        GuestCreateHousekeepingRequestView.as_view(),
        name="guest-housekeeping-request",
    ),
]

# GET    /api/v1/public/housekeeping/services/<token>/
# POST   /api/v1/public/housekeeping/requests/<token>/


# GET    /api/v1/public/housekeeping/services/<token>/
# [
#     {
#         "id": 1,
#         "code": "CLEAN_ROOM",
#         "name": "Clean Room"
#     },
#     {
#         "id": 2,
#         "code": "CHANGE_TOWELS",
#         "name": "Change Towels"
#     },
#     {
#         "id": 3,
#         "code": "REFILL_WATER",
#         "name": "Refill Water"
#     },
#     {
#         "id": 4,
#         "code": "EXTRA_PILLOW",
#         "name": "Extra Pillow"
#     }
# ]

# POST   /api/v1/public/housekeeping/requests/<token>/
# {
#     "note": "Please come after 2 PM.",
#     "items": [
#         {
#             "service": 1
#         },
#         {
#             "service": 2
#         }
#     ]
# }
# {
#     "id": 15,
#     "status": "PENDING",
#     "note": "Please come after 2 PM.",
#     "created_at": "2026-07-18T11:15:00Z"
# }
