from django import template
register = template.Library()

@register.filter(name="myfilter", is_safe=True, needs_autoescape=True)
def myfilter(value, autoescape=True):
    sentence = value.split(" - ")
    return sentence[1]