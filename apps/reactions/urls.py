from django.urls import path
from . import views

app_name = 'reactions'

urlpatterns = [
    path('reactions/<int:pk>', views.pruduct_reaction(), name = 'path_product_reaction'),

]