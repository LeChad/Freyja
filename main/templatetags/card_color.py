from django import template
import random
register = template.Library()


@register.simple_tag
def random_color():
    colors = ['info', 'warning', 'royal', 'success', 'primary', 'danger']
    return colors[random.randint(0, len(colors) - 1)]
