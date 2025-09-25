from django.contrib import admin
from user_app.models import Basket, BasketItem


admin.site.register(BasketItem)
admin.site.register(Basket)