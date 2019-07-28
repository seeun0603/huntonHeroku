from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.new, name= 'new'),
    path('edit/<int:board_id>', views.edit, name='edit'),
    path('detail/<int:board_id>', views.detail, name = 'detail'),
    path('delete/<int:board_id>', views.delete, name='delete'),
    path('<int:board_id>/comment/create', views.comment_create, name="comment_create"),
    path('<int:board_id>/comment/<int:comment_id>/delete', views.comment_delete, name="comment_delete"),
    path('<int:board_id>/comment/<int:comment_id>/edit', views.comment_edit, name="comment_edit"),
]
