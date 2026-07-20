from django.urls import path

from .views import (
    GuestCreateEngineeringRequestView,
    GuestEngineeringServicesView,
)

urlpatterns = [
    path(
        "services/<str:token>/",
        GuestEngineeringServicesView.as_view(),
        name="guest-engineering-services",
    ),
    path(
        "requests/<str:token>/",
        GuestCreateEngineeringRequestView.as_view(),
        name="guest-engineering-request",
    ),
]

# GET    /api/v1/public/engineering/services/<token>/
# POST   /api/v1/public/engineering/requests/<token>/


# GET  /api/public/engineering/services/<token>/
# [
#     {
#         "id": 1,
#         "code": "AIR_CONDITIONING",
#         "name": "Air Conditioning"
#     },
#     {
#         "id": 2,
#         "code": "LIGHTING",
#         "name": "Lighting"
#     },
#     {
#         "id": 3,
#         "code": "TELEVISION",
#         "name": "Television"
#     }
# ]

# POST /api/public/engineering/requests/<token>/
# {
#     "note": "Air conditioner is not cooling.",
#     "items": [
#         {
#             "service": 1
#         },
#         {
#             "service": 2
#         }
#     ]
# }

# Response
# {
#     "id": 8,
#     "status": "PENDING",
#     "note": "Air conditioner is not cooling.",
#     "created_at": "2026-07-18T17:15:23Z",
#     "completed_at": null
# }
