from django.contrib.auth.views import LoginView
from rest_framework import generics, status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class LoginView(ObtainAuthToken):
       def post(self, request, *args, **kwargs):
           response = super(LoginView, self).post(request, *args, **kwargs)
           token = Token.objects.get(key=response.data['token'])
           return Response({'token': token.key, 'user_id': token.user_id})

class LogoutView(generics.GenericAPIView):
   permission_classes = (IsAuthenticated,)

    # def post(self, request):
    #  request.user.auth_token.delete()
    #     return Response(status=status.HTTP_200_OK)

# Create your views here.
