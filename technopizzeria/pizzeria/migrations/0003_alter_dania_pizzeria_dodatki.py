# Generated by Django 4.1 on 2022-08-08 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeria', '0002_remove_dania_pizzeria_podkategoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dania_pizzeria',
            name='Dodatki',
            field=models.CharField(max_length=500),
        ),
    ]
