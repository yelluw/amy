from django.core.urlresolvers import reverse_lazy
from django.contrib import messages 
from django.http import HttpResponseRedirect
from django.core.exceptions import MultipleObjectsReturned
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

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

            try:
                drip_subscriber = DripSubscriber.objects.get(
                    email=form.cleaned_data["email"].lower()
                )
            
                messages.info(request, "subscription-exists")
                return HttpResponseRedirect(reverse_lazy('index'))

            except MultipleObjectsReturned:
            
                messages.info(request, "subscription-exists")
                return HttpResponseRedirect(reverse_lazy('index'))

            except DripSubscriber.DoesNotExist:

                drip_subscriber= DripSubscriber.objects.create(
                    email=form.cleaned_data["email"].lower(),
                    funnel_entry_point=form.cleaned_data["funnel_entry_point"]
                )

                messages.success(request, "subscription-success")

                if request.session.get('redirect_to', False):
                    return HttpResponseRedirect(request.session.get('redirect_to', reverse_lazy("index")))

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
    """
    Dashboard for subscriber data and admin 
    """
    return render(
        request,
        "drip-subscribers.html",
        {"subscribers": DripSubscriber.objects.all()}
        )


@login_required
def drip_subscriber_status(request, user_id):
    """
    Update the status of a drip subscriber
    to active / inactive
    """
    drip_subscriber = get_object_or_404(DripSubscriber, id=user_id)

    drip_subscriber.active = False if drip_subscriber.active == True else True

    drip_subscriber.save()

    return HttpResponseRedirect(reverse_lazy("drip_subscribers"))
