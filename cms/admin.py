from django.contrib import admin
from .models import WorkInquiryContact, BlogArticle


class WorkInquiryContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'received_on'
    list_display = ("received_on", "email", "name", "message")


class BlogArticleAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ("published", "featured", "title", "author", "slug", "created")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(WorkInquiryContact, WorkInquiryContactAdmin)
admin.site.register(BlogArticle, BlogArticleAdmin)
