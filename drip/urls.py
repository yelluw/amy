from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', drip_dashboard, name="drip_dashboard"),
    url(r'^subscribe/$', subscribe, name="subscribe"),

    url(r'^subscribers/$', drip_subscribers, name="drip_subscribers"),

    url(r'^subscriber-lists/$', drip_subscriber_lists, name="drip_subscriber_lists"),

    url(r'^subscriber-list/subscribers/(?P<drip_subscriber_list_id>\d+)/$', drip_subscriber_list_subscribers, name="drip_subscriber_list_subscribers"),

    url(r'^subscriber-list/new/$', create_drip_subscriber_list, name="create_drip_subscriber_list"),

    url(r'^subscriber/status/(?P<user_id>\d+)/$', drip_subscriber_status, name="drip_subscriber_status"),

]
