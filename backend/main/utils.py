import re

from django.utils.text import slugify as django_slugify

from urllib.parse import quote


def custom_slugify(value):
    """Create a custom slug from the given value, preserving Persian characters"""
    value = re.sub(r'[^\w\s\-ء-ی]', '', value).strip().lower()
    value = re.sub(r'[\s\-]+', '-', value)
    return quote(value)


def get_client_ip(request):
    """Get the client's IP address from the HTTP request"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
