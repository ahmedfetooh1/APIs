from django.shortcuts import render ,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from storeapp.models import *
from .serializers import *


# Create your views here.
class APIProducts(APIView):
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many = True)
        return Response(serializer.data)
    def post(self,request):
        serializer = ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class APIProduct(APIView):
    
    def get(self,request,id):
            product = get_object_or_404(Product,id= id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
    def put(self,request,id):
        product = get_object_or_404(Product,id= id)
        serializer = ProductSerializer(product,data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()    

    def delete(self,request,id):
        product = get_object_or_404(Product,id= id)
        product.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class APICategories(APIView):
    def get(self,request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories,many = True)
        return Response(serializer.data)        
    def post(self,request):
        serializer = CategorySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class APICategory(APIView):
    def get(self,request,id):
        category = get_object_or_404(Category, category_id = id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self,request,id):
        category = get_object_or_404(Category, category_id = id)
        serializer = CategorySerializer(category,data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def delete(self,request,id):
        category = get_object_or_404(Category, category_id = id)
        category.delete()
        return Response(status=HTTP_204_NO_CONTENT)

