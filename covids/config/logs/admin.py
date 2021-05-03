from django.contrib import admin

from .models import Log
# Register your models here.

class LogAdmin(admin.ModelAdmin):
    model = Log
    list_display = ['date_swabbed', 'covid_status', 'date_recorded', 'date_quarantine_ends', 'health_status']

admin.site.register(Log, LogAdmin)
