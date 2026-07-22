from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    MenuCategoryViewSet,
    MenuItemViewSet,
    RoomServiceOrderItemViewSet,
    RoomServiceOrderListApiView,
    RoomServiceOrderViewSet,
)

router = DefaultRouter()

router.register(
    "categories",
    MenuCategoryViewSet,
)

router.register(
    "menu-items",
    MenuItemViewSet,
)

router.register(
    "orders",
    RoomServiceOrderViewSet,
)

router.register(
    "order-items",
    RoomServiceOrderItemViewSet,
)

urlpatterns = [
    path(
        "orders-get/",
        RoomServiceOrderListApiView.as_view(),
        name="order-list",
    ),
    path(
        "",
        include(router.urls),
    ),
]

#  /api/v1/staff/room-service/orders-get/


# GET /api/v1/staff/room-service/orders-get/?status=PENDING
# GET /api/v1/staff/room-service/orders-get/?status=ASSIGNED
# GET /api/v1/staff/room-service/orders-get/?room=1205
# GET /api/v1/staff/room-service/orders-get/?assigned_to=john
# GET /api/v1/staff/room-service/orders-get/?status=PENDING&room=1205
# GET /api/v1/staff/room-service/orders-get/?search=breakfast
# GET /api/v1/staff/room-service/orders-get/?search=1205
# GET /api/v1/staff/room-service/orders-get/?search=john
