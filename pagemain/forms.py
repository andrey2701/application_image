from django import forms
from .models import FileImage

class FileImageForm(forms.ModelForm):
    class Meta:
        model = FileImage
        fields = ['name_image', 'name_file', 'description_file']
        labels = {'name_image': 'Название изображения',
                  'name_file': 'Загрузить изображение',
                  'description_file': 'Описание изображения'}
        
