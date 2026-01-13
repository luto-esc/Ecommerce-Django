from django.urls import path, include
from . import views

app_name = 'products'

urlpatterns = [
    path('product_create/', views.ProductCreateView.as_view(), name = 'path_product_create'),

    path('product_list/', views.productreadview, name = 'path_products_list'),

    path('product_update/<int:pk>', views.ProductUpdateView.as_view(), name = 'path_product_update'),

    path('product_delete/<int:pk>', views.ProductDeleteView.as_view(), name = 'path_product_delete'),

    path('product_detail/<int:pk>', views.ProductDetailView.as_view(), name = 'path_product_detail'),
]