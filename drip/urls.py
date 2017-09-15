from django.conf.urls import url
from .views import subscribe, drip_dashboard, drip_subscribers, drip_subscriber_status


urlpatterns = [
    url(r'^$', drip_dashboard, name="drip_dashboard"),
    url(r'^subscribe/$', subscribe, name="subscribe"),

    url(r'^subscribers/$', drip_subscribers, name="drip_subscribers"),

    url(r'^subscriber/status/(?P<user_id>\d+)/$', drip_subscriber_status, name="drip_subscriber_status"),

]
