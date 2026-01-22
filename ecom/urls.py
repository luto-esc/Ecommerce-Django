from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('apps.core.urls')),

    path('products/', include('apps.products.urls')),

    path('users/', include('apps.users.urls')),

    path('ractions/', include('apps.reactions.urls')),

    path('opinions/', include('apps.opinions.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
