from django.contrib import admin
from .models import Basket, BasketItem

admin.site.register(BasketItem)
admin.site.register(Basket)

