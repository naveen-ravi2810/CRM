from django.db import models
from uuid import uuid4


# Create your models here.
class Admin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(null=False, max_length=100)
    last_name = models.CharField(null=False, max_length=100)
    email = models.CharField(unique=True, max_length=100)
    phone = models.BigIntegerField(null=False, unique=True, db_index=True)
    password = models.CharField(max_length=250, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
