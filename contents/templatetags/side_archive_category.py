from django import template
from django.utils import timezone
from ..models import Article
from django.db.models import Count


register = template.Library()

@register.inclusion_tag('app1/includes/month_links.html')

def render_month_links():
    return {
        'dates': Article.objects.filter(created_at__lte=timezone.now()).dates('created_at', 'month', order='DESC'),
    }

