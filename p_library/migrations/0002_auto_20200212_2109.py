# Generated by Django 3.0.3 on 2020-02-12 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='full_name',
            field=models.CharField(max_length=128),
        ),
    ]
