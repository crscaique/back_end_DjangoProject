# users/urls.py
from django.contrib.auth.views import LoginView
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import RegisterView
from .views import LoginView
# LoginView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    ]

