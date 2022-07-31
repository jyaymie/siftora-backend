from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Bin, Product
from .serializers import BinSerializer, ProductSerializer


class UserApiView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response(content)


class BinListApiView(APIView):
    # ======================================================== RETRIEVE ALL BINS
    def get(self, request, *args, **kwargs):
        bins = Bin.objects.all()
        serializer = BinSerializer(bins, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # ============================================================= CREATE A BIN
    def post(self, request, *args, **kwargs):
        data = {
            'title': request.data.get('title'),
            'products': request.data.get('products', []),
        }

        serializer = BinSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BinDetailApiView(APIView):
    # ======================================================= RETRIEVE BIN BY ID
    def get_object(self, bin_id):
        try:
            return Bin.objects.get(id=bin_id)
        except Bin.DoesNotExist:
            return None

    def get(self, request, bin_id, *args, **kwargs):
        bin_instance = self.get_object(bin_id)
        if not bin_instance:
            return Response(
                {"res": "Object with bin id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = BinSerializer(bin_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # ========================================================= UPDATE BIN BY ID
    def put(self, request, bin_id, *args, **kwargs):
        bin_instance = self.get_object(bin_id)
        if not bin_instance:
            return Response(
                {"res": "Object with bin id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'title': request.data.get('title'),
            'products': request.data.get('products'),
        }
        serializer = BinSerializer(
            instance=bin_instance, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ========================================================= DELETE BIN BY ID
    def delete(self, request, bin_id, *args, **kwargs):
        bin_instance = self.get_object(bin_id)
        if not bin_instance:
            return Response(
                {"res": "Object with bin id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        bin_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_204_NO_CONTENT
        )


class ProductListApiView(APIView):
    # ==================================================== RETRIEVE ALL PRODUCTS
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # ========================================================= CREATE A PRODUCT
    def post(self, request, *args, **kwargs):
        data = {
            'bins': request.data.get('bins', []),
            'brand': request.data.get('brand'),
            'name': request.data.get('name'),
            'shade': request.data.get('shade'),
            'finish': request.data.get('finish'),
            'purchase_date': request.data.get('purchase_date'),
            'price': request.data.get('price'),
            'open_date': request.data.get('open_date'),
            'expiry_date': request.data.get('expiry_date'),
            'use_count': request.data.get('use_count'),
            'finish_date': request.data.get('finish_date'),
            'will_repurchase': request.data.get('will_repurchase'),
            'notes': request.data.get('notes'),
        }

        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailApiView(APIView):
    # =================================================== RETRIEVE PRODUCT BY ID
    def get_object(self, product_id):
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return None

    def get(self, request, product_id, *args, **kwargs):
        product_instance = self.get_object(product_id)
        if not product_instance:
            return Response(
                {"res": "Object with product id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ProductSerializer(product_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # ===================================================== UPDATE PRODUCT BY ID
    def put(self, request, product_id, *args, **kwargs):
        product_instance = self.get_object(product_id)
        if not product_instance:
            return Response(
                {"res": "Object with product id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'brand': request.data.get('brand'),
            'name': request.data.get('name'),
            'shade': request.data.get('shade'),
            'finish': request.data.get('finish'),
            'purchase_date': request.data.get('purchase_date'),
            'price': request.data.get('price'),
            'open_date': request.data.get('open_date'),
            'expiry_date': request.data.get('expiry_date'),
            'use_count': request.data.get('use_count'),
            'finish_date': request.data.get('finish_date'),
            'will_repurchase': request.data.get('will_repurchase'),
            'notes': request.data.get('notes'),
        }
        serializer = ProductSerializer(
            instance=product_instance, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ===================================================== DELETE PRODUCT BY ID
    def delete(self, request, product_id, *args, **kwargs):
        product_instance = self.get_object(product_id)
        if not product_instance:
            return Response(
                {"res": "Object with product id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        product_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_204_NO_CONTENT
        )
