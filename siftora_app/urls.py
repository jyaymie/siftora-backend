from django.urls import path, include
from . import views

urlpatterns = [
    path('api/bins/', views.BinListApiView.as_view(), name='bin_list'),
    path('api/bins/<int:bin_id>/',
         views.BinDetailApiView.as_view(), name='bin_detail'),
    path('api/products/', views.ProductListApiView.as_view(), name='product_list'),
    path('api/products/<int:product_id>/',
         views.ProductDetailApiView.as_view(), name='product_detail'),
]
