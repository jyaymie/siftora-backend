from django.urls import path
from . import views

urlpatterns = [
    path('api/signup/', views.SignupView.as_view(), name='signup'),
    path('api/login/', views.LoginView.as_view(), name='login'),
    path('api/logout/', views.LogoutView.as_view(), name='logout'),
    path('api/bins/', views.BinListApiView.as_view(), name='bin_list'),
    path('api/bins/<int:bin_id>/',
         views.BinDetailApiView.as_view(), name='bin_detail'),
    path('api/products/', views.ProductListApiView.as_view(), name='product_list'),
    path('api/products/<int:product_id>/',
         views.ProductDetailApiView.as_view(), name='product_detail'),
]
