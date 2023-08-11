from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('membership/', views.MembershipPageView.as_view(), name='membership'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
]