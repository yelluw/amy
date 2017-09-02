from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse_lazy

from .forms import WorkInquiryContactForm

#command: python3 manage.py test --verbosity=2

class CrmIntegrationTest(TestCase):
    """
    Integration tests for views
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
