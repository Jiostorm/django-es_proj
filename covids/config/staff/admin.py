from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import StaffCreationForm, StaffChangeForm
from .models import Staff

# Register your models here.
class StaffAdmin(UserAdmin):
    add_form = StaffCreationForm
    form = StaffChangeForm
    model = Staff
    list_display = ['email', 'username', 'sex', 'is_staff', ] # new
    fieldsets = UserAdmin.fieldsets + ( # new
        (None, {'fields': ('sex',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + ( # new
        (None, {'fields': ('sex',)}),
    )

admin.site.register(Staff, StaffAdmin)
