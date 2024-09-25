from django.urls import path
from .views import InventoryListCreate, InventoryDetailUpdateDelete

urlpatterns = [
    path('inventory/', InventoryListCreate.as_view(), name='inventory-list'),
    path('inventory/<int:pk>/', InventoryDetailUpdateDelete.as_view(), name='inventory-detail'),
]
