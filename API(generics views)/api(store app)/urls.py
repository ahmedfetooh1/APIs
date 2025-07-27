from django.urls import path 
from .views import *



urlpatterns = [
    path('products_api/',APIProducts.as_view()),
    path('products_api/<str:pk>/',APIProduct.as_view()),
    path('categories_api/',APICategories.as_view()),
    path('categories_api/<str:pk>/',APICategory.as_view()),
]