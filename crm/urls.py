from django.conf.urls import url
from .views import thank_you 


urlpatterns = [
    # funnel
    url(r'^thank-you/$', thank_you, name="thank_you"),
]
