from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('<h2>Главная страница сайта подсчета площади изображения</h2>')