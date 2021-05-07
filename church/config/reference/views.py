from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView

from .serializers import CovidReferenceUpdateModelSerializer
from .models import CovidReference
# Create your views here.

# API views

class CovidReferenceUpdateModelView(RetrieveUpdateAPIView):
    queryset = CovidReference.objects.all()
    serializer_class = CovidReferenceUpdateModelSerializer

class CovidReferenceListModelView(ListAPIView):
    queryset = CovidReference.objects.all()
    serializer_class = CovidReferenceUpdateModelSerializer

# Default views

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
