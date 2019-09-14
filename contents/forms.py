from django import forms
from markdownx.widgets import MarkdownxWidget
from .models import Article, Tag
from django.contrib.auth.forms import UserCreationForm


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title','text','tag','photo',)
        widgets = {            # 'text': forms.Textarea(attrs={'rows':5, 'cols':8}),
            'title': forms.TextInput(attrs={"placeholder":"タイトル"}),
            'text': MarkdownxWidget(attrs={'class': 'textarea','rows': 7, 'cols': 22, 'style': 'resize:none;'}),

                  }

class LoginForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username","email")

