from django.contrib import admin
from .models import Article,Tag
from markdownx.admin import MarkdownxModelAdmin

admin.site.register(Article, MarkdownxModelAdmin)
admin.site.register(Tag)
