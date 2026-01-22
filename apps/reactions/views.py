from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from apps.products.models import Product
from .models import Like, DisLike
from django.contrib.auth.decorators import login_required

#------------PRODUCT REACTION---------
@login_required
def product_reaction(request, pk):
    #Cargamos el formulario
    if request.method == 'POST':
        #Tomamos el producto
        product = Product.objects.get(pk=pk)

        #Tomamos el usuario
        user = request.user

        #Según el botón que apretó
        action = request.POST.get('action')

        #Comprueba si existe en la tabla
        have_like = Like.objects.filter(product=product,author=user).exists()
        have_dislike = DisLike.objects.filter(product=product,author=user).exists()

        #Si el input es like
        if action == 'like':

            #Si existe en la tabla dislike lo elimina
            if have_dislike:
                DisLike.objects.filter(product=product,author=user).delete()

            #Si existe en la tabla like
            if have_like:
                Like.objects.filter(product=product,author=user).delete()
            else:
                #Si no lo crea
                Like.objects.create(product=product, author=user)
         
         #Si el input es dislike    
        elif action == 'dislike':
            
            #Si existe en la tabla like lo elimina
            if have_like:
                Like.objects.filter(product=product,author=user).delete()

            #Si existe en la tabla dislike lo elimina
            if have_dislike:
                DisLike.objects.filter(product=product,author=user).delete()
            else:
                #Sino lo crea
                DisLike.objects.create(product=product, author=user)

    return HttpResponseRedirect(reverse_lazy('products:path_product_detail', kwargs = {'pk':pk}))
