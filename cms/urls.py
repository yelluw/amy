from django.conf.urls import url
from .views import index, thank_you, featured_articles, article


urlpatterns = [
    url(r'^$', index, name="index"),
    
    # funnel
    url(r'^thank-you/$', thank_you, name="thank_you"),

    #blog
    url(r'^blog/$', featured_articles, name="featured_articles"),
    url(r'^blog/(?P<article_slug>[\w-]+)/(?P<article_id>[\w-]+)/$', article, name="article"),

]
