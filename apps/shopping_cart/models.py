from django.db import models
from apps.products.models import Product
from django.contrib.auth.models import User


class ShoppingCart(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Shopping Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, related_name='items' , on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"

