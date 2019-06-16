from django import forms
from .models import Article, Tag


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
