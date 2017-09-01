from django.conf.urls import url
from .views import subscribe


urlpatterns = [
    url(r'^subscribe/$', subscribe, name="subscribe"),
]
