from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('lovnik/', views.lovenik, name='love'),
    path('onkrut/', views.onkrut, name='onkrut'),
]
