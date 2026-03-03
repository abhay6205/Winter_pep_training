from django.db import models

# Create your models here.
class Driver(models.Model):
   name = models.CharField(max_length=100)
   license_number = models.CharField(max_length=20)

class Student(models.Model):
    name = models.CharField(max_length=100)
    reg_no = models.IntegerField(primary_key=True)
    roll_no = models.IntegerField()

    def __str__(self):
        return self.name

class StudentReport(models.Model):
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    attendance = models.DecimalField(max_digits=5, decimal_places=2)
    cgpa = models.DecimalField(max_digits=3, decimal_places=2)
    reg_no = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"Report for {self.reg_no.name}"
