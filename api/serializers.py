from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = ['id','name','description','price','category','quantity','sold','photo','shipping','created']


class CategorySerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields =['id','name','description','created']