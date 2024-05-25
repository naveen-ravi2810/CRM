from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from CRM.utils import admin_required
from .models import Seller
from django.http import HttpRequest
from .serializers import AddNewSellerSerializer, GetSellerSerializer


# Create your views here.
@api_view(["get"])
@admin_required
def get_seller(request: HttpRequest):
    seller_id = request.GET.get("id")
    first_name = request.GET.get("first_name")
    last_name = request.GET.get("last_name")
    shop_name = request.GET.get("shop_name")
    phone = request.GET.get("phone")
    filter_kwargs = {}
    if seller_id:
        filter_kwargs["id"] = seller_id
    if first_name:
        filter_kwargs["first_name__icontains"] = first_name
    if last_name:
        filter_kwargs["last_name__icontains"] = last_name
    if shop_name:
        filter_kwargs["shop_name__icontains"] = shop_name
    if phone:
        filter_kwargs["phone__icontains"] = phone
    sellers = Seller.objects.filter(**filter_kwargs).all()
    if not sellers:
        return Response({"message": "Seller not found"}, status.HTTP_404_NOT_FOUND)
    serializer = GetSellerSerializer(sellers, many=True)
    return Response({"message": serializer.data}, status.HTTP_200_OK)


@api_view(["POST"])
@admin_required
def add_seller(request: HttpRequest):
    serializer = AddNewSellerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Seller added successfully"}, status.HTTP_201_CREATED
        )
    return Response({"message": serializer.errors}, status.HTTP_400_BAD_REQUEST)
