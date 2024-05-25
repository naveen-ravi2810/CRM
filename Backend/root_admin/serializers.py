from rest_framework import serializers
from .models import Admin


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ["first_name", "last_name", "email", "phone", "password"]


class ReadAdminProfile(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    phone = serializers.IntegerField()
    created_on = serializers.DateTimeField()
    updated_on = serializers.DateTimeField()


class UpdateAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ["first_name", "last_name", "phone"]
