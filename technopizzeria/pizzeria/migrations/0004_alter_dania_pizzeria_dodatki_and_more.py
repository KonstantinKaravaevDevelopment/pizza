# Generated by Django 4.1 on 2022-08-08 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeria', '0003_alter_dania_pizzeria_dodatki'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dania_pizzeria',
            name='Dodatki',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='dania_pizzeria',
            name='Opis',
            field=models.CharField(max_length=150),
        ),
    ]
