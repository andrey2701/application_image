from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse

from .models import FileImage
from .forms import FileImageForm

def index(request):
	images = FileImage.objects.order_by('data_added')

	if request.method == 'POST':
		form = FileImageForm(request.POST, request.FILES)
		if form.is_valid():
			instance = FileImage(name_file=request.FILES['name_file'])
			instance.name_image = request.POST.get('name_image')
			instance.description_file = request.POST.get('description_file')
			instance.save()
			return HttpResponseRedirect(reverse('pagemain:index'))
	else:
		form = FileImageForm()
	return render(request, 'pagemain/index.html', {'form': form, 'images': images})

def success(request):
	return HttpResponse('<h2>Файл сохранен</h2>')

def del_image(request, image_id):
	try:
		image = FileImage.objects.get(id=image_id)
		image.delete()
		return HttpResponseRedirect(reverse('pagemain:index'))
	except FileImage.DoesNotExist:
		return HttpResponseNotFound('<h2>Изображение не найдено</h2>')	