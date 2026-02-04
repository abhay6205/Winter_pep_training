from django.db import models

# Create your models here.
class details(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField(max_length=300)

    def __str__(self): #if this will not define then all details will be stored as methods
        return f"{self.name} {self.email} {self.phone} {self.address}"