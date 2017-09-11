from django.contrib import admin

from .models import DripSubscriberList, DripSubscriber


class DripSubscriberListAdmin(admin.ModelAdmin):
    list_display = ("name", "created")



class DripSubscriberAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display = ("created", "email", "funnel_entry_point", "lists")


    def lists(self, obj):
        """
        display lists subscriber belongs to
        """
        return "\n".join([drip_subscriber_list.name for drip_subscriber_list in obj.drip_subscriber_lists.all()])


admin.site.register(DripSubscriber, DripSubscriberAdmin)
admin.site.register(DripSubscriberList, DripSubscriberListAdmin)
