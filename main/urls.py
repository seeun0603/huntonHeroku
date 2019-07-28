from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.main, name= 'main'),
    path('searchKeyword/', views.searchKeyword,name='searchKeyword'),
    path('mypage', views.mypage, name='mypage'),
]
