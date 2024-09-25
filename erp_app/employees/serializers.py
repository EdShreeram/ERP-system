from rest_framework import serializers
from .models import Employee, Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']

class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'email', 'department', 'hire_date']

    def create(self, validated_data):
        # Extract department data from validated data
        department_data = validated_data.pop('department', None)
        if department_data:
            # Get or create the department instance
            department, created = Department.objects.get_or_create(name=department_data['name'])
            validated_data['department'] = department

        # Create and return the employee instance
        return Employee.objects.create(**validated_data)
