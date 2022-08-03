from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Bin, Product
from .serializers import BinSerializer, ProductSerializer


# Authentication help from https://testdriven.io/blog/django-spa-auth/#django-drf-frontend-served-separately-same-domain

# =============================================================== AUTHENTICATION
class CSRFView(APIView):
    def get_csrf(request):
        response = JsonResponse({'detail': 'CSRF cookie set'})
        response['X-CSRFToken'] = get_token(request)
        return response


class SignupView(APIView):
    def post(self, request, format=None):
        data = {
            'username': request.data.get('username'),
            'password': request.data.get('password'),
        }

        user = User.objects.create_user(request.data.get('username'),
                                        'user@email.com',
                                        request.data.get('password'))

        return Response(data)


class SigninView(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return JsonResponse({'detail': 'Please provide username and password.'}, status=400)

        user = authenticate(username=username, password=password)

        if user is None:
            return JsonResponse({'detail': 'Invalid credentials.'}, status=400)

        login(request, user)
        return JsonResponse({'detail': 'Successfully logged in.'})


class SignoutView(APIView):
    def post(self, request, format=None):
        # if not request.user.is_authenticated:
        #     return JsonResponse({'detail': 'You\'re not logged in.'}, status=400)
        logout(request)
        return JsonResponse({'detail': 'Successfully logged out.'})


# CRUD functionality help from https://blog.logrocket.com/django-rest-framework-create-api/#restful-structure-get-post-put-delete-methods


class BinListApiView(APIView):
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]

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
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated=]

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
                {"res": "Object with bin id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        query_params = request.query_params
        sort = query_params.get('sort')

        sorted_products = []
        if sort:
            sorted_products = bin_instance.products.all().order_by(sort)
        else:
            sorted_products = bin_instance.products.all()

        serializer = BinSerializer(bin_instance)

        data = {
            **serializer.data,
            "products": ProductSerializer(sorted_products, many=True).data,
        }

        return Response(data, status=status.HTTP_200_OK)

    # ========================================================= UPDATE BIN BY ID
    def put(self, request, bin_id, *args, **kwargs):
        bin_instance = self.get_object(bin_id)
        if not bin_instance:
            return Response(
                {"res": "Object with bin id does not exist"},
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
                {"res": "Object with bin id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        bin_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_204_NO_CONTENT
        )


class ProductListApiView(APIView):
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]

    # ==================================================== RETRIEVE ALL PRODUCTS
    def get(self, request, *args, **kwargs):
        query_params = request.query_params
        sort = query_params.get('sort')

        if sort:
            queryset = Product.objects.all().order_by(sort)
        else:
            queryset = Product.objects.all()

        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # ========================================================= CREATE A PRODUCT
    def post(self, request, *args, **kwargs):
        data = {
            'bins': request.data.get('bins', []),
            'brand': request.data.get('brand'),
            'name': request.data.get('name'),
            'shade': request.data.get('shade'),
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
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]

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
                {"res": "Object with product id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ProductSerializer(product_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # ===================================================== UPDATE PRODUCT BY ID
    def put(self, request, product_id, *args, **kwargs):
        product_instance = self.get_object(product_id)
        if not product_instance:
            return Response(
                {"res": "Object with product id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'brand': request.data.get('brand'),
            'name': request.data.get('name'),
            'shade': request.data.get('shade'),
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
                {"res": "Object with product id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        product_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_204_NO_CONTENT
        )


class SessionView(APIView):
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, format=None):
        return JsonResponse({'isAuthenticated': True})


class WhoAmIView(APIView):
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, format=None):
        return JsonResponse({
            'id': request.user.id,
            'username': request.user.username
        })
