from django.db import models
from django.contrib.auth.models import User
from apps.categories.models import ProductCategory

class Reaction(models.Model):
	author = models.Foreingkey(User, on_delete=models.CASCADE)
	like = models.IntegerField(default=0)
	dislike = models.IntegerField(default=0)