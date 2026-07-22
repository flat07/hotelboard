# backend/hk/urls.py
from django.urls import path

from .views import (
    CreateHousekeepingRequestAPIView,
    HousekeepingRequestListAPIView,
)

urlpatterns = [
    path(
        "requests/",
        CreateHousekeepingRequestAPIView.as_view(),
        name="create-request",
    ),
    path(
        "requests-get/",
        HousekeepingRequestListAPIView.as_view(),
        name="housekeeping-request-list",
    ),
]

# /api/v1/staff/housekeeping/requests/
# /api/v1/staff/housekeeping/requests-get/


# GET /api/v1/staff/housekeeping/requests-get/?status=PENDING
# GET /api/v1/staff/housekeeping/requests-get/?status=ASSIGNED
# GET /api/v1/staff/housekeeping/requests-get/?room=1205
# GET /api/v1/staff/housekeeping/requests-get/?assigned_to=john
# GET /api/v1/staff/housekeeping/requests-get/?status=PENDING&room=1205
# GET /api/v1/staff/housekeeping/requests-get/?search=towels
# GET /api/v1/staff/housekeeping/requests-get/?search=1205
# GET /api/v1/staff/housekeeping/requests-get/?search=john

# /api/v1/staff/housekeeping/requests-get/

# Example response
# [
#     {
#         "id": 12,
#         "room_number": "1205",
#         "status": "PENDING",
#         "assigned_to": null,
#         "note": "Need extra towels",
#         "services": [
#             "Clean Room",
#             "Change Towels"
#         ],
#         "created_at": "2026-07-20T10:12:30Z"
#     },
#     {
#         "id": 11,
#         "room_number": "1402",
#         "status": "ASSIGNED",
#         "assigned_to": "john",
#         "note": "",
#         "services": [
#             "Make Bed"
#         ],
#         "created_at": "2026-07-20T09:48:11Z"
#     }
# ]
