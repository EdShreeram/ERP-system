from django.urls import path
from .views import EmployeeListCreate, EmployeeDetailUpdateDelete, DepartmentListCreate, DepartmentDetailUpdateDelete

urlpatterns = [
    path('employees/', EmployeeListCreate.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeDetailUpdateDelete.as_view(), name='employee-detail'),
    path('departments/', DepartmentListCreate.as_view(), name='department-list'),
    path('departments/<int:pk>/', DepartmentDetailUpdateDelete.as_view(), name='department-detail'),
]
