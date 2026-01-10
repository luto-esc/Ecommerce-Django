from django.shortcuts import render
from .forms import CreateProductForm
from .models import Product, ProductImage
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator

#-------------CREATE----------------
class ProductCreateView(CreateView):
    model = Product
    form_class = CreateProductForm
    template_name = "products/product_create.html"
    success_url = reverse_lazy('core:path_home')

    def form_valid(self, form):
        product = form.save(commit=False)
        product.save()

        for img in form.cleaned_data["images"]:
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

        images = form.cleaned_data.get("images")

        if images:
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
