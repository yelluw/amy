from django.contrib import admin

from .models import DripSubscriberList, DripSubscriber, DripMessage


class DripSubscriberListAdmin(admin.ModelAdmin):
    list_display = ("name", "created")


class DripSubscriberAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display = ("created", "email", "funnel_entry_point", "lists")


    def lists(self, obj):
        """
        display lists subscriber belongs to
        """
        return "\n".join([dsl.name for dsl in obj.drip_subscriber_lists.all()])


class DripMessageAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display = ("title", "published", "created", "author")



admin.site.register(DripSubscriber, DripSubscriberAdmin)
admin.site.register(DripSubscriberList, DripSubscriberListAdmin)
admin.site.register(DripMessage, DripMessageAdmin)
