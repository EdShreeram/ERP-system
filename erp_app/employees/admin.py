from django.contrib import admin
from .models import Employee, Department  # Adjust the import based on your structure

admin.site.register(Employee)
admin.site.register(Department)