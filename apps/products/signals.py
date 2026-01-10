from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import ProductImage

@receiver(post_delete, sender=ProductImage)
def delete_image_file(sender, instance, **kwargs):
    if instance.images:
        instance.images.delete(save=False)