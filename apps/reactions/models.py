from django.db import models
from django.contrib.auth.models import User
from apps.products.models import Product
from apps.opinions.models import ProductOpinion

#-----------PRODUCT LIKE-----------------
class Like(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, related_name='like', on_delete=models.CASCADE)

	class Meta:
		unique_together = ('author', 'product')

#-----------PRODUCT DISLIKE---------------
class DisLike(models.Model):	
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, related_name='dislike', on_delete=models.CASCADE)

	class Meta:
		unique_together = ('author', 'product')

#------------OPINION LIKE-----------------
class OpinionLike(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	opinion = models.ForeignKey(ProductOpinion, related_name='like', on_delete=models.CASCADE)

	class Meta:
		unique_together = ('author', 'opinion')

#-------------OPINION DISLIKE--------------
class OpinionDisLike(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	opinion = models.ForeignKey(ProductOpinion, related_name='dislike', on_delete=models.CASCADE)

	class Meta:
		unique_together = ('author', 'opinion')

