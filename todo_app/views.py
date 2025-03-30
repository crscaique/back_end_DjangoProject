from django.contrib.auth.views import LoginView
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    from django.shortcuts import render

class LoginView(ObtainAuthToken):
       def post(self, request, *args, **kwargs):
           response = super(LoginView, self).post(request, *args, **kwargs)
           token = Token.objects.get(key=response.data['token'])
           return Response({'token': token.key, 'user_id': token.user_id})

# Create your views here.
