from django.contrib import admin

# Register your models here.
from market.models import Seller, Buyer

admin.site.register(Seller)
admin.site.register(Buyer)