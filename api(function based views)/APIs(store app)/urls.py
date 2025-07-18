from django.urls import path 
from .views import *



urlpatterns = [
    path('products_api/',api_products),
    path('products_api/<str:id>/',api_product),
    path('categories_api/',api_categories),
    path('categories_api/<str:category_id>/',api_category),
]