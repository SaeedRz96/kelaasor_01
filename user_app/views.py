from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from user_app.serializers import BasketItemSerializer
from user_app.models import Basket, BasketItem, OTP
from rest_framework.views import APIView
from rest_framework.response import Response
from user_app.permissions import IsNotBanUser
from user_app.tasks import send_email_to_user
import random
from datetime import timedelta
from django.utils.timezone import now
from django.core.cache import cache


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
        send_email_to_user.delay()
        return Response("Basket status: PAID!")


class GetOTP(APIView):
    
    def post(self, request):
        genrated_otp = random.randint(1000,9999)
        phone_number = request.data.get('phone_number')
        # SEND OTP TO USER BY SMS
        cache.set(phone_number,genrated_otp, timeout=180)
        
        # otp_object = OTP.objects.create(
        #     otp = genrated_otp,
        #     phone_number = request.data.get('phone_number'),
        # )
        # SEND OTP TO USER BY SMS
        # otp_object.expire_date = now() + timedelta(seconds=180)
        # otp_object.save()
        return Response("OTP sent!")


class CheckOTP(APIView):
    
    def post(self, request):
        input_otp = request.data.get('otp')
        input_phone_number = request.data.get('phone_number')
        saved_otp = cache.get(input_phone_number)
        if saved_otp == input_otp:
            return Response("OK")
        else:
            return Response('Some things wrong!!')
        
        # saved_otp = OTP.objects.get(phone_number=input_phone_number)
        # if saved_otp.otp == input_otp and saved_otp.expire_date >= now():
        #     saved_otp.delete()
        #     return Response('OK')
        # else:
        #     return Response('Some things wrong!!')