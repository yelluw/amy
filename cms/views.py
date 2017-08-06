from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import messages 
from django.http import HttpResponseRedirect, Http404

from .forms import WorkInquiryContactForm

from .models import WorkInquiryContact, BlogArticle


INDEX_LINK = reverse_lazy("index")
BLOG_LINK = reverse_lazy("featured_articles")


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

    return render(
            request,
            "index.html",
                {
                    "form": WorkInquiryContactForm(),
                    "header_link": INDEX_LINK
                }
            )


def thank_you(request):
    """
    View user is redirected to
    after submitting the work inquiry contact form
    """
    return render(request, "thank-you.html", {"header_link": BLOG_LINK})


def featured_articles(request):
    """
    Featured articles are those thta have
    a specific business purpose and have
    precendence over others.
    """
    articles = BlogArticle.objects.filter()
    return render(
                request,
                "featured_articles.html",
                {
                    "featured_articles": articles.filter(featured=True),
                    "articles": articles.filter(featured=False),
                    "header_link": INDEX_LINK
                }
            )


def article(request, article_slug, article_id):
    """
    View pubished BlogArticle from DB
    """
    try:
        article = BlogArticle.objects.get(id=article_id, published=True)
    except BlogArticle.DoesNotExist:
        raise Http404("Article does not exists")

    return render(
            request,
            "article.html",
                {
                    "article": article,
                    "header_link": BLOG_LINK
                }
            )
