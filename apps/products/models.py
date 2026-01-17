from django.db import models
from django.contrib.auth.models import User
from apps.categories.models import ProductCategory



class Product(models.Model):
	
	name = models.CharField(max_length = 180)
	description = models.TextField(default = None)
	price = models.DecimalField(max_digits = 8, decimal_places=2)
	cost_price = models.DecimalField(max_digits = 8, decimal_places=2)
	stock = models.PositiveIntegerField()
	user_author = models.ForeignKey(User, on_delete=models.CASCADE)
	create_date = models.DateTimeField(auto_now_add = True)
	category = models.ForeignKey(ProductCategory, related_name='categories', on_delete=models.CASCADE)


	def __str__(self):
		return self.name
	
	def myOpinions(self):
		return self.opinion_set.all()
	

	
class ProductImage(models.Model):
    product = models.ForeignKey(Product,related_name="images",on_delete=models.CASCADE)
    images = models.ImageField(upload_to = 'products_images', blank=True, null=True)

    def __str__(self):
    	return f"Image from {self.product.name}"

