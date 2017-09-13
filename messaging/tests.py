from django.test import TestCase

from .email import send_email


class SendEmailUnitTest(TestCase):
    """
    email.send_email unit tests
    """


    def setUp(self):
        self.subject = "test subject"
        self.message = "test message"
        self.to = "pryelluw@gmail.com"


    def test_send_email_returns_one_on_success(self):
        sent = send_email(self.to, self.subject, self.message)
        self.assertTrue(sent)


    def test_send_email_returns_zero_on_failure(self):
        sent = send_email("", self.subject, self.message)
        self.assertFalse(sent)