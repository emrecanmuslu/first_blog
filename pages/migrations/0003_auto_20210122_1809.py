# Generated by Django 3.1.5 on 2021-01-22 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_page_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Başlık'),
        ),
    ]
