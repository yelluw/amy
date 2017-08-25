from django.contrib import admin
from .models import WorkInquiryContact, BlogArticle, BlogArticleCategory, ContentPage


class WorkInquiryContactAdmin(admin.ModelAdmin):
    date_hierarchy = "received_on"
    list_display = ("received_on", "email", "name", "message")


class BlogArticleAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display = ("title", "published", "featured", "author", "created", "blog_article_category")
    prepopulated_fields = {"slug": ("title",)}


class BlogArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class ContentPageAdmin(admin.ModelAdmin):
    list_display = ("title", "published",  "author", "slug", "created")


admin.site.register(WorkInquiryContact, WorkInquiryContactAdmin)
admin.site.register(BlogArticle, BlogArticleAdmin)
admin.site.register(BlogArticleCategory, BlogArticleCategoryAdmin)
admin.site.register(ContentPage, ContentPageAdmin)
