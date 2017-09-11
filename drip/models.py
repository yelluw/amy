from django.db import models


class DripSubscriberList(models.Model):
    """
    Defines a list of subscribers
    to which a message will be sent.
    """
    name = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class DripSubscriber(models.Model):
    """
    Defines a subscriber to all newsletters
    and or content sent by drip campaigns
    """
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    funnel_entry_point = models.TextField()
    drip_subscriber_lists = models.ManyToManyField(DripSubscriberList, blank=True)


    def __str__(self):
        return self.email
