# backend/config/api/urls.py
from django.urls import include, path

urlpatterns = [
    path(
        "public/",
        include("config.api.public"),
    ),
    path(
        "staff/",
        include("config.api.staff"),
    ),
]
