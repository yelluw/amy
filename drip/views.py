from django.core.urlresolvers import reverse_lazy
from django.contrib import messages 
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import DripSubscriberForm

from .models import DripSubscriber, DripSubscriberList, DripMessage


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
                email=form.cleaned_data["email"],
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


@login_required
def drip_dashboard(request):
    """
    main area of drip functionality
    """
    return render(request, "drip-dashboard.html")


@login_required
def drip_subscribers(request):
    return render(
        request,
        "drip-subscribers.html",
        {"subscribers": DripSubscriber.objects.all()}
        )
