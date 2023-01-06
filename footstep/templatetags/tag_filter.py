from django import template

register = template.Library()

@register.filter #slice 템플릿 필터로 대체 가능
def list_index(list, index):
    return list[index]