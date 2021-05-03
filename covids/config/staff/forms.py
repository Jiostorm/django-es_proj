from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Staff

class StaffCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Staff
        fields = UserCreationForm.Meta.fields + ('sex',)

class StaffChangeForm(UserChangeForm):
    class Meta:
        model = Staff
        fields = UserChangeForm.Meta.fields
