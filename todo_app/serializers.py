from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email','password']

def create (self, validated_data):
    user = User.objects.create_user(**validated_data)
    user.set_password(validated_data['password'])
    user.save()
    return user

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        '__all__'