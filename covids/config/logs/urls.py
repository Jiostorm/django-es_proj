from django.urls import path

from .views import *

urlpatterns = [
    path('', LogListView.as_view(), name='logs_list'),
    path('new/', LogCreateView.as_view(), name='logs_new'),
    path('<int:pk>/', LogDetailView.as_view(), name='logs_detail'),
]
