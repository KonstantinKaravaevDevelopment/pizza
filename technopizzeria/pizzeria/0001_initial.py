# Generated by Django 4.0.5 on 2022-08-06 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Dania_Pizzeria',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Nazwa', models.CharField(max_length=50)),
                ('Opis', models.CharField(max_length=300)),
                ('Zdjecie', models.ImageField(upload_to=None)),
                ('Cena', models.FloatField(max_length=10)),
                ('Stan', models.BooleanField(default=False)),
                ('Waga', models.FloatField(max_length=10)),
                ('Rozmiar', models.IntegerField()),
                ('Dodatki', models.CharField(max_length=300)),
                ('Data', models.DateTimeField(auto_now_add=True)),
                ('Kategoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='pizzeria.category')),
                ('PodKategoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='pizzeria.subcategory')),
            ],
        ),
    ]
