from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


from .models import Dania_Pizzeria
from .serializers import DaniaSerializer

# Create your views here.


class DaniaAPIViewSet(viewsets.ModelViewSet):
    queryset = Dania_Pizzeria.objects.all()
    serializer_class = DaniaSerializer
    filter_backends=[DjangoFilterBackend]
    permission_classes = (IsAuthenticated,)

    filterset_fields = ['Id','Kategoria','Cena','Stan','Rozmiar','Waga']




# class DaniaAPIView(generics.ListAPIView):
#     queryset = Dania_Pizzeria.objects.all()
#     serializer_class = DaniaSerializer

# class DaniaAPIView(APIView):
#     def get(self,request):
#         lst = Dania_Pizzeria.objects.all().values()
#         return Response({'dania':list(lst)})
