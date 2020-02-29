from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import EmployeeForm, StudentForm
from .models import Employee, Student




#Homepage.
def homepage(request):
  context = {'object' :''}
  return render(request, 'home.html', context)


#Employee Area.
def employee_list(request):
  context = {'employee_list' : Employee.objects.all()}
  return render(request, 'employee_register/employee_list.html', context)
  



def employee_form(request):
  if not request.user.is_superuser:
    return redirect('/redirect')
  else:
     form = EmployeeForm(request.POST or None)
     if form.is_valid():
       form.save()
       form = EmployeeForm()
       return redirect('/employee-list')
     return render(request, 'employee_register/employee_form.html', {'form': form})

def employee_update_form(request, id):
  if not request.user.is_superuser:
    return redirect('/redirect')
  else:
    obj = get_object_or_404(Employee, id = id)
    form = EmployeeForm(request.POST or None, instance=obj)
    if form.is_valid():
      form.save()
      return redirect('/employee-list')
    return render(request, 'employee_register/employee_form.html', {'form': form})



def employee_delete(request, id):
  if not request.user.is_superuser:
    return redirect('/redirect')
  else:
    obj = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
      obj.delete()
      return redirect('/employee-list')
    return render(request, 'employee_register/employee_delete.html', {'object': obj})



  #Student Area'

def student_list(request):
  context = {'student_list' : Student.objects.all()}
  return render(request, 'student_register/student_list.html', context)
  



def student_form(request):
  if not request.user.is_superuser:
    return redirect('/redirect')
  else:
    form = StudentForm(request.POST or None)
    if form.is_valid():
      form.save()
      form = StudentForm()
      return redirect('/student-list')
    return render(request, 'student_register/student_form.html', {'form': form})

def student_update_form(request, id):
  if not request.user.is_superuser:
    return redirect('/redirect')
  else:
    obj = get_object_or_404(Student, id = id)
    form = StudentForm(request.POST or None, instance=obj)
    if form.is_valid():
      form.save()
      return redirect('/student-list')
    return render(request, 'student_register/student_form.html', {'form': form})



def student_delete(request, id):
  if not request.user.is_superuser:
    return redirect('/redirect')
  else:
    obj = get_object_or_404(Student, id=id)
    if request.method == 'POST':
      obj.delete()
      return redirect('/student-list')
    return render(request, 'student_register/student_delete.html', {'object': obj})