from django.conf.urls import url
from .views import index, featured_articles, article, page


urlpatterns = [
    url(r'^$', index, name="index"),

    # blog
    url(r'^blog/$', featured_articles, name="featured_articles"),
    url(r'^blog/(?P<article_slug>[\w-]+)/(?P<article_id>[\w-]+)/$', article, name="article"),

    # pages
    url(r'^(?P<page_slug>[\w-]+)/$', page, name="page"),
]
