from django import template
from app.models import AddCategory, Category
register = template.Library()


@register.simple_tag
def get_field(model, field):
    return getattr(model, field)


@register.simple_tag
def get_array(array, index):
    return array[index]


@register.simple_tag
def get_add_category():
    return AddCategory.objects.all()


