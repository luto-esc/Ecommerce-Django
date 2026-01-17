from django.db import models
from django.contrib.auth.models import User
from apps.products.models import Product

class ProductOpinion(models.Model):
    create_data = models.DateTimeField(auto_now_add = True)
    modification_data = models.DateTimeField(auto_now = True)
    text = models.TextField()
    author = models.ForeignKey(User, related_name='opinion', on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)

    def __str__(self):
        return self.create_data