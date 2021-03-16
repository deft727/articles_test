from django import template
from len_parfume.models import Article

register = template.Library()

@register.simple_tag()
def get_article(filter):
    pass
