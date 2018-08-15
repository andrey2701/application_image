from django import forms
from .models import FileImage

class FileImageForm(forms.ModelForm):
    class Meta:
        model = FileImage
        fields = ['name_image', 'name_file', 'escription_file']
