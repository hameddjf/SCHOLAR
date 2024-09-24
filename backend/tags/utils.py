from django.utils.text import slugify
from unidecode import unidecode


def unique_slugify(instance, value, slug_field_name='slug', queryset=None):
    """Generate a unique slug"""
    slug = slugify(unidecode(value))
    if queryset is None:
        queryset = instance.__class__._default_manager.all()
    slug_field = instance._meta.get_field(slug_field_name)
    slug = slug_field.slug_generator(slug, queryset)
    setattr(instance, slug_field.attname, slug)
