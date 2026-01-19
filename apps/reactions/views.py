from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from apps.reactions.models import Reaction
from apps.products.models import Product
from .models import Liken Dislike

def reaction_like(self, pk):
	#Cargamos el formulario
	if request.method == 'POST':
    product = Product.objects.get(pk=pk)
    user = request.user
    #Comprueba si ya dio like
    ya_dio_like = Like.objects.filter(product=product,author=user).exists()
    #Comprueba si ya dio dislike
    ya_dio_dislike = Dislike.objects.filter(product=product,author=user).exists()

    if ya_dio_like:
        Like.objects.filter(product=product, author=user).delete()


    if ya_dio_dislike:
        Dislike.objects.filter(product=product, author=user).delete()

    # según el botón que apretó
    accion = request.POST.get('accion')

    if accion == 'like':
        Like.objects.create(product=product, author=user)

    elif accion == 'dislike':
        Dislike.objects.create(product=product, author=user)

