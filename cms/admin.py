from django.contrib import admin
from .models import WorkInquiryContact, BlogArticle, BlogArticleCategory


class WorkInquiryContactAdmin(admin.ModelAdmin):
    date_hierarchy = "received_on"
    list_display = ("received_on", "email", "name", "message")


class BlogArticleAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display = ("title", "published", "featured", "author", "created",)
    prepopulated_fields = {"slug": ("title",)}


class BlogArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(WorkInquiryContact, WorkInquiryContactAdmin)
admin.site.register(BlogArticle, BlogArticleAdmin)
admin.site.register(BlogArticleCategory, BlogArticleCategoryAdmin)