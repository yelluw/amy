from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import messages 
from django.http import HttpResponseRedirect, Http404


from .forms import WorkInquiryContactForm

from .models import WorkInquiryContact, BlogArticle, ContentPage


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
    articles = BlogArticle.objects.filter()

    return render(
                request,
                "thank-you.html", 
                {
                    "header_link": BLOG_LINK,
                    "featured_articles": articles.filter(featured=True, published=True),
                    "articles": articles.filter(featured=False, published=True).order_by('-id')[:3] #newest 3 articles
                }
            )


def featured_articles(request):
    """
    Featured articles are those that have
    a specific business purpose and have
    precendence over others.
    """
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
                    "header_link": INDEX_LINK
                }
            )


def article(request, article_slug, article_id):
    """
    View pubished BlogArticle
    """
    article = get_object_or_404(BlogArticle, slug=article_slug, id=article_id, published=True)

    return render(
            request,
            "article.html",
                {
                    "article": article,
                    "header_link": BLOG_LINK
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
                    "header_link": INDEX_LINK
                }
            )
