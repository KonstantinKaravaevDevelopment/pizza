# Generated by Django 4.1 on 2022-10-07 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeria', '0006_rename_dodatki_dania_pizzeria_dodatki_pl_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dania_pizzeria',
            name='Cena',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='dania_pizzeria',
            name='Waga',
            field=models.CharField(max_length=150),
        ),
    ]