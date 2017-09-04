from django.contrib import admin
from .models import BlogArticle, BlogArticleCategory, ContentPage


class BlogArticleAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display = ("title", "published", "featured", "author", "created", "blog_article_category")
    prepopulated_fields = {"slug": ("title",)}


class BlogArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class ContentPageAdmin(admin.ModelAdmin):
    list_display = ("title", "published",  "author", "slug", "created")


admin.site.register(BlogArticle, BlogArticleAdmin)
admin.site.register(BlogArticleCategory, BlogArticleCategoryAdmin)
admin.site.register(ContentPage, ContentPageAdmin)
