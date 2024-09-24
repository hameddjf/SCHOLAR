from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Category, Tag
from .utils import unique_slugify


@receiver(pre_save, sender=Category)
@receiver(pre_save, sender=Tag)
def create_slug(sender, instance, *args, **kwargs):
    """Create slug for Category and Tag instances"""
    if not instance.slug:
        unique_slugify(instance, instance.name)
