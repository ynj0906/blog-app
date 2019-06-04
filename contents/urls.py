from django.urls import path
from . import views

app_name = "contents"
urlpatterns =[
    path("hello", views.Hello.as_view(), name="hello"),
    path("main",views.Main.as_view(), name="main"),
]