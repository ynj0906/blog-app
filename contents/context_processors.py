from .models import Article, Tag
from django.db.models import Count
from django.db.models.fields import DateField
from django.db.models.functions import TruncDate
from django.db.models.functions import Trunc,TruncYear,TruncMonth,TruncDate
from django.utils import timezone
import pytz

#タグに紐づく件数を取得
#annotate:参照先の

# melb = pytz.timezone('Asia/Tokyo')
def common(request):
    # melb = pytz.timezone('Asia/Tokyo')
    tag = Tag.objects.annotate(num_tags=Count('article'))
    # dates = Article.objects.annotate(num_date=TruncDate('created_at'))





    context = {
        "tags":tag,
        # "datess":dates,
    }
    return context