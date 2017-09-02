from django.conf.urls import url
from .views import work_inquiry_contact 


urlpatterns = [
    # funnel
    url(r'^work-inquiry-contact/$', work_inquiry_contact, name="work_inquiry_contact"),
]
