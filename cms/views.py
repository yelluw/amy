from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib import messages 
from django.http import HttpResponseRedirect

from .forms import WorkInquiryContactForm

from .models import WorkInquiryContact


def index(request):
    """
    index view is reserved for
    whatever template is being rendered
    for the main landing page.
    """
    if request.method == 'POST':
        form = WorkInquiryContactForm(request.POST)

        if form.is_valid():

            work_inquiry_contact = WorkInquiryContact.objects.create(
                inquiry_type=form.cleaned_data["inquiry_type"],
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                company=form.cleaned_data["company"],
                phone=form.cleaned_data["phone"],
                message=form.cleaned_data["message"]
            )

            return HttpResponseRedirect(reverse('thank_you'))

    return render(request, "index.html", {"form": WorkInquiryContactForm()})


def thank_you(request):
    """
    View user is redirected to
    after submitting the work inquiry contact form
    """
    return render(request, "thank-you.html")
