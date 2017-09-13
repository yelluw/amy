from django.conf.urls import url
from .views import subscribe, drip_dashboard, drip_subscribers


urlpatterns = [
    url(r'^$', drip_dashboard, name="drip_dashboard"),
    url(r'^subscribers/$', drip_subscribers, name="drip_subscribers"),

    url(r'^subscribe/$', subscribe, name="subscribe"),
]
