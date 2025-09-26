from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from user_app.serializers import BasketItemSerializer
from user_app.models import Basket, BasketItem
from rest_framework.views import APIView
from rest_framework.response import Response
from user_app.permissions import IsNotBanUser


def _update_basket_price(basket):
    basket.total_price = 0
    basket.save()
    i = 0
    for item in BasketItem.objects.filter(basket=basket):
        basket.total_price = basket.total_price + (item.quantity * item.product.price)
        i += 1
    if i > 9 :
        discount = 3000
    basket.final_price = basket.total_price + basket.delivery_price - (basket.discount + discount)
    basket.save()


class AddProductToBasketItem(CreateAPIView):
    permission_classes = [IsAuthenticated, IsNotBanUser]
    serializer_class = BasketItemSerializer
    queryset = BasketItem.objects.all()
    
    def perform_create(self, serializer):
        if not Basket.objects.filter(owner=self.request.user, is_paid=False).exists():
            basket = Basket.objects.create(
                owner=self.request.user,
                total_price = 0,
                final_price = 0,
            )
        else:
            basket = Basket.objects.get(owner=self.request.user, is_paid=False)
        serializer.save(owner=self.request.user, basket=basket)
        _update_basket_price(basket)


class BasketItemList(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BasketItemSerializer
    queryset = BasketItem.objects.all()
    
    def get_queryset(self):
        return BasketItem.objects.filter(owner=self.request.user)


class DeleteBasketItem(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BasketItemSerializer
    queryset = BasketItem.objects.all()

    def get_queryset(self):
        return BasketItem.objects.filter(owner=self.request.user)


class SetPaidStatus(APIView):
    permission_classes = [IsAdminUser]
    
    def post(self, request, basket_id):
        basket = Basket.objects.get(id=basket_id)
        basket.is_paid = True
        basket.save()
        # Update product amount
        return Response("Basket status: PAID!")