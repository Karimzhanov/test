from django.contrib import admin
from apps.base import views
from django.urls import path
urlpatterns = [
    path("", views.index, name='index'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog_details', views.blog_details, name='blog_details')

    
]