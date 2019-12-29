from django import template
from ..models import Article


register = template.Library()


@register.filter
def article_count(x):
    counts= Article.objects.filter(created_at__contains="-"+str(x)+"-").count()
    return counts

