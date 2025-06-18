from django.shortcuts import render
from django.db.models import Count
from django.http import JsonResponse
from .models import Department, Attendance
from django.db.models.functions import TruncMonth


def chart_view(request):
    return render(request, 'charts.html')

def employees_by_department(request):
    data = Department.objects.annotate(total=Count('employees'))
    labels = [d.name for d in data]
    values = [d.total for d in data]
    return JsonResponse({"labels": labels, "values": values})

def monthly_attendance(request):
    qs = Attendance.objects.annotate(month=TruncMonth('date'))
    months = sorted(set(qs.values_list('month', flat=True)))

    data = {"labels": [m.strftime("%B %Y") for m in months], "present": [], "absent": [], "late": []}
    for month in months:
        month_qs = qs.filter(month=month)
        data["present"].append(month_qs.filter(status="Present").count())
        data["absent"].append(month_qs.filter(status="Absent").count())
        data["late"].append(month_qs.filter(status="Late").count())

    return JsonResponse(data)



