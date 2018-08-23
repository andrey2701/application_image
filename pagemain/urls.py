"""Определяет схемы URL для пользователей"""
from django.urls import path, re_path
# from django.contrib.auth.views import login
from . import views
from django.views.generic import TemplateView

# Установка пространства имен для users
app_name = 'pagemain'

urlpatterns = [
# Домашняя страница с темами
path('', views.index, name='index'),
# Отображение изображений по теме
path('images_topic/<int:topic_id>/', views.images_topic, name='images_topic'),
# Удаление изображения
path('del_image/<int:image_id>/', views.del_image, name='del_image'),
]