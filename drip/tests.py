from datetime import datetime

from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse_lazy

from drip.models import DripSubscriber
from drip.forms import DripSubscriberForm

#command: python3 manage.py test --verbosity=2


class DripSubscriberUnitTest(TestCase):
    """
    DripsSubscriber model unit test
    """


    def setUp(self):
        self.drip_subscriber = DripSubscriber.objects.create(
            email="a@a.com",
            funnel_entry_point="URI: test, location: test"
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


class DripIntegrationTest(TestCase):
    """
    Integrations tests for drip.views
    TODO
    """
    pass


class DripSubscriberFormUnittest(TestCase):
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
