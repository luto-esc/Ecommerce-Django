from django.shortcuts import render, get_object_or_404
from .forms import CreateProductForm
from .models import Product, ProductImage
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.db.models import Prefetch
from django.contrib.auth.models import User

#-------------CREATE----------------
class ProductCreateView(CreateView):
    model = Product
    form_class = CreateProductForm
    template_name = "products/product_create.html"
    success_url = reverse_lazy('core:path_home')

    def form_valid(self, form):
        #form.save(commit=false) no impacta en db todavia
        product = form.save(commit=False)
        #guardar el usuario creador
        product.user_author = self.request.user
        #impacta en la base de datos y obtiene un id
        product.save()
        #"images" es de CreateProductForm(ProductForm):
        for img in form.cleaned_data["images"]:

        # --> .objects es un manager; el manager sabe:
        #crear objetos, consultar la base de datos, eliminar y filtrar
        #--> .create() es un atajo que hace dos cosas a la vez:
        #crea el objeto y lo guarda en la base de datos
        #Recibe los campos del modelo como argumentos con nombre (keyword arguments)
        #-> product = product: Django usa product.id para guardar la ForeignKey
        #-> images = img

            ProductImage.objects.create(
                product=product,
                images=img
            )

        return super().form_valid(form)


#-------------READ----------------
def productreadview(request):
    products = Product.objects.all()

    query = request.GET.get('name','')
    price_min = request.GET.get('min_price')
    if query:
        products = products.filter(name__icontains=query)

    if price_min:
        #SELECT * FROM product WHERE price >= price_min
        products = products.filter(price__gte=price_min)

    #products.prefetch_related  # Método de QuerySet, es adecuado para relaciones uno-a-muchos y muchos-a-muchos
    # Ejecuta una consulta para Product y una consulta extra para todas las imágenes relacionadas
    # Prefetch --> permite personalizar cómo se realiza la precarga de datos
    # 'images' --> es el related_name de la ForeignKey
    # queryset --> define qué imágenes traer y cómo ordenarlas
    # to_attr --> guarda el resultado en un nuevo atributo llamado "prefetch_images"
    products = products.prefetch_related(Prefetch('images',queryset=ProductImage.objects.order_by('id'),to_attr='prefetched_images'))
    
    paginator = Paginator(products,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {}
    context["page_obj"] = page_obj
    context["query"] = query

    return render(request, 'products/products_list.html', context)


#-------------UPDATE---------------
class ProductUpdateView(UpdateView):
    model = Product
    form_class = CreateProductForm
    template_name = "products/product_update.html"
    success_url = reverse_lazy('products:path_products_list')

    def form_valid(self, form):
        product = form.save(commit=False)
        product.save()
        #--> "images" viene de CreateProductForm (ProductForm)
        #Se usa .get() porque puede no existir y devuelve None en lugar de lanzar un error
        #Si el usuario no sube ninguna imagen, usar form.cleaned_data["images"]
        images = form.cleaned_data.get("images")
        #
        if images:
            #Elimina todas las imágenes actuales del producto
            ProductImage.objects.filter(product=product).delete()

            for img in images:
                ProductImage.objects.create(
                    product=product,
                    images=img
                )
        return super().form_valid(form)


#-------------DELETE---------------
class ProductDeleteView(DeleteView):
    model = Product
    template_name = "products/product_delete.html"
    success_url = reverse_lazy('products:path_products_list')


#-------------DETAIL---------------
class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'


#-------------LIST MY PRODUCTS---------------
def listmyproducts(request, pk):
    #agarramos todo el usuario
    user_pk = request.user
    #agarramos especificamente la id o pk del usuario
    user_pk = user_pk.pk
    #agarramos los productos que sean tengan la pk igual a la del usuario
    products = Product.objects.filter(user_author_id = user_pk)
    
    query = request.GET.get('name','')
    if query:
        products = products.filter(name__icontains=query)
    
    products = products.prefetch_related(Prefetch('images',queryset=ProductImage.objects.order_by('id'),to_attr='prefetched_images'))

    paginator = Paginator(products,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {}
    context["page_obj"] = page_obj
    context["query"] = query

    return render(request,'products/products_bymyuser.html', context)


#-------------LIST PRODUCTS BY USER---------------
def listproductsbyuser(request, username):
    #agarramos el username del usuario
    profile_user = get_object_or_404(User, username = username)
    #agarramos los productos que tengan ese usuario
    products = Product.objects.filter(user_author = profile_user)

    query = request.GET.get('name','')
    if query:
        products = products.filter(name__icontains=query)
    
    products = products.prefetch_related(Prefetch('images',queryset=ProductImage.objects.order_by('id'),to_attr='prefetched_images'))

    paginator = Paginator(products,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {}
    context['profile_user'] = profile_user
    context["page_obj"] = page_obj
    context["query"] = query

    return render(request, 'products/products_byuser.html', context)