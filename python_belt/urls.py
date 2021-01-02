from django.contrib import admin
from django.urls import path, include  

urlpatterns = [
    path('', include('apps.users.urls')),
    path('travels/', include('apps.trips.urls')),
]
