from django.conf import settings


class ThemeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        theme_name = request.session.get('theme', settings.DEFAULT_THEME)

        if theme_name not in settings.THEMES:
            theme_name = settings.DEFAULT_THEME

        request.theme = settings.THEMES[theme_name]
        request.theme_name = theme_name

        response = self.get_response(request)
        return response