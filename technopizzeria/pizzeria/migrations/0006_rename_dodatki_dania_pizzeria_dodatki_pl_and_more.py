# Generated by Django 4.1 on 2022-09-04 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeria', '0005_dania_pizzeria_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dania_pizzeria',
            old_name='Dodatki',
            new_name='Dodatki_PL',
        ),
        migrations.RenameField(
            model_name='dania_pizzeria',
            old_name='Nazwa',
            new_name='Nazwa_PL',
        ),
        migrations.RenameField(
            model_name='dania_pizzeria',
            old_name='Opis',
            new_name='Opis_PL',
        ),
        migrations.AddField(
            model_name='dania_pizzeria',
            name='Dodatki_DE',
            field=models.CharField(default='<Wpisz coś>', max_length=600),
        ),
        migrations.AddField(
            model_name='dania_pizzeria',
            name='Dodatki_EN',
            field=models.CharField(default='<Wpisz coś>', max_length=600),
        ),
        migrations.AddField(
            model_name='dania_pizzeria',
            name='Dodatki_RU',
            field=models.CharField(default='<Wpisz coś>', max_length=600),
        ),
        migrations.AddField(
            model_name='dania_pizzeria',
            name='Nazwa_DE',
            field=models.CharField(default='<Wpisz coś>', max_length=50),
        ),
        migrations.AddField(
            model_name='dania_pizzeria',
            name='Nazwa_EN',
            field=models.CharField(default='<Wpisz coś>', max_length=50),
        ),
        migrations.AddField(
            model_name='dania_pizzeria',
            name='Nazwa_RU',
            field=models.CharField(default='<Wpisz coś>', max_length=50),
        ),
        migrations.AddField(
            model_name='dania_pizzeria',
            name='Opis_DE',
            field=models.CharField(default='<Wpisz coś>', max_length=150),
        ),
        migrations.AddField(
            model_name='dania_pizzeria',
            name='Opis_EN',
            field=models.CharField(default='<Wpisz coś>', max_length=150),
        ),
        migrations.AddField(
            model_name='dania_pizzeria',
            name='Opis_RU',
            field=models.CharField(default='<Wpisz coś>', max_length=150),
        ),
        migrations.AlterField(
            model_name='dania_pizzeria',
            name='Zdjecie',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
