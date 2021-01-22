from django.db import models
from django.contrib.auth.models import User
from cropperjs.models import CropperImageField
from ckeditor.fields import RichTextField


class Page(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_to_page',
        null=True,
        blank=True,
        verbose_name='Kullanıcı'
    )
    title = models.CharField(
        null=False,
        blank=False,
        max_length=50,
        verbose_name='Başlık'
    )
    slug = models.SlugField(
        null=False,
        blank=False,
        unique=True,
        verbose_name='Adres Anahtarı'
    )
    content = RichTextField(
        null=False,
        blank=False,
        verbose_name='İçerik'
    )
    sort = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
        unique=True,
        verbose_name='Sıra'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Sayfa Durumu',
        help_text='Bu alan seçilirse sayfa yayınlanacaktır.'
    )
    show_top_position = models.BooleanField(
        default=True,
        verbose_name='Header',
        help_text='Seçilirse anamenüde görünecek.'
    )
    show_bottom_position = models.BooleanField(
        default=True,
        verbose_name='Footer',
        help_text='Seçilirse footerda görünecek.'
    )
    image = CropperImageField(
        null=False,
        blank=False,
        aspectratio=1.7777,
        verbose_name='Fotoğraf'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Eklenme Tarihi'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Sayfa'
        verbose_name_plural = 'Sayfalar'
        ordering = ['-sort']
