from django.db import models

class FileImage(models.Model):
    """Название изображения, которое необоходимо обработать"""
    name_image = models.CharField(max_lenght=200, verbose_name='Название изображения')
    name_file = models.FileField()
    data_added = models.DataTimeField(auto_now_add=True, verbose_name='Дата создания изображения')
    
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        
    def __str__(self):
        return self.name_image
