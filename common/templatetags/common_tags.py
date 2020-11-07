from django import template
register = template.Library()


@register.filter
def get_theme_path(theme):
    return theme.path


@register.filter
def get_theme_name(theme):
    return theme.name
