from django.contrib import admin

from .models import CloseContact
# Register your models here.

class CloseContactAdmin(admin.ModelAdmin):
    model = CloseContact
    list_display = ['covid_user_id', 'close_user_id', 'date_recorded', 'date_quarantine_ends']

admin.site.register(CloseContact, CloseContactAdmin)
