from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy

from cms.models import BlogArticle, BlogArticleCategory

#command: python3 manage.py test --verbosity=2

class CmsIntegrationTest(TestCase):
    """
    Integration tests for views
    """


    def setUp(self):
        self.client = Client()

        self.user = User.objects.create(
            username="test",
            password="hello_world",
            email="test@test.com",
            first_name="hello",
            last_name="world"
        )

        self.blog_article_category = BlogArticleCategory.objects.create(
            name="Testing"
        )

        self.unpublished_blog_article = BlogArticle.objects.create(
            author=self.user,
            title="Not published",
            slug="not-published",
            content="really not published",
            blog_article_category=self.blog_article_category,
        )

        self.published_blog_article = BlogArticle.objects.create(
            author=self.user,
            title="Testing Testing 123",
            slug="testing-testing-123",
            content="This is a test!",
            blog_article_category=self.blog_article_category,
            published=True
        )


    def test_index(self):
        response = self.client.get(reverse_lazy("index"))
        self.assertEqual(response.status_code, 200)


    def test_blog(self):
        response = self.client.get(reverse_lazy("featured_articles"))
        self.assertEqual(response.status_code, 200)


    def test_published_blog_article(self):
        response = self.client.get(
            reverse_lazy(
                "article", kwargs={
                    "article_slug": self.published_blog_article.slug,
                    "article_id": self.published_blog_article.id
                    }
            )
        )
        self.assertEqual(response.status_code, 200)


    def test_unpublished_blog_article(self):
        response = self.client.get(
            reverse_lazy(
                "article", kwargs={
                    "article_slug": self.unpublished_blog_article.slug,
                    "article_id": self.unpublished_blog_article.id
                    }
            )
        )
        self.assertEqual(response.status_code, 404)
