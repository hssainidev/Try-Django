from django.urls import path

from .views import (
    article_create_view,
    article_detail_view,
    article_search_view
)

app_name = 'articles'
urlpatterns = [
    path(r'', article_search_view, name='search'),
    path(r'create/', article_create_view, name='create'),
    path(r'<slug:slug>/', article_detail_view, name='detail'),

]
