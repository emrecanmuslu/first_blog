from django.contrib import admin
from pages.models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'slug',
        'author',
        'image',
        'show_top_position',
        'show_bottom_position',
        'is_active',
        'created_at'
    ]
    search_fields = [
        'title',
        'author__username'
    ]
    list_display_links = [
        'title'
    ]
    prepopulated_fields = {'slug': ('title',), }
    autocomplete_fields = [
        'author'
    ]
    list_editable = [
        'show_top_position',
        'show_bottom_position',
        'is_active'
    ]




