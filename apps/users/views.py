from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserProfileUpdateForm
from apps.shopping_cart.models import ShoppingCart
from .models import Profile

class UserRegister(CreateView):
	template_name = 'users/user_register.html'
	form_class = UserRegisterForm
	success_url = reverse_lazy('users:path_login')
	
	def form_valid(self, form):
		user = form.save()
		Profile.objects.create(user=user)
		return super().form_valid(form)

def user_profile(request, username):
	# Agarramos el usuario con get_object_of_404 que busca en la tabla el valor que recibimos
	# Buscara en la tabla 'User' en la columna 'username'
	# el valor de 'username' que sea igual al que recibimos
	profile_user = get_object_or_404(User, username = username)
	
	# Agarramos los objetos de la tabla profiles en donde el user coincida con el user que recibimos
	# Ocupamos nuevamente get() por que es una relacion one_to_one
	profile = get_object_or_404(Profile, user=profile_user)
	context = {}
	context['profile'] = profile

	return render(request, 'users/user_profile.html', context)

class UserProfileUpdate(UpdateView):
	template_name = 'users/user_update_profile.html'
	form_class = UserProfileUpdateForm
	success_url = reverse_lazy('users:path_user_profile')