from rest_framework import serializers
from .models import products,categories

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = ['id','title','category']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = categories
        fields = ['id','title']


