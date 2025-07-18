from django.shortcuts import render ,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.status import HTTP_204_NO_CONTENT
from storeapp.models import *
from .serializers import *


# Create your views here.

@api_view(['GET','POST'])
def api_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products,many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET','PUT','DELETE'])
def api_product(request,id):
    product = get_object_or_404(Product,id= id)
    if request.method == 'GET' :
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = ProductSerializer(product,data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    if request.method == 'DELETE':
        product.delete()
        return Response(status=HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def api_categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories,many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = CategorySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



@api_view(['GET','PUT','DELETE'])
def api_category(request,category_id):
    category = get_object_or_404(Category, category_id = category_id)
    if request.method == 'GET' :
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = CategorySerializer(category,data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    if request.method == 'DELETE':
        category.delete()
        return Response(status=HTTP_204_NO_CONTENT)