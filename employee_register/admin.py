from django.contrib import admin

from .models import Employee, Position, Student, SchoolYear

# Register your models here.

admin.site.register(Employee)
admin.site.register(Position)
admin.site.register(Student)
admin.site.register(SchoolYear)
