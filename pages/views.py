from django.shortcuts import render
from articles.models import Article
from pages.models import Page
from django.views.generic import ListView, DetailView


class IndexListView(ListView):
    template_name = 'index.html'
    model = Article
    paginate_by = 2

    def get_queryset(self):
        object_list = self.model.objects.filter(is_active=True)

        return object_list


class PageDetailView(DetailView):
    template_name = 'pages/pages_detail.html'
    model = Page
    queryset = model.objects.filter(is_active=True)
