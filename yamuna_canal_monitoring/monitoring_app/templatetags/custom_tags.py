import ast
from django import template
register = template.Library()


@register.filter
def make_dict(val):
    return ast.literal_eval(val)