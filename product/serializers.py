from rest_framework.serializers import ModelSerializer, StringRelatedField
from product.models import Product, Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = ['title', 'price', 'category']


class ProductCreateSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'