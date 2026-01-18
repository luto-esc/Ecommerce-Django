from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from apps.reactions.models import Reaction
from apps.products.models import Product

def reaction(self, pk):
	product = Product.objects.get(pk = pk)
	author = request.user

	reaction = request.POST.get('react', None)