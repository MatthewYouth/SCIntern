from django.core.management.base import BaseCommand
from employees.models import Department, Employee, Attendance, Performance
from faker import Faker
import random
from datetime import timedelta, date

fake = Faker()

class Command(BaseCommand):
    help = 'Seed database with fake employee data'

    def handle(self, *args, **kwargs):
        Department.objects.all().delete()
        Employee.objects.all().delete()

        departments = ['HR', 'Engineering', 'Sales', 'Marketing', 'Finance']
        dept_objs = []

        for dept_name in departments:
            dept_objs.append(Department.objects.create(name=dept_name))

        for _ in range(50):
            dept = random.choice(dept_objs)
            employee = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone_number=fake.phone_number(),
                address=fake.address(),
                date_of_joining=fake.date_between(start_date='-2y', end_date='today'),
                department=dept
            )
            for _ in range(10):
                date_attended = fake.date_between(start_date='-30d', end_date='today')
                Attendance.objects.create(
                    employee=employee,
                    date=date_attended,
                    status=random.choice(['Present', 'Absent', 'Late'])
                )
                Performance.objects.create(
                    employee=employee,
                    rating=random.randint(1, 5),
                    review_date=date_attended
                )
        self.stdout.write(self.style.SUCCESS('Successfully seeded data'))
