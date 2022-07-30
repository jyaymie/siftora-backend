from django.urls import path, include
from siftora_app.views import (
    BinListApiView, BinDetailApiView, ProductListApiView, ProductDetailApiView
)

urlpatterns = [
    path('api/bins/', BinListApiView.as_view()),
    path('api/bins/<int:bin_id>/', BinDetailApiView.as_view()),
    path('api/products/', ProductListApiView.as_view()),
    path('api/products/<int:product_id>/', ProductDetailApiView.as_view()),
]
