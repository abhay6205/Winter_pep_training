from django.db import models

# Create your models here.
class details(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField(max_length=300)

    def __str__(self): #if this will not define then all details will be stored as methods
        return f"{self.name} {self.email} {self.phone} {self.address}"
    
    
class FormModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to='images/', blank=True, null=True)
    
    #rename the instances of the model with their title name
    def __str__(self):
        return self.title
    
