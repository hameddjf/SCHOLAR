from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def truncate_chars(value, max_length):
    """Truncate a string to a specified length"""
    if len(value) > max_length:
        truncd_val = value[:max_length]
        if len(value) > max_length + 1 and value[max_length] != " ":
            truncd_val = truncd_val[:truncd_val.rfind(" ")]
        return truncd_val + "..."
    return value


@register.simple_tag
def get_verbose_name(instance, field_name):
    """
    Returns verbose_name for a field.
    """
    return instance._meta.get_field(field_name).verbose_name.title()


@register.filter
def addclass(field, css_class):
    """Add a CSS class to a form field"""
    return field.as_widget(attrs={"class": css_class})


@register.filter(is_safe=True)
def highlight_search(text, search):
    """Highlight search terms in text"""
    highlighted = text.replace(
        search, '<span class="highlight">{}</span>'.format(search))
    return mark_safe(highlighted)
