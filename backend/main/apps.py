from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    verbose_name = _('برنامه اصلی')

    def ready(self):
        import main.signals
