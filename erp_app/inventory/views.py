from django.shortcuts import render
from rest_framework import generics
from .models import Inventory
from .serializers import InventorySerializer

class InventoryListCreate(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class InventoryDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


