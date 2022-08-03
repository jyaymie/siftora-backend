from rest_framework import serializers
from .models import Bin, Product


class BinsSerializerField(serializers.Field):
    def to_representation(self, obj):
        return [
            {
                'id': bin.id,
                'title': bin.title,
            } for bin in obj.all()]

    def to_internal_value(self, data):
        return [item["id"] for item in data]


class ProductsSerializerField(serializers.Field):
    def to_representation(self, obj):
        return [
            {'id': product.id,
             'brand': product.brand,
             'name': product.name,
             'shade': product.shade,
             'purchase_date': product.purchase_date,
             'price': product.price,
             'open_date': product.open_date,
             'expiry_date': product.expiry_date,
             'use_count': product.use_count,
             'finish_date': product.finish_date,
             'will_repurchase': product.will_repurchase,
             'image': product.image,
             'notes': product.notes} for product in obj.all()]

    def to_internal_value(self, data):
        return [item['id'] for item in data]


class BinSerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField('get_product_count')
    products = ProductsSerializerField()

    def get_product_count(self, bin):
        return bin.products.count()

    class Meta:
        model = Bin
        fields = ['id', 'title',
                  'product_count', 'products']


class ProductSerializer(serializers.ModelSerializer):
    bins = BinsSerializerField()

    class Meta:
        model = Product
        fields = ['id', 'bins', 'brand',
                  'name', 'shade', 'purchase_date',
                  'price', 'open_date', 'expiry_date', 'use_count', 'finish_date', 'will_repurchase', 'image', 'notes']
