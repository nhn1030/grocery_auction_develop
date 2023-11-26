from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    user_type = models.CharField(max_length=255)
    user_business_info = models.TextField()
    user_address = models.CharField(max_length=255)
    account_info = models.TextField()
    payment_info = models.TextField()

class Seller(models.Model):
    seller_id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller')

class Buyer(models.Model):
    buyer_id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='buyer')

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField()
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    transaction_status = models.CharField(max_length=255)
    transaction_type = models.CharField(max_length=255)
    is_safe_payment = models.BooleanField()

class Match(models.Model):
    match_id = models.AutoField(primary_key=True)
    provider_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    demender_id = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    match_date = models.DateTimeField()
    match_type = models.CharField(max_length=255)

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    category = models.CharField(max_length=255)

class Supply(models.Model):
    supply_id = models.AutoField(primary_key=True)
    supply_date = models.DateTimeField()
    supply_region = models.CharField(max_length=255)
    supply_item = models.CharField(max_length=255)
    supply_quantity = models.IntegerField()
    supplier = models.ForeignKey(User, on_delete=models.CASCADE)
