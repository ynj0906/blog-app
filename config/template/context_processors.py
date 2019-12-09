from contents.models import Article, Tag


def common(request):
    context = {
        "tags": Tag.objects.all(),
    }
    return context