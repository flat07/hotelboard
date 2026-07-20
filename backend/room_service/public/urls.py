# backend/room_service/public/urls.py
from django.urls import path

from .views import (
    GuestCreateOrderView,
    GuestMenuView,
)

urlpatterns = [
    path(
        "menu/<str:token>/",
        GuestMenuView.as_view(),
        name="guest-menu",
    ),
    path(
        "orders/<str:token>/",
        GuestCreateOrderView.as_view(),
        name="guest-create-order",
    ),
]

# GET    /api/v1/public/room-service/menu/<token>/
# POST   /api/v1/public/room-service/orders/<token>/

# GET    /api/v1/public/room-service/menu/<token>/
# [
#     {
#         "id": 1,
#         "name": "Breakfast",
#         "items": [
#             {
#                 "id": 1,
#                 "name": "Omelette",
#                 "description": "Three eggs with cheese",
#                 "price": "28.00"
#             },
#             {
#                 "id": 2,
#                 "name": "Pancakes",
#                 "description": "Served with maple syrup",
#                 "price": "24.00"
#             }
#         ]
#     },
#     {
#         "id": 2,
#         "name": "Beverages",
#         "items": [
#             {
#                 "id": 3,
#                 "name": "Coffee",
#                 "description": "Freshly brewed coffee",
#                 "price": "12.00"
#             }
#         ]
#     }
# ]

# POST   /api/v1/public/room-service/orders/<token>/
# {
#     "note": "Please bring extra ketchup.",
#     "items": [
#         {
#             "menu_item": 1,
#             "quantity": 2
#         },
#         {
#             "menu_item": 3,
#             "quantity": 1
#         }
#     ]
# }
# {
#     "id": 12,
#     "status": "PENDING",
#     "note": "Please bring extra ketchup.",
#     "total_price": "68.00",
#     "created_at": "2026-07-18T15:20:11Z"
# }
