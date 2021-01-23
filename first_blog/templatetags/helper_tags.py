from django import template
from pages.models import Page
from articles.models import Category

register = template.Library()


# header menu
@register.simple_tag()
def load_header_menu():
    return Page.objects.filter(is_active=True, show_top_position=True)[0:6]


# footer menu
@register.simple_tag()
def load_footer_menu():
    return Page.objects.filter(is_active=True, show_bottom_position=True)[0:6]


# sidebar category
@register.simple_tag()
def load_sidebar_category():
    return Category.objects.all()[0:6]
