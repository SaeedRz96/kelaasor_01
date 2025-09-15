from django.http.response import HttpResponse, JsonResponse
from product.models import Product, Category


def product_list(request):
    products = "1.T-shirt 2.Shirt 3.Jeans"
    return HttpResponse(products)


def product_list_json(request):
    products = {
        "1" : "T.shirt",
        "2" : "Shirt",
        "3" : "Jeans"
    }
    return JsonResponse(products, safe=False)


def product_detail(request, id):
    if id == '1':
        return HttpResponse("name:T-shirt price:1000")
    elif id == '2':
        return HttpResponse("name:Shirt price:3000")
    elif id == '3':
        return HttpResponse("name:Jeans price:2000")
    else:
        return HttpResponse("Product not found!")


def all_products(request):
    products = Product.objects.all().values('title','price','amount')
    # products = Product.objects.filter(price=100,amount=6).values('title','price','amount')
    # products = Product.objects.all().order_by('-price').values('title','price','amount')
    # products = Product.objects.filter(price__gte=200).values('title','price','amount')
    products = list(products)
    return JsonResponse(products, safe=False)

def all_categories(request):
    categories = Category.objects.all().values('name')
    categories = list(categories)
    return JsonResponse(categories, safe=False)


def add_product(request):
    Product.objects.create(
        title = 'جوراب',
        description = 'توضیحات',
        category_id=2,
        price=500,
        amount=1
    )
    return HttpResponse("New Product Added")


def delete_product(request):
    Product.objects.get(id=4).delete()
    return HttpResponse("Product Deleted")


def update_product(request):
    product = Product.objects.get(id=3)
    product.amount = 5
    product.save()
    return HttpResponse("Product UPdated")