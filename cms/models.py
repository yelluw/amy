from django.db import models
from django.contrib.auth.models import User


class WorkInquiryContact(models.Model):
    """
    Stores all work inquiry messages
    sent through the WorkInquiryContactForm
    """
    inquiry_type = models.TextField()
    name = models.TextField()
    email = models.TextField()
    company = models.TextField()
    phone = models.TextField()
    message = models.TextField()
    received_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email


class BlogArticleCategory(models.Model):
    """
    Used to organize blog posts by category
    """
    name = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class BlogArticle(models.Model):
    """
    Used for common blog articles or posts.
    """
    author = models.ForeignKey(User)
    blog_article_category = models.ForeignKey(BlogArticleCategory, default=1)
    title = models.TextField()
    slug = models.SlugField(max_length=60)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    author_notes = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.title


class ContentPage(models.Model):
    """
    Used for content that
    does not go in the blog.
    Example: about page
    """
    author = models.ForeignKey(User)
    title = models.TextField()
    slug = models.SlugField(max_length=60)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    author_notes = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.title
