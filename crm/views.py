from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages 
from django.http import HttpResponseRedirect

from cms.models import BlogArticle, ContentPage

from .models import WorkInquiryContact

from .forms import WorkInquiryContactForm


def work_inquiry_contact(request):
    """
    View user is redirected to
    after submitting the work inquiry contact form
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

            messages.success(request, "work-inquiry-contact-success")
            return HttpResponseRedirect(reverse_lazy('featured_articles'))

        # by-passes Django's built in form error messages
        messages.error(request, "work-inquiry-contact-error")
        return HttpResponseRedirect(reverse_lazy('index'))

    return HttpResponseRedirect(reverse_lazy("index"))
