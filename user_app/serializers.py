from rest_framework.serializers import ModelSerializer
from user_app.models import BasketItem


class BasketItemSerializer(ModelSerializer):
    class Meta:
        model = BasketItem
        fields = ['product','quantity']
