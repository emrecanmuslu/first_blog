from django.contrib import admin
from articles.models import Article, Category, Comment


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


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0
    classes = ['collapse']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]
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

    def get_queryset(self, request):
        qs = super(ArticleAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'article',
        'author',
        'created_at'
    ]
