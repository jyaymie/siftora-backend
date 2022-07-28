from rest_framework import viewsets
from .models import Bin, Product
from .serializers import BinSerializer, ProductSerializer


class BinViewSet(viewsets.ModelViewSet):
    serializer_class = BinSerializer
    queryset = Bin.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
