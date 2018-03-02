from django.urls import path

from . import views


urlpatterns = [
    path('send_command/', views.send_command),
    path('test_ground/', views.test_ground),
    path('main/', views.main_page),
    path('sensors/', views.sensors)
]
