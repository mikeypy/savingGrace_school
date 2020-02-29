from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('employee-add/', views.employee_form, name='EmployeeInsertForm'),
    path('employee-update/<int:id>', views.employee_update_form, name='EmployeeUpdateForm'),
    path('employee-list/', views.employee_list, name='EmployeeList'),
    path('employee-delete/<int:id>', views.employee_delete, name='EmployeeDelete'),
    path('student-add/', views.student_form, name='StudentInsertForm'),
    path('student-update/<int:id>', views.student_update_form, name='StudentUpdateForm'),
    path('student-list/', views.student_list, name='StudentList'),
    path('student-delete/<int:id>', views.student_delete, name='StudentDelete'),
    path('redirect/', TemplateView.as_view(template_name='redirect.html'))
]
