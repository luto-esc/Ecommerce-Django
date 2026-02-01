from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_image = models.ImageField(upload_to='profile_images', default='profile_images/default-profile-image.jpg', blank=False, null=False)
	bio = models.TextField(blank=True)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.user.username