from django import template

register = template.Library()

@register.filter
def root(key,value):
    return value.pop()