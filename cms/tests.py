from datetime import datetime

from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy

from cms.models import BlogArticle, BlogArticleCategory, ContentPage

#command: python3 manage.py test --verbosity=2


class BlogArticleCategoryUnitTest(TestCase):
    """
    Unit tests for model BlogArticleCategory
    """


    def setUp(self):

        self.blog_article_category = BlogArticleCategory.objects.create(
            name="Test"
        )


    def test_name_field(self):
        self.assertEqual(self.blog_article_category.name, "Test")


    def test_created_field(self):
        self.assertIsInstance(self.blog_article_category.created, datetime)


class BlogArticleUnitTest(TestCase):
    """
    Unit tests for model BlogArticle
    """


    def setUp(self):

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
            published=True,
            author_notes="This is a test note."
        )


    def test_author_field(self):
        self.assertIsInstance(self.published_blog_article.author, User)


    def test_blog_article_category_field(self):
        self.assertIsInstance(self.published_blog_article.blog_article_category, BlogArticleCategory)


    def test_blog_article_category_field_defaults_to_one(self):
        self.assertEqual(self.published_blog_article.blog_article_category.id, 1)


    def test_title_field(self):
        self.assertEqual(self.published_blog_article.title, "Testing Testing 123")


    def test_slug_field(self):
        self.assertEqual(self.published_blog_article.slug, "testing-testing-123")


    def test_content_field(self):
        self.assertEqual(self.published_blog_article.content, "This is a test!")


    def test_created_field(self):
        self.assertIsInstance(self.published_blog_article.created, datetime)


    def test_published_field_set_to_true_is_true(self):
        self.assertTrue(self.published_blog_article.published)


    def test_published_field_set_to_false_as_default(self):
        self.assertFalse(self.unpublished_blog_article.published)


    def test_featured_field_set_to_false_as_default(self):
        self.assertFalse(self.published_blog_article.featured == True)


    def test_author_notes_field(self):
        self.assertEqual(self.published_blog_article.author_notes, "This is a test note.")


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
