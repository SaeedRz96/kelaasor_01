from rest_framework.serializers import ModelSerializer
from user_app.models import BasketItem, Transaction


class BasketItemSerializer(ModelSerializer):
    class Meta:
        model = BasketItem
        fields = ["product", "quantity"]


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
        read_only_fields = ["user", "date", "payment_code", "payment_type"]
