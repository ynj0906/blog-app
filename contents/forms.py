from django import forms
from .models import Article, Tag
from django.contrib.auth.forms import UserCreationForm


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title','text','tag',)
        widgets = {
                    'text': forms.Textarea(attrs={'rows':4}),

                  }

class LoginForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username","email")

