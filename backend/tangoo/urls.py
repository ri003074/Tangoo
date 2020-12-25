from django.urls import path

from .views import ListTangoo, DetailTangoo

urlpatterns = [
    path('<int:pk>/', DetailTangoo.as_view()),
    path('', ListTangoo.as_view()),
]
