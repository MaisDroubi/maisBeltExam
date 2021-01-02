from django.urls import path
from . import views

urlpatterns = [
    path('', views.routetomain),
    path('main', views.index),
    path('login', views.login),
    path('register', views.register),
    path('logout', views.logout)
]
