from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='blog'),
    path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
]