from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

app_name = 'account'

urlpatterns = [
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/send_code', SendCodeView.as_view(), name='send_code'),
    path('api/v1/register_or_login', RegisterView.as_view(), name='register_view'),
]
