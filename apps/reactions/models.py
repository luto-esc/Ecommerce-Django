from django.db import models
from django.contrib.auth.models import User
from apps.products.models import Product

class Like(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, related_name='like', on_delete=models.CASCADE)

	class Meta:
		unique_together = ('author', 'product')

class DisLike(models.Model):	
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, related_name='dislike', on_delete=models.CASCADE)

	class Meta:
		unique_together = ('author', 'product')
