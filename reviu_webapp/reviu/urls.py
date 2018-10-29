from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    #url(r'^logout/$', views.logout, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url(r'^$', views.home, name='home'),
]