from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, EmployeeViewSet, AttendanceViewSet, PerformanceViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'performance', PerformanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from . import views_charts
urlpatterns += [
    path('charts/', views_charts.chart_view, name='chart_page'),
    path('charts/employees-by-department/', views_charts.employees_by_department),
    path('charts/monthly-attendance/', views_charts.monthly_attendance),
]