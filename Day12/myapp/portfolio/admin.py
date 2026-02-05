from django.contrib import admin

# Register your models here.
from .models import details
admin.site.register(details)


from .models import FormModel
admin.site.register(FormModel)