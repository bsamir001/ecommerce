from rest_framework import serializers
from .models import *
from account.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'description', 'stock', 'price', 'image', 'specification']


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer

    class Meta:
        model = CartItems
        fields = ['id', 'product', 'quantity']
