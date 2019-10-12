from django import template

register = template.Library()

@register.filter(name='replace')
def replace(str, replace):
    return str.replace(replace, "")