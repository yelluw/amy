from django.core.urlresolvers import reverse_lazy
from django.contrib import messages 
from django.http import HttpResponseRedirect
from django.core.exceptions import MultipleObjectsReturned
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *

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


@login_required
def drip_subscriber_lists(request):
    """
    view all subscriber lists
    """
    return render(
        request,
        "drip-subscriber-lists.html",
        {
            "subscriber_lists": DripSubscriberList.objects.all(),
            "create_form": CreateDripSubscriberListForm(),
            "update_form": UpdateDripSubscriberListForm()
        }
    )


@login_required
def create_drip_subscriber_list(request):
    """
    view to create new drip subscriber lists
    """
    if request.method == 'POST':
        form = CreateDripSubscriberListForm(request.POST)

        if form.is_valid():
            drip_subscriber_list = DripSubscriberList.objects.create(
                name=form.cleaned_data["name"]
            )

    return HttpResponseRedirect(reverse_lazy("drip_subscriber_lists"))


@login_required
def update_drip_subscriber_list(request):
    """
    Update an existing drip subscriber list
    """

    if request.method == 'POST':
        form = UpdateDripSubscriberListForm(request.POST)

        if form.is_valid():

            drip_subscriber_list = get_object_or_404(
                DripSubscriberList,
                id=form.cleaned_data["drip_subscriber_list_id"]
            )

            drip_subscriber_list.name = form.cleaned_data["name"]
            drip_subscriber_list.save()

    return HttpResponseRedirect(reverse_lazy("drip_subscriber_lists"))


@login_required
def delete_drip_subscriber_list(request, drip_subscriber_list_id):
    """
    delete a drip subscriber list by id
    """
    drip_subscriber_list = get_object_or_404(DripSubscriberList, id=drip_subscriber_list_id)

    drip_subscriber_list.delete()

    return HttpResponseRedirect(reverse_lazy("drip_subscriber_lists"))


@login_required
def drip_subscriber_list_subscribers(request, drip_subscriber_list_id):
    """
    view subscribers for a given list
    """
    drip_subscriber_list = get_object_or_404(DripSubscriberList, id=drip_subscriber_list_id)

    drip_subscribers = DripSubscriber.objects.filter(drip_subscriber_lists__id=drip_subscriber_list.id)

    return render(
        request,
        "drip-subscriber-list-subscribers.html",
        {"drip_subscriber_list_subscribers": drip_subscribers})


@login_required
def drip_messages(request):
    """
    view all drip messages
    """
    return render(
        request,
        "drip-messages.html",
        {"drip_messages": DripMessage.objects.all()}
    )


@login_required
def drip_message(request, message_id):
    """
    view one drip message by id
    """
    return render(
        request,
        "drip-message.html",
        {"drip_message": get_object_or_404(DripMessage, id=message_id)}
    )


@login_required
def email_single_drip_subscriber(request):
    """
    view to email single drip subscriber
    """
    return render(
        request,
        "email-single-drip-subscriber.html",
        {"form": EmailSingleDripSubscriberForm()}
    )
