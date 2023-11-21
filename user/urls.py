from django.urls import path
from .views import UserRegistrationView, UserProfileView, UserLogin

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLogin.as_view(), name='user-login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]