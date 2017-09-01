from django.contrib import admin

from .models import WorkInquiryContact

class WorkInquiryContactAdmin(admin.ModelAdmin):
    date_hierarchy = "received_on"
    list_display = ("received_on", "email", "name", "message")

admin.site.register(WorkInquiryContact, WorkInquiryContactAdmin)
