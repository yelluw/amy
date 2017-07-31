from django.conf.urls import url
from .views import index, thank_you


urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^thank-you/$', thank_you, name="thank_you"),
]
