# Generated by Django 4.1 on 2022-12-29 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeria', '0009_dania_pizzeria_skladniki_de_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Kategoria_image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
