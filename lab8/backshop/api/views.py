from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Product, Category


def products_list(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    data = {
        'products': products_json,
    }
    return JsonResponse(data)


def product_details(request, product_id):
    try:
        product = Product.objects.get(id=product_id).to_json()
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(product)

def categories_list(request):
    categories =Category.objects.all()

    categories_json =[category.to_json() for category in categories]
    return JsonResponse(categories_json,safe=False)

def category_detail(request,category_id):
    try:
        category=Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error':str(e)})

    return JsonResponse(category.to_json())

def category_products(request,category_id):
    try:
        category=Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error':str(e)})
    products = category.product_set.all()
    products_json=[product.to_json()for product in products]

    return JsonResponse(products_json, safe=False)