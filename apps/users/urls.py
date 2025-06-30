# apps/users/urls.py

from django.urls import path
from .views import UserRegistrationView
from .views import UserRegistrationView, CurrentUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# استيراد العوارض الجاهزة من مكتبة Simple JWT لتسجيل الدخول
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # مسار لتسجيل مستخدم جديد
    path('register/', UserRegistrationView.as_view(), name='user-register'),

    # مسار لتسجيل الدخول (للحصول على التوكن)
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # مسار لتحديث التوكن
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('me/', CurrentUserView.as_view(), name='current-user'),

]