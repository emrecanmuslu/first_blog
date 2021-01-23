# from django.shortcuts import render, get_object_or_404
from articles.models import Article, Category
from django.views.generic import ListView, DetailView
from django.db.models import Q


class ArticleDetailView(DetailView):
    template_name = 'articles/articles_detail.html'
    model = Article
    queryset = model.objects.filter(is_active=True)


class SearchView(ListView):
    template_name = 'articles/articles_search.html'
    model = Article
    paginate_by = 2

    def get_queryset(self):
        q = self.request.GET.get('q', None)
        object_list = self.model.objects.none()
        if q:
            object_list = self.model.objects.filter(Q(title__icontains=q) | Q(content__icontains=q), is_active=True)

        return object_list


class ArticleCategoryView(ListView):
    template_name = 'articles/articles_category.html'
    model = Article
    paginate_by = 2

    def get_queryset(self):
        slug = self.kwargs.get('slug', '')
        object_list = self.model.objects.none()
        if slug:
            object_list = self.model.objects.select_related('category').filter(is_active=True, category__slug=slug)

        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.filter(slug=self.kwargs.get('slug', None)).first()
        return context
