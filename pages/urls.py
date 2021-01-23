from django.urls import path, include
from pages.views import IndexListView, PageDetailView

app_name = 'pages'
urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('<slug:slug>/detail/', PageDetailView.as_view(), name='detail')
]
