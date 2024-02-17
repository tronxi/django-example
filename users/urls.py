from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.api.custom_token_pair_api_view import CustomTokenObtainPairView
from users.api.profile_api_view import ProfileAPIView
from users.api.register_api_view import RegisterView

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('profile/', ProfileAPIView.as_view(), name='profile'),


]