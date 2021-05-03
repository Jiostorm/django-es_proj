from django.urls import path

from .views import *

urlpatterns = [
    path('', CCListView.as_view(), name='cc_list'),
    path('new/', CCCreateView.as_view(), name='cc_new'),
    path('<int:pk>/', CCDetailView.as_view(), name='cc_detail'),
]
