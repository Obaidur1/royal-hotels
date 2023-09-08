from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name="stars")
def stars(value):
    if value == 0:
        return "No reviews yet"
    star = "&#128970;" * value + " Ratings"
    return mark_safe(star)
