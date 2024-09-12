from django.utils.deprecation import MiddlewareMixin
from django.utils.translation import activate


class LanguageMiddleware(MiddlewareMixin):
    """Set default language in session if not set"""

    def process_request(self, request):
        language = request.session.get('django_language', 'fa')
        activate(language)


class ViewCountMiddleware(MiddlewareMixin):
    """Count views for authenticated users"""

    def process_response(self, request, response):
        if request.user.is_authenticated and response.status_code == 200:
            from .tasks import update_view_count
            if 'object' in response.context_data:
                obj = response.context_data['object']
                update_view_count.delay(obj.__class__.__name__, obj.id)
        return response
