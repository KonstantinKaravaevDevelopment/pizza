# Generated by Django 4.1 on 2022-08-07 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeria', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dania_pizzeria',
            name='PodKategoria',
        ),
        migrations.AlterField(
            model_name='dania_pizzeria',
            name='Zdjecie',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
