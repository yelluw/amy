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
    if request.method == 'POST':

        form = DripSubscriberForm(request.POST)

        if form.is_valid():

            drip_subscriber, created = DripSubscriber.objects.get_or_create(
                email=form.cleaned_data["email"].lower(),
                funnel_entry_point=form.cleaned_data["funnel_entry_point"]
            )

            if created:
                messages.success(request, "subscription-success")

                if request.session.get('redirect_to', False):
                    return HttpResponseRedirect(request.session.get('redirect_to', reverse_lazy("index")))

                return HttpResponseRedirect(reverse_lazy('index'))

            messages.info(request, "subscription-exists")
            return HttpResponseRedirect(reverse_lazy('index'))

    return HttpResponseRedirect(reverse_lazy("index"))
