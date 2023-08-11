from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('visit', views.visit, name="visit"),
    path('team', views.team, name="team"),
    path('vacancies/save', views.save_vacancy, name="save_vacancy"),
    path('vacancies/delete/<id>', views.delete_vacancy, name="delete_vacancy"),
    path('vacancies/update/<id>', views.update_vacancy, name="update_vacancy"),
]
 