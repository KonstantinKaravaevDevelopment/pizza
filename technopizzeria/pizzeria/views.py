from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


from .models import Dania_Pizzeria
from .models import Category
from .models import Language 
from .models import Configuration

from .serializers import DaniaSerializer
from .serializers import CategorySerializer
from .serializers import LanguageSerializer
from .serializers import ConfigurationSerializer



# Create your views here.


class DaniaAPIViewSet(viewsets.ModelViewSet):
    queryset = Dania_Pizzeria.objects.all()
    serializer_class = DaniaSerializer
    filter_backends=[DjangoFilterBackend]
    permission_classes = (IsAuthenticated,)

    filterset_fields = ['Id','Kategoria','Cena','Stan','Rozmiar','Waga']


class ConfigurationAPIViewSet(viewsets.ModelViewSet):
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer
    filter_backends=[DjangoFilterBackend]
    permission_classes = (IsAuthenticated,)


class CategoryAPIViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends=[DjangoFilterBackend]
    permission_classes = (IsAuthenticated,)


class LanguageAPIViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    filter_backends=[DjangoFilterBackend]
    permission_classes = (IsAuthenticated,)





# class DaniaAPIView(generics.ListAPIView):
#     queryset = Dania_Pizzeria.objects.all()
#     serializer_class = DaniaSerializer

# class DaniaAPIView(APIView):
#     def get(self,request):
#         lst = Dania_Pizzeria.objects.all().values()
#         return Response({'dania':list(lst)})
