from django import template
register = template.Library()


@register.filter
def get_theme_path(theme):
    pass#return theme


@register.filter
def get_theme_name(theme):
    pass #return theme.name
