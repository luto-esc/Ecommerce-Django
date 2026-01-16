from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm

class UserRegister(CreateView):
	template_name = 'users/user_register.html'
	form_class = UserRegisterForm
	success_url = reverse_lazy('users:path_login')