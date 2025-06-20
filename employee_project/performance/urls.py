from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('employees.urls')),
    path('api/', include('attendance.urls')),
    path('api/', include('performance.urls')),
]