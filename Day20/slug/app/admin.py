from django.contrib import admin

# Register your models here.
from .models import student
admin.site.register(student)

from .models import Article
admin.site.register(Article)