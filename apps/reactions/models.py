from django.db import models
from django.contrib.auth.models import User
from apps.products.models import Product

class Reaction(models.Model):
	author = models.Foreingkey(User, on_delete=models.CASCADE)
	like = models.IntegerField(default=0)
	dislike = models.IntegerField(default=0)

class Like(models.Model):
	count_likes = 0
	author = models.Foreingkey(User, on_delete=models.CASCADE)
	product = models.Foreingkey(Product, related_name='like', on_delete=models.CASCADE)


	class Meta:
        unique_together = ('author', 'product')

class DisLike(models.Model):
	count_dislikes = 0		
	author = models.Foreingkey(User, on_delete=models.CASCADE)
	product = models.Foreingkey(Product, related_name='dislike', on_delete=models.CASCADE)

	class Meta:
    	unique_together = ('author', 'product')
