# Generated by Django 3.0.3 on 2020-02-17 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0003_auto_20200214_0755'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='images',
            field=models.ImageField(default=None, upload_to='images/', verbose_name='Изображение книги'),
            preserve_default=False,
        ),
    ]
