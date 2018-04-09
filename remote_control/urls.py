from django.urls import path

from . import views


urlpatterns = [
    path('', views.main_page),
    path('send_command/', views.send_command),
    path('test_ground/', views.test_ground),
    path('sensors/', views.sensors),
    path('registration/', views.registration),
    path('login/', views.login_user),
    path('logout/', views.logout_user),
]
