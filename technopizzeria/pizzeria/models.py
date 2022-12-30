from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Dania_Pizzeria(models.Model):
    Id = models.AutoField(primary_key=True)
    Kategoria = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    #PodKategoria = models.ForeignKey('SubCategory', on_delete=models.PROTECT, null=True)
    Nazwa_PL = models.CharField(max_length=50)
    Nazwa_EN = models.CharField(max_length=50, default='<Wpisz coś>')
    Nazwa_DE = models.CharField(max_length=50, default='<Wpisz coś>')
    Nazwa_RU = models.CharField(max_length=50, default='<Wpisz coś>')
    Opis_PL = models.CharField(max_length=150)
    Opis_EN = models.CharField(max_length=150, default='<Wpisz coś>')
    Opis_DE = models.CharField(max_length=150, default='<Wpisz coś>')
    Opis_RU = models.CharField(max_length=150, default='<Wpisz coś>')
    Zdjecie = models.ImageField(upload_to='images/')
    Cena = models.CharField(max_length=50)
    Stan = models.BooleanField(default=False)
    Waga = models.CharField(max_length=50)
    Rozmiar = models.CharField(max_length=50)
    Skladniki_PL = models.CharField(max_length=600, default='<Wpisz coś>')
    Skladniki_EN = models.CharField(max_length=600, default='<Wpisz coś>')
    Skladniki_DE = models.CharField(max_length=600, default='<Wpisz coś>')
    Skladniki_RU = models.CharField(max_length=600, default='<Wpisz coś>')
    Dodatki_PL = models.CharField(max_length=600)
    Dodatki_EN = models.CharField(max_length=600, default='<Wpisz coś>')
    Dodatki_DE = models.CharField(max_length=600, default='<Wpisz coś>')
    Dodatki_RU = models.CharField(max_length=600, default='<Wpisz coś>')
    Data = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='Uzytkownik', on_delete=models.CASCADE)

    def __str__(self):
        return self.Nazwa_PL


class Configuration(models.Model):
    name = models.CharField(max_length=50, db_index = True)
    first_image = models.ImageField(upload_to='images/')
    second_image = models.ImageField(upload_to='images/')
    icon_na_miejscu = models.ImageField(upload_to='images/')
    icon_na_wynos = models.ImageField(upload_to='images/')
    icon_dodatki = models.ImageField(upload_to='images/')
    icon_karta = models.ImageField(upload_to='images/')
    icon_blik = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

    
class Category(models.Model):
    name = models.CharField(max_length=50, db_index = True)
    Kategoria_image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50, db_index = True)
    Jezyk_image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.name
    

# class SubCategory(models.Model):
#     name = models.CharField(max_length=50, db_index = True)

#     def __str__(self):
#         return self.name

