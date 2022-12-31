from django import template

register = template.Library()

@register.filter
def list_index(list, index):
    return list[index]