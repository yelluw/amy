from django.core.urlresolvers import reverse_lazy
from django.contrib import messages 
from django.http import HttpResponseRedirect

from .forms import DripSubscriberForm

from .models import DripSubscriber


def subscribe(request):
    """
    General entry point
    for subscribers to
    enter drip
    """
    if request.method == 'GET':
        return HttpResponseRedirect(reverse_lazy("index"))

    form = DripSubscriberForm(request.POST)

    if form.is_valid():
        drip_subscriber = DripSubscriber.objects.create(
            email=form.cleaned_data["email"],
            funnel_entry_point=form.cleaned_data["funnel_entry_point"]
        )

        return HttpResponseRedirect(reverse_lazy('subscriber_thank_you'))

    return HttpResponseRedirect(reverse_lazy("index"))
