from django.conf.urls import url
from .views import subscribe, drip_dashboard


urlpatterns = [
    url(r'^$', drip_dashboard, name="drip_dashboard"),

    url(r'^subscribe/$', subscribe, name="subscribe"),
]
