from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BinSerializer, ProductSerializer
from .models import Bin, Product


class BinView(viewsets.ModelViewSet):
    serializer_class = BinSerializer
    queryset = Bin.objects.all()


class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
