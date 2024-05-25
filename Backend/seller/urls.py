from django.urls import path
from .views import get_seller, add_seller

urlpatterns = [
    path("", get_seller, name="Get seller"),
    path("add_seller", add_seller, name="Add new seller"),
]
