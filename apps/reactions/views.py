from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from apps.products.models import Product
from .models import Like, DisLike
from django.contrib.auth.decorators import login_required

@login_required
#------------PRODUCT REACTION---------
def product_reaction(request, pk):
    # Cargamos el formulario
    if request.method == 'POST':
        # Tomamos el producto
        product = Product.objects.get(pk=pk)

        # Tomamos el usuario
        user = request.user
    
        #Comprueba si el usuario existe en la tabla y dio like a ese producto
        have_like = Like.objects.filter(product=product,author=user).exists()
    
        #Comprueba si el usuario existe en la tabla y ya dio like a ese producto
        have_dislike = DisLike.objects.filter(product=product,author=user).exists()

        #Si ya_dio_like --> = True, osea que el usuario ya habia dado like, elimina su registro de la tabla
        if have_like:
            Like.objects.filter(product=product, author=user).delete()

        #Si ya_dio_dislike --> = False, osea que el usuario ya habia dado dislike, elimina su registro de la tabla
        if have_dislike:
            DisLike.objects.filter(product=product, author=user).delete()

        # según el botón que apretó
        action = request.POST.get('action')

        #Si el input es like, se crea un fila en la tabla like
        if action == 'like':
            Like.objects.create(product=product, author=user)
        #Si el input es dislike, se crea una fila en la tabla dislike
        elif action == 'dislike':
            DisLike.objects.create(product=product, author=user)

    return HttpResponseRedirect(reverse_lazy('products:path_product_detail', kwargs = {'pk':pk}))
