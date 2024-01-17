from django import template

register = template.Library()

@register.filter(name='cents_to_dollars')
def cents_to_dollars(value):
    """Converts cents to dollars."""
    return "{:.2f}".format(float(value) / 100.0)