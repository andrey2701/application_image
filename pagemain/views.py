from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import FileImage
from .forms import FileImageForm

def index(request):
	if request.method == 'POST':
		form = FileImageForm(request.POST, request.FILES)
		if form.is_valid():
			instance = FileImage(file_field=request.FILES['file'])
			instance.save()
			return HttpResponseRedirect('/success')
	else:
		form = FileImageForm()
	return render(request, 'pagemain/index.html', {'form': form})

def success(request):
	return HttpResponse('<h2>Файл сохранен</h2>')

