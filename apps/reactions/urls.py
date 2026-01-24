from django.urls import path
from . import views

app_name = 'reactions'

urlpatterns = [
    path('reactions/<int:pk>', views.product_reaction, name = 'path_product_reaction'),

    path('opinion_reactions/<int:pk>', views.opinion_reaction, name = 'path_opinion_reaction'),
]