from django.db import models


class WorkInquiryContact(models.Model):
    """
    Stores all work inquiry messages
    sent through the WorkInquiryContactForm
    """
    inquiry_type = models.TextField()
    name = models.TextField()
    email = models.TextField()
    company = models.TextField()
    phone = models.TextField()
    message = models.TextField()
    received_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email
