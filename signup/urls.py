
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name= 'signup'),
    path('success/', views.registerSuccess, name = 'registerSuccess'),
    path('id_overlap_check/', views.id_overlap_check, name = 'id_overlap_check')
]
