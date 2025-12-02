from django.conf import settings


def theme_context(request):
    theme_name = request.session.get('theme', settings.DEFAULT_THEME)

    return {
        'theme': settings.THEMES.get(theme_name, settings.THEMES[settings.DEFAULT_THEME]),
        'theme_name': theme_name,
        'available_themes': settings.THEMES,
        'DEFAULT_THEME': settings.DEFAULT_THEME,
    }