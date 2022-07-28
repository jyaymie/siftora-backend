from rest_framework import serializers
from .models import Bin, Product


class BinSerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField('get_product_count')
    products = serializers.SerializerMethodField('get_products')

    def get_product_count(self, bin):
        return bin.products.count()

    def get_products(self, bin):
        print(bin.products)
        return [str(product) for product in bin.products.all()]

    class Meta:
        model = Bin
        fields = ['id', 'title',
                  'product_count', 'products']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
