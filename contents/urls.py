from django.urls import path
from . import views
from django.views.generic.dates import ArchiveIndexView

app_name = "contents"
urlpatterns =[
    path("hello", views.Hello.as_view(), name="hello"),
    path("main", views.Main.as_view(), name="main"),
    path("create", views.Create.as_view(), name="create"),
    path("detail/<int:pk>/", views.Detail.as_view(), name="detail"),
    path("update/<int:pk>/", views.Update.as_view(), name="update"),
    path("delete/<int:pk>", views.Delete.as_view(),name="delete"),
    path("tagcreate", views.TagCreate.as_view(), name="tagcreate"),
    path('tag/<int:pk>', views.TagView.as_view(), name='tagview'),#name='tagview'は、main_list.htmlの{% url 'contents:tagview' tag.pk %}">と対応
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.LogoutView.as_view(), name="logout"),
    path('<int:year>/<int:month>/', views.ArticleMonthArchive.as_view(), name='article_month_archive'),


]