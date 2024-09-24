from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey


class Base(models.Model):
    """Base model for common fields"""
    name = models.CharField(_("Name"), max_length=50)
    slug = models.SlugField(_("Slug"), unique=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        abstract = True


class Category(MPTTModel, Base):
    """Category model with tree structure"""
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})


class Tag(Base):
    """Tag model"""

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tag_detail", kwargs={"slug": self.slug})
