from django.urls import path

from .views import *

urlpatterns = [
    path('', AttendanceListView.as_view(), name='attend_list'),
    path('new/', AttendanceCreateView.as_view(), name='attend_new'),
    path('<int:pk>/', AttendanceDetailView.as_view(), name='attend_detail'),
]
