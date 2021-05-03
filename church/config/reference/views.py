from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import CovidReference
# Create your views here.

class CovidReferenceListView(LoginRequiredMixin, ListView):
    model = CovidReference
    template_name = 'ref_list.html'
    context_object_name = 'all_refs_list'

class CovidReferenceCreateView(LoginRequiredMixin, CreateView):
    model = CovidReference
    template_name = 'ref_new.html'
    fields = ('user', 'staff_id', 'covid_reference_id')

    def form_valid(self, form):
        form.instance.staff = self.request.user
        return super().form_valid(form)

class CovidReferenceDetailView(LoginRequiredMixin, DetailView):
    model = CovidReference
    template_name = 'ref_detail.html'
    context_object_name = 'ref'
