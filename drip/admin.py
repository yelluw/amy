from django.contrib import admin

from .models import DripSubscriber

class DripSubscriberAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display = ("created", "email", "funnel_entry_point")

admin.site.register(DripSubscriber, DripSubscriberAdmin)