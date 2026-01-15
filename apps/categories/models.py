from django.db import models

class ProductCategory(models.Model):

	name = models.CharField(max_length = 180)
	description = models.TextField(default = None)

	def __str__(self):
		return self.name

