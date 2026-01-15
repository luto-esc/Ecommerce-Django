from django.urls import path
from . import views
from django.contrib.auth import views as auth

app_name = 'users'

urlpatterns = [
    path('login/', auth.LoginView.as_view(template_name = 'users/user_login.html'), name = 'path_login'),
    
    path('logout/', auth.LogoutView.as_view(), name = 'path_logout'),
    
    path('register/', views.UserRegister.as_view(), name = 'path_register'),
]