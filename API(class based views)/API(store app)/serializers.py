from rest_framework import serializers
from storeapp.models import *





class ProductSerializer(serializers.ModelSerializer):
    class Meta :
        model = Product
        fields = ['id','name', 'description', 'old_price', 'category', 'slug','inventory','price']

class CategorySerializer(serializers.ModelSerializer):
    class  Meta:
        model = Category
        fields = ['category_id','title',  'slug']