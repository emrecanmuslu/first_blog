from django.urls import path
from articles.views import SearchView, ArticleCategoryView, ArticleDetailView

app_name = 'articles'
urlpatterns = [
    path('<slug:slug>/detail/', ArticleDetailView.as_view(), name='detail'),
    path('search/', SearchView.as_view(), name='search'),
    path('<slug:slug>/category/', ArticleCategoryView.as_view(), name='category')
]
