from django import template
import datetime

register = template.Library()

@register.simple_tag
def current_date():
    x = datetime.date.today()
    return x.strftime("%d/%m/%Y")

@register.filter
def get_type(value):
    return type(value)

@register.filter
def to_str(value):
    return type(value)


@register.filter
def change_date_format(value):
    return value.strftime("%d/%m/%Y")

@register.filter
def compare_date(value):
    a = datetime.date.today()
    if a == value:
        return True
    else:
        return False