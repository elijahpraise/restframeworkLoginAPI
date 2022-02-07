from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.core.serializers import serialize
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}, 'email': {'required': True}}

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = User(username=username, email=email)
        password_validation.validate_password(password)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user

