from django.contrib import admin
from user_app.models import Basket, BasketItem, Profile, Transaction, Wallet


admin.site.register(Profile)
admin.site.register(BasketItem)
admin.site.register(Basket)
admin.site.register(Transaction)
admin.site.register(Wallet)