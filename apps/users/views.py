from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from apps.shopping_cart.models import ShoppingCart

class UserRegister(CreateView):
	template_name = 'users/user_register.html'
	form_class = UserRegisterForm
	success_url = reverse_lazy('users:path_login')

	def form_valid(self):
		user = form.save()
		ShoppingCart.objects.get_or_create(user=user)

		return super().form_valid(form)
