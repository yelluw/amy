from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, Http404

from crm.forms import WorkInquiryContactForm
from drip.forms import DripSubscriberForm

from .models import BlogArticle, ContentPage


def index(request):
    """
    index view is reserved for
    whatever template is being rendered
    for the main landing page.
    """
    uri = reverse_lazy("index")
    location = "hero top under header"
    funnel_entry_point = f"URI: {uri}, Location: {location}"

    return render(
            request,
            "index.html",
                {
                    "drip_form": DripSubscriberForm(initial={"funnel_entry_point": funnel_entry_point}),
                    "form": WorkInquiryContactForm(),
                    "header_link": reverse_lazy("index")
                }
            )


def featured_articles(request):
    """
    Featured articles are those that have
    a specific business purpose and have
    precendence over others.
    """
    uri = reverse_lazy("featured_articles")
    location = "hero top under header"
    funnel_entry_point = f"URI: {uri}, Location: {location}"
    
    request.session['redirect_to'] = str(uri)

    articles_list = BlogArticle.objects.all()

    # Only paginate articles not marked as featured
    paginator = Paginator(articles_list.filter(featured=False, published=True).order_by('-id'), 2)

    try:
        articles = paginator.page(request.GET.get('page'))
    
    except PageNotAnInteger:
        articles = paginator.page(1)
    
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(
                request,
                "featured_articles.html",
                {
                    "featured_articles": articles_list.filter(featured=True, published=True),
                    "articles": articles,
                    "header_link": reverse_lazy("index"),
                    "form": WorkInquiryContactForm(),
                    "drip_form": DripSubscriberForm(initial={"funnel_entry_point": funnel_entry_point}),
                }
            )


def article(request, article_slug, article_id):
    """
    View pubished BlogArticle
    """
    uri = reverse_lazy("article", kwargs={"article_slug": article_slug, "article_id": article_id})
    location = "hero top under header"
    funnel_entry_point = f"URI: {uri}, Location: {location}"

    # redirect back to article again
    request.session['redirect_to'] = str(uri)

    article = get_object_or_404(BlogArticle, slug=article_slug, id=article_id, published=True)

    return render(
            request,
            "article.html",
                {
                    "article": article,
                    "header_link": reverse_lazy("featured_articles"),
                    "form": WorkInquiryContactForm(),
                    "drip_form": DripSubscriberForm(initial={"funnel_entry_point": funnel_entry_point}),
                }
            )


def page(request, page_slug):
    """
    View published ContentPage
    """
    content_page = get_object_or_404(ContentPage, slug=page_slug, published=True)

    return render(
            request,
            "page.html",
                {
                    "page": content_page,
                    "header_link": reverse_lazy("index")
                }
            )
