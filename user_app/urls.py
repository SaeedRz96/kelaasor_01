from django.urls import path

from user_app.views import (AddProductToBasketItem, BasketItemList,
                            DeleteBasketItem, SetPaidStatus, TransactionView)

urlpatterns = [
    path("add-to-basketitem", AddProductToBasketItem.as_view()),
    path("my-basketitem-list", BasketItemList.as_view()),
    path("delete-basketitem/<str:pk>", DeleteBasketItem.as_view()),
    path("set-basket-status/<str:basket_id>", SetPaidStatus.as_view()),
    path("new-transaction", TransactionView.as_view()),
]
