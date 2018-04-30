"""remote URL Configuration"""
from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    path('', include('remote_control.urls')),

    # красивые штуки для админки
    # path('grappelli/', include('grappelli.urls')),
    url(r'^jet/', include('jet.urls', 'jet')),

    path('admin/', admin.site.urls),
    path('default/', include('api.urls')),
    # path('default/', views.main_page),
]
