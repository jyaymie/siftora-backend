from rest_framework import serializers
from .models import Bin, Product


class BinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bin
        fields = ('id', 'title', 'product_count')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'brand', 'name', 'shade',
                  'texture', 'purchase_date', 'price', 'open_date', 'expiry_date', 'use_count', 'finish_date', 'will_repurchase', 'notes')
