from celery import shared_task

from django.core.mail import send_mail
from django.conf import settings
from django.apps import apps


@shared_task
def send_notification_email(subject, message, recipient_list):
    """Send notification email asynchronously / For multilingual sites"""
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        recipient_list,
        fail_silently=False,
    )


@shared_task
def update_view_count(model_name, object_id):
    """Update view count for a specific object"""
    model = apps.get_model('main', model_name)
    obj = model.objects.get(id=object_id)
    obj.view_count += 1
    obj.save()
