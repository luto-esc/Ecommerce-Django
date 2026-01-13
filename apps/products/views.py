from django.shortcuts import render
from .forms import CreateProductForm
from .models import Product, ProductImage
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.db.models import Prefetch

#-------------CREATE----------------
class ProductCreateView(CreateView):
    model = Product
    form_class = CreateProductForm
    template_name = "products/product_create.html"
    success_url = reverse_lazy('core:path_home')

    def form_valid(self, form):
        #form.save(commit=false) no impact in the db
        product = form.save(commit=False)
        #the object gets an id
        product.save()
        #images is from CreateProductForm(ProductForm):
        for img in form.cleaned_data["images"]:

        #--> .objects is a manager, the manager can know:
        #    create object, consult in the db, delete, filter
        #--> .create() is a shortcuts that does two things at once: build the object, saved in the db
        #receive the model fields as keyword arguments
        #->product = product: django use product.id for save the foreignkey
        #->images = img

            ProductImage.objects.create(
                product=product,
                images=img
            )

        return super().form_valid(form)


#-------------READ----------------
def productreadview(request):
    products = Product.objects.all()

    query = request.GET.get('name','')
    if query:
        products = products.filter(name__icontains=query)
    #products.prefetch_related --> method of queryset, it is suitable for 1-to-many and many-to-many relationships
    #run an query for product, run an extra query for all images
    #Prefetc --> it allow you to customize how prefetch is done
    #'images' --> the related_name of fk
    #queryset...--> define which images import, define how order them
    #to_attr --> put them in a new attribute called "prefetch_images"
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
        #-->"images" is from CreateProductForm(ProductForm):
        #use because .get it may not exist, return instead of an error
        #if the user doesn't upload any image, it would only be form.cleaned_data-> return error
        images = form.cleaned_data.get("images")
        #
        if images:
            #remove all current product images
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
