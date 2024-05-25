from django.db import models
from uuid import uuid4
from root_admin.models import Admin


# Create your models here.
class Actions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    admin_id = models.ForeignKey(Admin, on_delete=models.CASCADE)
    done_on = models.DateTimeField(auto_now_add=True)
    action = models.CharField(
        null=False,
        choices=[
            # Billed operation
            ("add_bill", "Added Billed"),
            ("update_bill", "Updated Billed"),
            # Product operation
            ("add_product", "Added Product"),
            ("update_product", "Updated Product"),
            # Seller operations
            ("add_seller", "Added Seller"),
            ("update_seller", "Updated seller"),
            # People operations
            ("add_people", "Added People"),
            ("update_people", "Updated People"),
        ],
        max_length=50,
    )
    additional_info = models.TextField()
