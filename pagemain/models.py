from django.db import models

class FileImage(models.Model):
    """Название изображения, которое необоходимо обработать"""
    name_image = models.CharField(max_length=200,
                                  verbose_name='Название изображения')
    name_file = models.ImageField(upload_to='file_to_process/%Y/%m/%d/',
                                  width_field='file_width',
                                  height_field='file_height')
    description_file = models.TextField(blank=True,
                                        verbose_name='Описание файла')
    file_width = PositiveSmallIntegerField()
    file_height = PositiveSmallIntegerField()
    data_added = models.DataTimeField(auto_now_add=True,
                                      verbose_name='Дата создания изображения')
    
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        
    def __str__(self):
        return self.name_image
