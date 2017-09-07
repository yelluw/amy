from datetime import datetime

from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse_lazy

from crm.models import WorkInquiryContact
from crm.forms import WorkInquiryContactForm

#command: python3 manage.py test --verbosity=2


class WorkInquiryContactUnitTest(TestCase):
    """
    WorkInquiryContact model unit tests
    """
    pass

    def setUp(self):
        self.work_inquiry_contact = WorkInquiryContact.objects.create(
            inquiry_type="general",
            name="mr test",
            email="a@a.com",
            company="test corp",
            phone="1234567890",
            message="hello test"
        )


    def test_inquiry_type_field_type(self):
        self.assertIsInstance(self.work_inquiry_contact.inquiry_type, str)


    def test_inquiry_type_field_value(self):
        self.assertEqual(self.work_inquiry_contact.inquiry_type, "general")


    def test_name_field_type(self):
        self.assertIsInstance(self.work_inquiry_contact.name, str)


    def test_name_field_value(self):
        self.assertEqual(self.work_inquiry_contact.name, "mr test")


    def test_email_field_type(self):
        self.assertIsInstance(self.work_inquiry_contact.email, str)


    def test_email_field_value(self):
        self.assertEqual(self.work_inquiry_contact.email, "a@a.com")


    def test_company_field_type(self):
        self.assertIsInstance(self.work_inquiry_contact.company, str)


    def test_company_field_value(self):
        self.assertEqual(self.work_inquiry_contact.company, "test corp")


    def test_phone_field_type(self):
        self.assertIsInstance(self.work_inquiry_contact.phone, str)


    def test_phone_field_value(self):
        self.assertEqual(self.work_inquiry_contact.phone, "1234567890")


    def test_message_field_type(self):
        self.assertIsInstance(self.work_inquiry_contact.message, str)


    def test_message_field_value(self):
        self.assertEqual(self.work_inquiry_contact.message, "hello test")


    def test_received_on_field(self):
        self.assertIsInstance(self.work_inquiry_contact.received_on, datetime)


class CrmIntegrationTest(TestCase):
    """
    Integration tests for views

    TODO
    """
    pass


class WorkInquiryFormUnitTest(TestCase):
    """
    Test the actual form and not the view
    """

    def test_work_inquiry_form(self):
        data = {
            "inquiry_type": "general",
            "name": "Test",
            "email": "test@test.com",
            "company": "Test Corp.",
            "phone": "+1 (123)456-7890",
            "message": "This is a test",
        }
        form = WorkInquiryContactForm(data=data)
        self.assertTrue(form.is_valid())
