from django import template
from app.models import AddCategory, Category, Article
from app.forms import SubscribeForm
import random

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


@register.simple_tag
def get_subscribe_form():
    form = SubscribeForm()
    return form


@register.simple_tag
def get_random_add():
    try:
        random_add = random.sample(list(Article.objects.filter(add=True)), 1)
    except:
        random_add = None
    return random_add


@register.simple_tag
def get_random_article():
    try:
        counts = len(Article.objects.all())
        if counts > 3:
            counts = 3
        random_article = random.sample(list(Article.objects.all()), counts)
    except:
        random_article = None
    return random_article


@register.simple_tag
def get_random_article_10():
    try:
        counts = len(Article.objects.all())
        if counts > 10:
            counts = 10
        random_article = random.sample(list(Article.objects.all()), counts)
    except:
        random_article = None
    return random_article


@register.simple_tag
def get_slider_lg_basic_lens(obj):
    nums = range(1, 10)
    lens = 0
    for item in nums:
        field_name = 'slider_lg_basic_'+str(item)
        if getattr(obj, field_name):
            lens = lens + 1
    if lens > 8:
        return True
    else:
        return False



