from django.db import models
from uuid import uuid4
from root_admin.models import Admin
from people.models import People


# Create your models here.
class Bill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    billed_by = models.ForeignKey(Admin, models.CASCADE, null=False)
    buyer = models.ForeignKey(People, on_delete=models.CASCADE)
    billed_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    total_rate = models.IntegerField()
