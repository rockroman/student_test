from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='blog'),
    path('comment/<int:pk>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
    path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
]