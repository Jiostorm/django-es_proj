from django.urls import path

from ..views import UserVerifyModelView, UserListModelView

urlpatterns = [
    path('', UserListModelView.as_view()),
    path('<int:pk>/', UserVerifyModelView.as_view())
]
