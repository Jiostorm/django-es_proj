from django.urls import path

from ..views import CovidReferenceUpdateModelView, CovidReferenceListModelView

urlpatterns = [
    path('', CovidReferenceListModelView.as_view()),
    path('<int:pk>', CovidReferenceUpdateModelView.as_view())
]
