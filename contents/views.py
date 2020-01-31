from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse

from django.urls import reverse
from django.urls import reverse_lazy
from django.shortcuts import redirect, resolve_url

from .models import Article, Tag
from .forms import ArticleForm, TagForm,LoginForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.views import (LoginView, LogoutView)
from django.views.generic.dates import ArchiveIndexView,MonthArchiveView


# Create your views here.

#確認用
class Hello(View):
    def get(self, request):
        context = {"message": "helloWorld","message2":"goodbyworld","message3":"againworld"}
        # return TemplateResponse(request, "./hello.html", context)
        return JsonResponse(context)

hello = Hello.as_view()

class Sample(ListView, PermissionRequiredMixin):
    model = Tag
    # queryset=Article.objects.all().order_by("-created_at")#表示を新しい順に
    template_name = "app1/ajax_test.html"

def ajax_post_add(request):
    names = request.POST.get('name')
    post = Tag.objects.create(name=names)
    d = {
        'name': post.name,
    }
    return JsonResponse(d)

# ログイン
class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    success_url = reverse_lazy("contents:main")
    template_name = 'app1/login.html'

login = Login.as_view()

# ページネーション
def paginate_queryset(request, queryset, count):
    """Pageオブジェクトを返す。

    ページングしたい場合に利用してください。

    countは、1ページに表示する件数です。
    返却するPgaeオブジェクトは、以下のような感じで使えます。

        {% if page_obj.has_previous %}
          <a href="?page={{ page_obj.previous_page_number }}">Prev</a>
        {% endif %}

    また、page_obj.object_list で、count件数分の絞り込まれたquerysetが取得できます。

    """
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj

# メインメニュー
class Main(ListView, PermissionRequiredMixin):
    model = Article
    queryset=Article.objects.all().order_by("-created_at")#表示を新しい順に
    template_name = "app1/main_list.html"
    permission_required = ("contents.view_article", "contents.view_tag")
    
    def get_context_data(self,**kwargs):#検索時のメソッド
        self.paginate_by = 1
        context = super(ListView, self).get_context_data(**kwargs)

        if self.request.GET.get('keyword') is not None:  # アクセスしたURLにパラーメターがあれば分岐
            search_keyword = self.request.GET.get('keyword')
            context['search_keyword'] = search_keyword
            article_list = Article.objects.filter(text__contains=search_keyword).order_by("-created_at")
            page_obj = paginate_queryset(self.request, article_list, 3)#別に登録したpaginate_queryset関数を使ってる
            context["article_list"] = page_obj.object_list  # フィルタした結果を辞書型としてcontextに追加
            context["page_obj"] = page_obj
            return context
        else:
            self.paginate_by = 6
            context = super(ListView, self).get_context_data(**kwargs)
            return context
            # return Article.objects.all()#パラメータがなければ全件取得

    #
    # def get_context_data(self):
    #     if self.request.GET.get('keyword') is not None:#アクセスしたURLにパラーメターがあれば分岐
    #         search_keyword = self.request.GET.get('keyword')
    #         if search_keyword:
    #             queryset = Article.objects.filter(text__contains=search_keyword)
    #             print(search_keyword)
    #             print(queryset)
    #             return queryset
    #     else:
    #         return Article.objects.all()#パラメータがなければ全件取得

main = Main.as_view()


# 記事新規作成
class Create(CreateView,PermissionRequiredMixin):
    model = Article
    form_class = ArticleForm
    template_name = "app1/create_list.html"
    permission_required = ("contents.add_article", "contents.add_tag")
    raise_exception = True
    success_url = reverse_lazy("contents:main")

create = Create.as_view()

# 記事詳細
class Detail(DetailView,PermissionRequiredMixin):
    model = Article
    template_name = "app1/detail_list.html"
    permission_required = ("contents.add_article", "contents.add_tag")
    
detail = Detail.as_view()


# 記事更新
class Update(UpdateView,PermissionRequiredMixin):
    model = Article
    template_name = "app1/create_list.html"
    form_class = ArticleForm
    permission_required =("contents.add_article", "contents.add_tag")
    
    #
    def get_success_url(self):
        return reverse('contents:detail', kwargs={'pk': self.object.pk})

update = Update.as_view()

# 記事削除
class Delete(DeleteView,PermissionRequiredMixin):
    model = Article
    template_name = "app1/delete_list.html"
    form_class = ArticleForm
    permission_required = ("contents.add_article", "contents.add_tag")
    success_url = reverse_lazy('contents:main')


class TagAll(ListView):
    model=Tag
    template_name = "app1/tag_all.html"

tagall = TagAll.as_view()

# タグ作成
class TagCreate(CreateView, PermissionRequiredMixin):
    model = Tag
    form_class = TagForm
    template_name = "app1/tag_form.html"
    permission_required = ("contents.add_article", "contents.add_tag")
    # success_url = reverse_lazy('contents:update/<int(pk)>')
    
    #失敗作、このままだとタグのpkが取得される、detailのpkをとってきたい。
    def get_success_url(self):
        # context = super().get_context_data(**kwargs)
        return reverse('contents:detail', kwargs={'pk': self.object.pk})
    
tagcreate = TagCreate.as_view()

# タグ表示
class TagView(ListView,PermissionRequiredMixin):
    paginate_by = 3
    model = Tag
    form_class = TagForm
    
    permission_required = ("contents.add_article", "contents.add_tag")
    template_name = "app1/tag_view.html"
   
    # def get_queryset(self):
    #     queryset = Article.objects.all().filter(tag__pk=self.kwargs['pk'])
    #     print(queryset)
    #     return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        propertyinfo = Tag.objects.get(id=self.kwargs['pk'])
        context["propertyinfo"]=propertyinfo
        article_list=Article.objects.all().filter(tag__pk=self.kwargs['pk'])
        page_obj = paginate_queryset(self.request, article_list, 3)
        context["article_list"] = page_obj.object_list
        context["page_obj"] = page_obj
        print(context)
        return context


        # search_keyword = self.request.GET.get('keyword')
        #     context['search_keyword'] = search_keyword
        #     article_list = Article.objects.filter(text__contains=search_keyword).order_by("-created_at")
        #     page_obj = paginate_queryset(self.request, article_list, 3)#別に登録したpaginate_queryset関数を使ってる
        #     context["article_list"] = page_obj.object_list  # フィルタした結果を辞書型としてcontextに追加
        #     context["page_obj"] = page_obj
        #     return context
    
tagview = TagView.as_view()

#タグ削除
class TagDelete(DeleteView):
    model=Tag
    template_name = "app1/delete_list.html"
    success_url = reverse_lazy('contents:main')


tagdelete = TagDelete.as_view()


# 月別アーカイブ
class ArticleMonthArchive(MonthArchiveView):
    model = Article
    template_name = "app1/article_archive.html"
    date_field = 'created_at'
    make_object_list = True
    month_format='%m'