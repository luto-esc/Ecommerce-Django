from django.urls import path
from . import views

app_name = 'opinions'

urlpatterns = [
	path('opinion/<int:pk>', views.productopinioncreateview, name='path_opinion_create'),

	path('opinion_delete/<int:pk>', views.ProductOpinionDeleteView.as_view(), name='path_opinion_delete')
]