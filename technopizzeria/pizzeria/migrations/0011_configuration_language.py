# Generated by Django 4.1 on 2022-12-29 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeria', '0010_category_kategoria_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('first_image', models.ImageField(upload_to='images/')),
                ('second_image', models.ImageField(upload_to='images/')),
                ('icon_na_miejscu', models.ImageField(upload_to='images/')),
                ('icon_na_wynos', models.ImageField(upload_to='images/')),
                ('icon_dodatki', models.ImageField(upload_to='images/')),
                ('icon_karta', models.ImageField(upload_to='images/')),
                ('icon_blik', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('Jezyk_image', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
    ]
