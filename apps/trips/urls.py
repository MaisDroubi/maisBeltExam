from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add', views.add),
    path('destination/<int:number>', views.destination),
    path('process', views.process),
    path('join/<int:number>', views.join),
    path('leave/<int:number>', views.leave)

]
