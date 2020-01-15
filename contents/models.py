from django.db import models
from markdownx.models import MarkdownxField
# Create your models here.


class Tag(models.Model):
    """ タグ """
    name = models.CharField(
        verbose_name="タグ名",
        max_length=255)

    created_at = models.DateTimeField(
        auto_now_add=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    """記事"""

    title = models.CharField(
        verbose_name="タイトル",
        max_length=255)

    # text = models.TextField(
    #     verbose_name="本文",)

    text = MarkdownxField('本文', help_text='Markdown形式で書いてください。')

    tag = models.ManyToManyField(
        Tag,
        verbose_name="たぐ",
        blank=True)

    photo = models.ImageField(
        verbose_name="フォト",
        blank=True,
        null=True,
        upload_to="photo/%Y%m%d",)

    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True)

    updated_at = models.DateTimeField(
        verbose_name='更新日',
        auto_now=True)

    def __str__(self):
        return self.title