from django.contrib import admin
from user_app.models import Basket, BasketItem, Profile


admin.site.register(Profile)
admin.site.register(BasketItem)
admin.site.register(Basket)