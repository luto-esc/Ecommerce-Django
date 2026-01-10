from django.urls import path, include
from . import views

app_name = 'products'

urlpatterns = [
    path('product_create/', views.ProductCreateView.as_view(), name = 'path_product_create'),

    path('product_list/', views.productreadview, name = 'path_product_list'),
]