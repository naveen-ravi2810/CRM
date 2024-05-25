from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    LoginSerializer,
    RegisterSerializer,
    ReadAdminProfile,
    UpdateAdminSerializer,
)
from .models import Admin
from CRM.utils import create_access_token, check_password, hash_password, admin_required
from django.db.utils import IntegrityError


@api_view(["POST"])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        admin = Admin.objects.filter(email=serializer.validated_data["email"]).first()
        if admin:
            if check_password(serializer.validated_data["password"], admin.password):
                token = create_access_token(admin)
                return Response({"access_token": token}, status=200)
        return Response({"message": "Invalid email/Password"}, status=401)
    else:
        return Response({"status": serializer.errors}, status=401)


@api_view(["POST"])
def register(request):
    try:
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["password"] = hash_password(
                serializer.validated_data["password"]
            )
            Admin.objects.create(**serializer.validated_data)
            return Response({"message": "User Added Successfully"}, 201)
        else:
            return Response({"message": serializer.errors}, 400)
    except IntegrityError:
        return Response({"message": "User with similar data exists"}, 400)


@api_view(["GET"])
@admin_required
def get_profile(request):
    admin = Admin.objects.filter(id=request.jwt_payload.get("id")).first()
    if not admin:
        return Response({"message": "Admin not found"}, status.HTTP_404_NOT_FOUND)
    admin = ReadAdminProfile(admin)
    return Response(admin.data, status.HTTP_200_OK)


@api_view(["PUT"])
@admin_required
def update_admin(request):
    admin: Admin = Admin.objects.filter(id=request.jwt_payload.get("id")).first()
    if not admin:
        return Response({"message": "Admin Not Found"}, status.HTTP_404_NOT_FOUND)
    serializer = UpdateAdminSerializer(admin, request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        serializer = ReadAdminProfile(admin)
    return Response({"message": serializer.data}, status.HTTP_201_CREATED)
