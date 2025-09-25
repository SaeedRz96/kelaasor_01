from django.db import models
from django.contrib.auth.models import User
from product.models import Product


class Basket(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.PositiveBigIntegerField()
    delivery_price = models.PositiveBigIntegerField(default=0)
    discount = models.PositiveBigIntegerField(default=0)
    final_price = models.PositiveBigIntegerField()
    is_paid = models.BooleanField(default=False)
    destination_lat = models.FloatField(null=True, blank=True)
    destination_long = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class BasketItem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)