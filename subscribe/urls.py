from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe, name="subscribe"),
    path('', views.HomePageView.as_view(), name='home'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
]
 