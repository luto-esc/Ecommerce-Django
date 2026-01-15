from django.db import models
from django.contrib.auth.models import User
from apps.categories.models import ProductCategory


class Product(models.Model):
	
	name = models.CharField(max_length = 180)
	description = models.TextField(default = None)
	price = models.DecimalField(max_digits = 8, decimal_places=2)
	cost_price = models.DecimalField(max_digits = 8, decimal_places=2)
	stock = models.PositiveIntegerField()
	#author = models.ForeignKey(User, on_delete=models.CASCADE)
	# date_create = models.DateTimeField(auto_now_add=True)

	
	def __str__(self):
		return self.name
	
class ProductImage(models.Model):
    product = models.ForeignKey(Product,related_name="images",on_delete=models.CASCADE)
    images = models.ImageField(upload_to = 'products_images', blank=True, null=True)

    def __str__(self):
    	return f"Image from {self.product.name}"

