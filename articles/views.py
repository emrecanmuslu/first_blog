from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from articles.models import Article, Category, Comment
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q
from django.shortcuts import reverse
from articles.forms import CommentForm


def article_comment_create(request, id):
    article = get_object_or_404(Article, id=id)
    form = CommentForm(request.POST, None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.article = article
        obj.author = request.user
        obj.save()
        messages.success(request, 'Yorum eklendi.')

    return redirect(reverse('articles:detail', args=[article.slug]))


class ArticleDetailView(DetailView):
    template_name = 'articles/articles_detail.html'
    model = Article
    queryset = model.objects.prefetch_related('article_to_comments').filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data()
        context['form'] = CommentForm()

        return context


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
