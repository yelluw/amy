from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from cms.models import BlogArticle


class IntegrationTest(TestCase):
    """
    Integration tests for web pages

    command: python3 manage.py test --verbosity=2
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

        self.unpublished_blog_article = BlogArticle.objects.create(
            author=self.user,
            title="Not published",
            slug="not-published",
            content="really not published",
            category="Testing",
        )

        self.published_blog_article = BlogArticle.objects.create(
            author=self.user,
            title="Testing Testing 123",
            slug="testing-testing-123",
            content="This is a test!",
            category="Testing",
            published=True
        )


    def test_user_username(self):
        self.assertEqual(self.user.username, "test")


    def test_published_blog_article_slug(self):
        self.assertEqual(self.published_blog_article.slug, "testing-testing-123")


    def test_index(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)


    def test_thank_you(self):
        response = self.client.get(reverse("thank_you"))
        self.assertEqual(response.status_code, 200)


    def test_blog(self):
        response = self.client.get(reverse("featured_articles"))
        self.assertEqual(response.status_code, 200)


    def test_published_blog_article(self):
        response = self.client.get(
            reverse(
                "article", kwargs={
                    "article_slug": self.published_blog_article.slug,
                    "article_id": self.published_blog_article.id
                    }
            )
        )
        self.assertEqual(response.status_code, 200)


    def test_unpublished_blog_article(self):
        response = self.client.get(
            reverse(
                "article", kwargs={
                    "article_slug": self.unpublished_blog_article.slug,
                    "article_id": self.unpublished_blog_article.id
                    }
            )
        )
        self.assertEqual(response.status_code, 404)
