from django.db import models
from uuid import uuid4
from product.models import Product
from bill.models import Bill


# Create your models here.
class Sale(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    product_id = models.ForeignKey(Product, models.CASCADE)
    bill_id = models.ForeignKey(Bill, models.CASCADE)
    quantity = models.IntegerField()
