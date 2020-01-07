from django.contrib import admin
from user.models import *


class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name_event']}),
        ('Date information', {'fields': ['date_event']}),
    ]
    list_display = ('name_event', 'date_event')
    list_filter = ['date_event']
    search_fields = ['name_event']


admin.site.register(Event, EventAdmin)

