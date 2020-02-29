from django.db import models

# Create your models here.

class Position(models.Model):
  title = models.CharField(max_length=50)

  def __str__(self):
    return self.title

class Employee(models.Model):
  fullname = models.CharField(max_length=200)
  emp_code = models.CharField(max_length=20)
  mobile_no = models.CharField(max_length=20)
  position = models.ForeignKey(Position, on_delete=models.CASCADE)


  def __str__(self):
    return self.fullname



class SchoolYear(models.Model):
  title = models.CharField(max_length=50)

  def __str__(self):
    return self.title

class Student(models.Model):
  fullname = models.CharField(max_length=200)
  age = models.PositiveIntegerField()
  home_address = models.CharField(max_length=20)
  year = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)


  def __str__(self):
    return self.fullname