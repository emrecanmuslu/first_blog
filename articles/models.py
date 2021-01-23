from django.db import models
from django.contrib.auth.models import User
from cropperjs.models import CropperImageField
from ckeditor.fields import RichTextField
from django.shortcuts import reverse


class Category(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
        max_length=50,
        verbose_name='İsim'
    )
    slug = models.SlugField(
        null=False,
        blank=False,
        unique=True,
        verbose_name='Adres Anahtarı'
    )
    rank = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
        unique=True,
        verbose_name='Sıra'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'
        ordering = ['-id']


class Article(models.Model):
    title = models.CharField(
        null=False,
        blank=False,
        max_length=100,
        verbose_name='Başlık'
    )
    content = RichTextField(
        null=False,
        blank=False,
        verbose_name='İçerik'
    )
    slug = models.SlugField(
        null=False,
        blank=False,
        unique=True,
        verbose_name='Adres Anahtarı'
    )
    image = CropperImageField(
        null=False,
        blank=False,
        aspectratio=2.433333333333333,
        verbose_name='Afiş'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='category_to_article',
        null=False,
        blank=False,
        verbose_name='Kategori'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_to_article',
        null=False,
        blank=False,
        verbose_name='Yazar'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Yayın Durumu',
        help_text='Bu alan seçilirse makale yayınlanacaktır.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Yayın Tarihi'
    )

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('articles:detail', args=[self.slug])

    class Meta:
        verbose_name = 'Makale'
        verbose_name_plural = 'Makaleler'
        ordering = ['-created_at']


class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='article_to_comments',
        null=False,
        blank=False,
        verbose_name='Makale'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_to_comments',
        null=False,
        blank=False,
        verbose_name='Yazar'
    )
    comment = models.TextField(
        null=False,
        blank=False,
        verbose_name='Yorum'
    )
