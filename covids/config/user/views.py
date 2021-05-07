from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    UpdateView, DeleteView, CreateView
)

from rest_framework.generics import RetrieveAPIView, ListAPIView

from .serializers import UserVerifyModelSerializer
from .models import User
# Create your views here.

# API views

class UserVerifyModelView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserVerifyModelSerializer

class UserListModelView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserVerifyModelSerializer

# Default views

class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'all_user_list'

class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'user_new.html'
    fields = ('first_name', 'middle_name', 'last_name', 'birthdate', 'age', 'sex', 'profession', 'staff')

    def form_valid(self, form):
        form.instance.staff = self.request.user
        return super().form_valid(form)

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'd_user'

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('first_name', 'middle_name', 'last_name', 'birthdate', 'age', 'sex', 'profession', 'staff')
    template_name = 'user_edit.html'
