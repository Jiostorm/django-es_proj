from django.urls import path

from .views import *

urlpatterns = [
    path('', CovidReferenceListView.as_view(), name='ref_list'),
    path('new/', CovidReferenceCreateView.as_view(), name='ref_new'),
    path('<int:pk>/', CovidReferenceDetailView.as_view(), name='ref_detail'),
]
