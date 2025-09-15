from django.contrib import admin
from product.models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'amount']
    search_fields = ['title']
    list_filter = ['category']


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
