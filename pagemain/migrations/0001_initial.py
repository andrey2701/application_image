# Generated by Django 2.1 on 2018-08-16 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_image', models.CharField(max_length=200, verbose_name='Название изображения')),
                ('name_file', models.ImageField(height_field='file_height', upload_to='file_to_process/%Y/%m/%d/', width_field='file_width')),
                ('description_file', models.TextField(blank=True, verbose_name='Описание файла')),
                ('file_width', models.PositiveSmallIntegerField()),
                ('file_height', models.PositiveSmallIntegerField()),
                ('data_added', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания изображения')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
