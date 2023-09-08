from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name="stars")
def stars(value):
    star = "&#128970;" * value
    return mark_safe(star)
