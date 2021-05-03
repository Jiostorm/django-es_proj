from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Attendance
# Create your views here.

class AttendanceListView(LoginRequiredMixin, ListView):
    model = Attendance
    template_name = 'attend_list.html'
    context_object_name = 'all_attends_list'

class AttendanceCreateView(LoginRequiredMixin, CreateView):
    model = Attendance
    template_name = 'attend_new.html'
    fields = ('user_id', 'event_type', 'staff_id')

    def form_valid(self, form):
        form.instance.staff = self.request.user
        return super().form_valid(form)

class AttendanceDetailView(LoginRequiredMixin, DetailView):
    model = Attendance
    template_name = 'attend_detail.html'
    context_object_name = 'attend'
