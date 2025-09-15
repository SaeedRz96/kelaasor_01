from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم")
    description = models.TextField(null=True, blank=True, verbose_name="توضیحات اختیاری")
    
    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT)
    price = models.IntegerField()
    amount = models.IntegerField()