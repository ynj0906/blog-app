from .models import Article, Tag
from django.db.models import Count


def common(request):
    tag = Tag.objects.annotate(num_tags=Count('article'))
    context = {
        "tags":tag
    }
    return context