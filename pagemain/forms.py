from django import forms
from .models import FileImage

class FileImageForm(forms.ModelForm):
    class Meta:
        model = FileImage
        widgets = {
        'description_file': forms.Textarea
        }
        fields = ['name_image', 'name_file', 'description_file']
        
    name_image = forms.CharField(label='Название изображения',
    							 error_messages={
    							 'required': 'Введите название изображения'
    							 				}
    							 )
    name_file = forms.ImageField(label='Загрузить изображение',
    							 error_messages={
    							 'required': 'Укажите файл изображения',
    							 'invalid_image': 'Неправильный формат изображения',
    							 'mossing': 'Произошла ошибка чтения файла. Попробуйте снова.'
    							 				}
    							 )
    description_file = forms.CharField(label='Описание изображения',
    								   required=False)