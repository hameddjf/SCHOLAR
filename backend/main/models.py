from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()


class Base(models.Model):
    title = models.CharField(_("عنوان"), max_length=200)
    content = models.TextField(_("محتوا"))
    slug = models.SlugField(_("اسلاگ"), unique=True, allow_unicode=True)

    category = models.ManyToManyField(
        "tags.Category", verbose_name=_("دسته‌بندی"), related_name="base_items")
    tags = models.ManyToManyField("tags.Tag", verbose_name=_(
        "برچسب‌ها"), related_name="base_items")
    user = models.ForeignKey(User, verbose_name=_(
        "کاربر"), on_delete=models.CASCADE, related_name="base_items")

    is_published = models.BooleanField(_("منتشر شده"), default=False)
    created_at = models.DateTimeField(_("تاریخ ایجاد"), auto_now_add=True)
    updated_at = models.DateTimeField(_("تاریخ به‌روزرسانی"), auto_now=True)

    view_count = models.PositiveIntegerField(_("تعداد بازدید"), default=0)
    like_count = models.PositiveIntegerField(_("تعداد لایک"), default=0)

    thumbnail = models.ImageField(
        _("تصویر شاخص"), upload_to="base_thumbnails/", blank=True, null=True)

    class Meta:
        abstract = True
        verbose_name = _("آیتم پایه")
        verbose_name_plural = _("آیتم‌های پایه")
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("base_detail", kwargs={"slug": self.slug})

    def increment_view_count(self):
        self.view_count += 1
        self.save()

    def like(self):
        self.like_count += 1
        self.save()
