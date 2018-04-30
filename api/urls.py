from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.test),
    path('telemetry/', views.telemetry),
    path('answers/', views.answer)
]