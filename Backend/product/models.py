from django.db import models
from uuid import uuid4
from seller.models import Seller
from root_admin.models import Admin


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(null=False, max_length=100)
    type = models.CharField(null=False, max_length=100)
    seller_id = models.ForeignKey(Seller, models.CASCADE)
    updater_id = models.ForeignKey(Admin, models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    price = models.IntegerField(null=False)
    discount = models.IntegerField(null=False)
    quantity = models.IntegerField(null=False)
