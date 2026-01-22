from django.shortcuts import render, HttpResponseRedirect
from .models import ProductOpinion
from apps.products.models import Product
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required

#-----------CREATE-------------
@login_required
def productopinioncreateview(request, pk):
	
	product = Product.objects.get(pk = pk)
	user = request.user

	opinion = request.POST.get('text_comment', None)

	ProductOpinion.objects.create(text = opinion, author = user, product = product)

	return HttpResponseRedirect(reverse_lazy('products:path_product_detail', kwargs = {'pk':pk}))

#-----------DELETE-------------
class ProductOpinionDeleteView(DeleteView):
	model = ProductOpinion
	template_name = 'opinions/opinion_delete.html'

	def get_success_url(self):
		return reverse_lazy('products:path_product_detail', kwargs={'pk':self.object.product.pk})