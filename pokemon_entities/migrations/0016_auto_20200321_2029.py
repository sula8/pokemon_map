# Generated by Django 2.2.3 on 2020-03-21 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0015_auto_20200321_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='images',
            field=models.ImageField(upload_to='', verbose_name='Изображение'),
        ),
    ]