from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import CloseContact
# Create your views here.

class CCListView(LoginRequiredMixin, ListView):
    model = CloseContact
    template_name = 'cc_list.html'
    context_object_name = 'all_cc_list'

class CCCreateView(LoginRequiredMixin, CreateView):
    model = CloseContact
    template_name = 'cc_new.html'
    fields = ('covid_user_id', 'close_user_id', 'staff_id')

    def form_valid(self, form):
        form.instance.staff = self.request.user
        return super().form_valid(form)

class CCDetailView(LoginRequiredMixin, DetailView):
    model = CloseContact
    template_name = 'cc_detail.html'
    context_object_name = 'cc'
