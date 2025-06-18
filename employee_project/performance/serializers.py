from rest_framework import serializers
from employees.models import Employee
from .models import Performance

class PerformanceSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField(read_only=True)
    employee_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(),
        source='employee',
        write_only=True
    )

    class Meta:
        model = Performance
        fields = '__all__'