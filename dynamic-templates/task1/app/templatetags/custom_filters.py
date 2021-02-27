from django import template

register = template.Library()


@register.filter
def get_value(dictionary, key):
    return dictionary[key]


@register.filter
def make_float(value):
    try:
        result = float(value)
    except ValueError:
        result = value
    return result
