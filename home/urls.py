from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('visit', views.visit, name="visit"),
    path('team', views.team, name="team")
]
 