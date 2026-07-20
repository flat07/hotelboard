from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    MenuCategoryViewSet,
    MenuItemViewSet,
    RoomServiceOrderItemViewSet,
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
        "",
        include(router.urls),
    ),
]
