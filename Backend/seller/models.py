from django.db import models
from uuid import uuid4


class Seller(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    shop_name = models.CharField(unique=True, max_length=100, null=False)
    shop_address = models.TextField(max_length=800, null=False)
    phone = models.BigIntegerField(null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
