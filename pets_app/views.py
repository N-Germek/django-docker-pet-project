from django.shortcuts import render
from rest_framework import generics
from .models import Pet
from .serializer import PetSerializer


class PetsList(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class PetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
