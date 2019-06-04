from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView

# Create your views here.
class Hello(View):

    def get(self,request):
        context = {"message": "helloWorld"}
        return TemplateResponse(request, "./hello.html", context)


hello = Hello.as_view()


class Main(TemplateView):
    template_name = "app1/main_list.html"

# class Sample(ListView):
#     model = Initial
#     template_name = "app1/sample_list.html"
#     #context_object_name = "sample_list"
#     def get_queryset(self,*args):
#         #a = Initial.objects.all()
#         #a = Initial.objects.filter(detail__detail="男前"
#         #a = Initial.objects.values_list('initial', flat=True)
#         a=Initial.objects.filter(id__regex=r'\w*')
#         return a
#
#
#
# sample_list = Sample.as_view()