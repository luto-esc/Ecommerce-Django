from django.db import models

class ProductCategory(models.Model):

	name = models.CharField(max_length = 180)
	description = models.TextField(default = None)

	def __str__(self):
		return self.name


class Product(models.Model):
	
	name = models.CharField(max_length = 180)
	description = models.TextField(default = None)
	price = models.DecimalField(max_digits = 8, decimal_places=2)
	cost_price = models.DecimalField(max_digits = 8, decimal_places=2)
	stock = models.PositiveIntegerField()

	
	def __str__(self):
		return self.name
	
class ProductImage(models.Model):
    product = models.ForeignKey(Product,related_name="images",on_delete=models.CASCADE)
    images = models.ImageField(upload_to = 'products_images', blank=True, null=True)

    def __str__(self):
    	return f"Image from {self.product.name}"

