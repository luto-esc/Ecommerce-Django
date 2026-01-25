from django.db import models
from apps.products.models import Product
from django.contrib.auth.models import User


class ShoppingCart(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	products = models.ManyToManyField(Product, blank=True)

	def __str__(self):
		return f"Shopping Cart of {self.user.username}"
