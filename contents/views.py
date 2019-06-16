from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article, Tag
from .forms import ArticleForm, TagForm


# Create your views here.
class Hello(View):

    def get(self, request):
        context = {"message": "helloWorld"}
        return TemplateResponse(request, "./hello.html", context)


hello = Hello.as_view()


class Main(ListView):
    model = Article
    template_name = "app1/main_list.html"
    print(1)

    paginate_by = 3

    def get_context_data(self,**kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        print(1)
        if self.request.GET.get('keyword') is not None:#アクセスしたURLにパラーメターがあれば分岐
            search_keyword = self.request.GET.get('keyword')
            context['search_keyword'] = search_keyword
            if search_keyword:
                article_list = Article.objects.filter(text__contains=search_keyword)
                context["article_list"]=article_list#フィルタした結果を辞書型としてcontextに追加
                print(context)
                return context
        else:
            print(2)
            queryset=super(ListView, self).get_context_data(**kwargs)
            print(queryset)
            return queryset

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


# class Search(ListView):
#     model =Article
#     template_name = "app1/main_list.html"


class Create(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "app1/create_list.html"
    success_url = reverse_lazy("contents:main")


create = Create.as_view()


class Detail(DetailView):
    model = Article
    template_name = "app1/detail.html"


detail = Detail.as_view()


class Update(UpdateView):
    model = Article
    template_name = "app1/create_list.html"
    form_class = ArticleForm
    success_url = reverse_lazy('contents:main')


update = Update.as_view()


class Delete(DeleteView):
    model = Article
    template_name = "app1/delete_list.html"
    form_class = ArticleForm
    success_url = reverse_lazy('contents:main')


class TagCreate(CreateView):
    model = Article
    form_class = TagForm
    template_name = "app1/tag_form.html"
    success_url = reverse_lazy('contents:main')


tagcreate = TagCreate.as_view()


class TagView(ListView):
    model = Article
    form_class = TagForm
    template_name = "app1/tag_view.html"

    def get_queryset(self):
        queryset = Article.objects.all().filter(tag__pk=self.kwargs['pk'])
        return queryset


tagview = TagView.as_view()
