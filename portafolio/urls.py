from django.urls import path
from . import views

urlpatterns = [
    path('', views.MensajeCreateView.as_view(), name='contactame'),
]
