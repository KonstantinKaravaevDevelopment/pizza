from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Dania_Pizzeria(models.Model):
    Id = models.AutoField(primary_key=True)
    Kategoria = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    #PodKategoria = models.ForeignKey('SubCategory', on_delete=models.PROTECT, null=True)
    Nazwa = models.CharField(max_length=50)
    Opis = models.CharField(max_length=150)
    Zdjecie = models.ImageField(upload_to='images')
    Cena = models.FloatField(max_length=10)
    Stan = models.BooleanField(default=False)
    Waga = models.FloatField(max_length=10)
    Rozmiar = models.IntegerField()
    Dodatki = models.CharField(max_length=600)
    Data = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='Uzytkownik', on_delete=models.CASCADE)

    def __str__(self):
        return self.Nazwa

    
class Category(models.Model):
    name = models.CharField(max_length=50, db_index = True)

    def __str__(self):
        return self.name
    

# class SubCategory(models.Model):
#     name = models.CharField(max_length=50, db_index = True)

#     def __str__(self):
#         return self.name