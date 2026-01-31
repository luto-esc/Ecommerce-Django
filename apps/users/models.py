from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, one_delete=models.CASCADE)
	profile_image = models.ImageField(upload_to='profiles_images', blank=False, null=False)

	def __str__(self):
		return self.user.username