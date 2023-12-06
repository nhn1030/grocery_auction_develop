from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Seller(models.Model):
    seller_id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller')

class Buyer(models.Model):
    buyer_id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='buyer')