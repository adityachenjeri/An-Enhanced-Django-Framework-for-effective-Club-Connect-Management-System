"""
URL configuration for clubconnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
    path('', views.gitam, name= 'gitam'),
    path('sq', views.sq, name='sq'),
    path('index', views.index, name= 'index'),
    path('all_stu', views.all_stu, name= 'all_stu'),
    path('add_stu', views.add_stu, name= 'add_stu'),
    path('remove_stu', views.remove_stu, name= 'remove_stu'),
    path('remove_stu/<int:stu_id>', views.remove_stu, name='remove_stu'),
    path('filter_stu', views.filter_stu, name= 'filter_stu'),
]
    
