from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

from cms.models import BlogArticle, ContentPage

from .models import WorkInquiryContact

from .forms import WorkInquiryContactForm


def thank_you(request):
    """
    View user is redirected to
    after submitting the work inquiry contact form
    """
    articles = BlogArticle.objects.filter()

    return render(
                request,
                "thank-you.html", 
                {
                    "header_link": reverse_lazy("featured_articles"),
                    "featured_articles": articles.filter(featured=True, published=True),
                    "articles": articles.filter(featured=False, published=True).order_by('-id')[:3] #newest 3 articles
                }
            )