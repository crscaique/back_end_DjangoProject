# users/urls.py

from django.urls import path
from .views import RegisterView, LoginView, LogoutView, TodoCreateView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', TodoCreateView.as_view(), name='note-create'),
    path('update/<int:pk>/', TodoUpdateView.as_view(), name='note-update'),
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name='note-delete'),
    ]


