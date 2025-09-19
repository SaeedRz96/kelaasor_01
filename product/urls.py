from django.urls import path
from product.views import (
    product_list,
    product_detail,
    product_list_json,
    all_products,
    all_categories,
    add_product,
    delete_product,
    update_product,
    AllProductList,
    AddProduct,
    DeleteProduct,
    UpdateProduct,
    RetrieveProduct
)


urlpatterns = [
    path("list", product_list),
    path("detail/<str:id>", product_detail),
    path("list-json", product_list_json),
    path("all-products", all_products),
    path("all-cetegories", all_categories),
    path('add-product',add_product),
    path('delete-product', delete_product),
    path('update-product', update_product),
    path('product-list', AllProductList.as_view()),
    path('add-product-new', AddProduct.as_view()),
    path('delete-product-new/<str:pk>', DeleteProduct.as_view()),
    path('update-product-new/<str:pk>',UpdateProduct.as_view()),
    path('retrieve-product/<str:pk>', RetrieveProduct.as_view())
]
