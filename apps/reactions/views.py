from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from apps.products.models import Product
from apps.opinions.models import ProductOpinion
from .models import Like, DisLike, OpinionLike, OpinionDisLike
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

#------------OPINION REACTION---------
@login_required
def opinion_reaction(request, pk):
    #Cargamos el formulario
    if request.method == 'POST':
        #Tomamos la opinion
        opinion = ProductOpinion.objects.get(pk=pk)
        product = opinion.product
        product_pk = product.pk

        #Tomamos el usuario
        user = request.user

        #Según el botón que apretó
        action = request.POST.get('action')

        #Comprueba si existe en la tabla
        have_like = OpinionLike.objects.filter(opinion=opinion,author=user).exists()
        have_dislike = OpinionDisLike.objects.filter(opinion=opinion,author=user).exists()

        #Si el input es like
        if action == 'like':

            #Si existe en la tabla dislike lo elimina
            if have_dislike:
                OpinionDisLike.objects.filter(opinion=opinion,author=user).delete()

            #Si existe en la tabla like
            if have_like:
                OpinionLike.objects.filter(opinion=opinion,author=user).delete()
            else:
                #Si no lo crea
                OpinionLike.objects.create(opinion=opinion, author=user)
         
         #Si el input es dislike    
        elif action == 'dislike':
            
            #Si existe en la tabla like lo elimina
            if have_like:
                OpinionLike.objects.filter(opinion=opinion,author=user).delete()

            #Si existe en la tabla dislike lo elimina
            if have_dislike:
                OpinionDisLike.objects.filter(opinion=opinion,author=user).delete()
            else:
                #Sino lo crea
                OpinionDisLike.objects.create(opinion=opinion, author=user)

    return HttpResponseRedirect(reverse_lazy('products:path_product_detail', kwargs = {'pk':product_pk}))