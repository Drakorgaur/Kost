from . import views
from django.conf.urls import include, url
from django.urls import path, re_path
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.Mafia.index, name='index'),
    path('random/', views.Mafia.randomizer, name='random'),
]