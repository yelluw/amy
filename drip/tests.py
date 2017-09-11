from datetime import datetime

from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse_lazy

from drip.models import DripSubscriber, DripSubscriberList
from drip.forms import DripSubscriberForm
from drip.tracking import tracking_string

#command: python3 manage.py test --verbosity=2


class DripSubscriberUnitTest(TestCase):
    """
    DripsSubscriber model unit test
    """


    def setUp(self):

        self.drip_subscriber = DripSubscriber.objects.create(
            email="a@a.com",
            funnel_entry_point="URI: test, location: test",
        )



    def test_email_field_type(self):
        self.assertIsInstance(self.drip_subscriber.email, str)


    def test_email_field_value(self):
        self.assertEqual(self.drip_subscriber.email, "a@a.com")


    def test_funnel_entry_point_field_type(self):
        self.assertIsInstance(self.drip_subscriber.funnel_entry_point, str)


    def test_funnel_entry_point_field_value(self):
        self.assertEqual(self.drip_subscriber.funnel_entry_point, "URI: test, location: test")


    def test_active_field_type(self):
        self.assertIsInstance(self.drip_subscriber.active, bool)


    def test_active_field_value(self):
        self.assertEqual(self.drip_subscriber.active, True)


    def test_created_field(self):
        self.assertIsInstance(self.drip_subscriber.created, datetime)


    def test_drip_subscriber_list_field_value(self):
        self.assertTrue(self.drip_subscriber.drip_subscriber_lists.first() == None)


class DripIntegrationTest(TestCase):
    """
    Integrations tests for drip.views
    """


    def setUp(self):
        self.client = Client()

        self.data = {
            "email":"a@a.com",
            "funnel_entry_point": "URI: test, location: test"
        }


    def test_subscribe_view_does_302_redirect(self):
        response = self.client.post(reverse_lazy("subscribe"), data=self.data)
        self.assertTrue(response.status_code == 302)


    def test_subscribe_view_redirects_to_index_view(self):
        response = self.client.post(reverse_lazy("subscribe"), data=self.data)
        self.assertTrue(response.url == "/")


    def test_subscribe_view_redirects_when_session_is_set(self):
        session = self.client.session
        session["redirect_to"] = str(reverse_lazy("featured_articles"))
        session.save()

        response = self.client.post(reverse_lazy("subscribe"), data=self.data)
        self.assertTrue(response.url == (reverse_lazy("featured_articles")))


class DripSubscriberFormUnitTest(TestCase):
    """
    Test the actual DripSubscriberForm
    and not the view
    """


    def test_drip_subscriber_form(self):
        data = {
            "email":"a@a.com",
            "funnel_entry_point":"URI: test, location: test"
        }
        form = DripSubscriberForm(data=data)
        self.assertTrue(form.is_valid())


class DripTrackingUnitTest(TestCase):
    """
    Test drip.tracking
    utilities
    """


    def test_tracking_string_is_formatted_correctly(self):
        self.assertEqual(
            tracking_string(
                uri=reverse_lazy("index"),
                location="test"
            ),
            "URI /, Location: test"
        )