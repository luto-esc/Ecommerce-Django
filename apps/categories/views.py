from django.shortcuts import render
from .forms import CreateProductForm
from .models import Product, ProductImage
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.db.models import Prefetch