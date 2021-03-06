from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse

from .models import FileImage, Topic
from .forms import FileImageForm, TopicForm

def index(request):
	"""Отображение тем на домашней странице"""
	topics = Topic.objects.order_by('data_added')
	context = {'topics': topics}
	return render(request, 'pagemain/index.html', context)

def images_topic(request, topic_id):
	"""Отображение изображений в теме"""
	topic = Topic.objects.get(id=topic_id)
	images = topic.fileimage_set.order_by('-data_added')
	context = {'topic': topic, 'images': images}
	return render(request, 'pagemain/images_topic.html', context)


# def index(request):
# 	images = FileImage.objects.order_by('data_added')

# 	if request.method == 'POST':
# 		form = FileImageForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			instance = FileImage(name_file=request.FILES['name_file'])
# 			instance.name_image = request.POST.get('name_image')
# 			instance.description_file = request.POST.get('description_file')
# 			instance.save()
# 			return HttpResponseRedirect(reverse('pagemain:index'))
# 	else:
# 		form = FileImageForm()
# 	return render(request, 'pagemain/index.html', {'form': form, 'images': images})

def del_image(request, image_id):
	"""Удаление изображения из списка (таблицы) изображений"""
	try:
		image = FileImage.objects.get(id=image_id)
		image.delete()
		return HttpResponseRedirect(reverse('pagemain:index'))
	except FileImage.DoesNotExist:
		return HttpResponseNotFound('<h2>Изображение не найдено</h2>')	