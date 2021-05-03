from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Log
# Create your views here.

class LogListView(LoginRequiredMixin, ListView):
    model = Log
    template_name = 'logs_list.html'
    context_object_name = 'all_logs_list'

class LogCreateView(LoginRequiredMixin, CreateView):
    model = Log
    template_name = 'logs_new.html'
    fields = ('covid_user_id', 'staff_id', 'date_swabbed', 'covid_status', 'health_status')

    def form_valid(self, form):
        form.instance.staff = self.request.user
        return super().form_valid(form)

class LogDetailView(LoginRequiredMixin, DetailView):
    model = Log
    template_name = 'logs_detail.html'
    context_object_name = 'logs'
