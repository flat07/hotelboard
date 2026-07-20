from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import MeView, RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("me/", MeView.as_view()),
]

# http://127.0.0.1:8000/api/v1/staff/auth/register/
# http://127.0.0.1:8000/api/v1/staff/auth/login/
# http://127.0.0.1:8000/api/v1/staff/auth/refresh/
# http://127.0.0.1:8000/api/v1/staff/auth/me/
