from django import forms
from .models import FileImage

class FileImageForm(forms.ModelForm):
    class Meta:
        model = FileImage
        fields = ['name_file', 'name_image', 'description_file']
        localized_fields = ('__all__')
        
    name_image = forms.CharField(label='Название изображения',
                                 widget=forms.TextInput(attrs={'size': 60}),
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
    								   required=False,
                                       widget=forms.Textarea(attrs={'cols': 40, 'rows': 7}),
                                      )