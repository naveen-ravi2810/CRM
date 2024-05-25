from rest_framework import serializers
from .models import Seller


class AddNewSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = [
            "first_name",
            "last_name",
            "shop_name",
            "shop_address",
            "phone",
        ]


class GetSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = [
            "id",
            "first_name",
            "last_name",
            "shop_name",
            "shop_address",
            "phone",
        ]
