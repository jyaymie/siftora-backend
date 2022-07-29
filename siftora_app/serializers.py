from rest_framework import serializers
from .models import Bin, Product


class BinSerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField('get_product_count')
    products = serializers.SerializerMethodField('get_products')

    def get_product_count(self, bin):
        return bin.products.count()

    def get_products(self, bin):
        return [
            {'id': product.id,
             'brand': product.brand,
             'name': product.name,
             'shade': product.shade,
             'finish': product.finish,
             'purchase_date': product.purchase_date,
             'price': product.price,
             'open_date': product.open_date,
             'expiry_date': product.expiry_date,
             'use_count': product.use_count,
             'finish_date': product.finish_date,
             'will_repurchase': product.will_repurchase,
             'notes': product.notes} for product in bin.products.all()]

    class Meta:
        model = Bin
        fields = ['id', 'title',
                  'product_count', 'products']


class ProductSerializer(serializers.ModelSerializer):
    bins = serializers.SerializerMethodField('get_bins')

    def get_bins(self, product):
        return [
            {'id': bin.id,
             'title': bin.title,
             } for bin in product.bins.all()]

    class Meta:
        model = Product
        fields = ['id', 'bins', 'brand',
                  'name', 'shade', 'finish', 'purchase_date',
                  'price', 'open_date', 'expiry_date', 'use_count', 'finish_date', 'will_repurchase', 'notes']
