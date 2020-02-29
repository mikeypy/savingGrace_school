from django import forms
from .models import Employee, Student


class EmployeeForm(forms.ModelForm):
  class Meta:
    model = Employee
    fields = '__all__'
    labels = {
      'fullname': 'STAFF FULL NAME ',
      'emp_code': 'STAFF ID ',
      'mobile_no': 'STAFF MOBILE NUMBER ',
      'position': 'STAFF POSITION '
    }

  def __init__(self, *args, **kwargs):
    super(EmployeeForm, self).__init__(*args, **kwargs)
    self.fields['position'].empty_label = 'Select'
    #self.fields['emp_code'].required = False


    
class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = '__all__'
    labels = {
      'fullname': 'FULL NAME ',
      'age': 'AGE ',
      'home_address': 'HOME ADDRESS ',
      'year': 'CLASS YEAR '
    }

  def __init__(self, *args, **kwargs):
    super(StudentForm, self).__init__(*args, **kwargs)
    self.fields['year'].empty_label = 'Select'

