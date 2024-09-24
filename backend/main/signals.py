from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from .models import Base


@receiver(pre_save, sender=Base)
def create_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
