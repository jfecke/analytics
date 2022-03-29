from django import template

register = template.Library()

@register.filter(name='cut2')
def cut2(value,arg):
    # cuts all values of arg from value
    return value.replace(arg,'')
