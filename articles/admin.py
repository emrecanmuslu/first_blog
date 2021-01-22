from django.contrib import admin
from articles.models import Article, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug'
    ]
    search_fields = [
        'name'
    ]
    prepopulated_fields = {'slug': ('name',), }


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'slug',
        'author',
        'category',
        'is_active',
        'created_at'
    ]
    list_filter = [
        'is_active',
        'author',
        'category',
        'created_at'
    ]
    search_fields = [
        'title',
        'author__username',
        'category__name'
    ]
    prepopulated_fields = {'slug': ('title',), }
    autocomplete_fields = [
        'author',
        'category'
    ]
    list_editable = [
        'is_active'
    ]
