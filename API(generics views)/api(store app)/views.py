from django.shortcuts import render ,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView ,RetrieveUpdateDestroyAPIView
from rest_framework.status import HTTP_204_NO_CONTENT
from storeapp.models import *
from .serializers import *



# Create your views here.
class APIProducts(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()



class APIProduct(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




class APICategories(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class APICategory(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
