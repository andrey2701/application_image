"""Определяет схемы URL для пользователей"""
from django.urls import path, re_path
# from django.contrib.auth.views import login
from . import views
from django.views.generic import TemplateView

# Установка пространства имен для users
app_name = 'pagemain'

urlpatterns = [
# Домашняя страница
path('', views.index, name='index'),
path('success/', views.success, name='success'),
path('del_image/<int:image_id>/', views.del_image, name='del_image'),
]