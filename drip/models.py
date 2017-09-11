from django.db import models


class DripSubscriber(models.Model):
    """
    Defines a subscriber to all newsletters
    and or content sent by drip campaigns
    """
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    funnel_entry_point = models.TextField()


    def __str__(self):
        return self.email
