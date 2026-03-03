from django.contrib import admin

# Register your models here.
from .models import Driver, Student, StudentReport
admin.site.register(Driver)
admin.site.register(Student)
admin.site.register(StudentReport)