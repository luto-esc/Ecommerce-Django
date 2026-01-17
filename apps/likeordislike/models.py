from django.db import models
from django.contrib.auth.models import User
from apps.products.models import Product

class ProductLikesOrDislikes(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
	likes = models.IntegerField(default=0)
	dislikes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.likes} {self.dislikes}"