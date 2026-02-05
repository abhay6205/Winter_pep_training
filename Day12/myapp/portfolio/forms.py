from django import forms

class InputForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    phone = forms.CharField(label='Your Phone Number', max_length=15)
    address = forms.CharField(label='Your Address', widget=forms.Textarea)
    password = forms.CharField(label='Your Password', widget=forms.PasswordInput())
    
    
#import class form from django
from django import forms

#imports the model form from models.py
from .models import FormModel

#create a ModelForm
class FormModelForm(forms.ModelForm):
    #specify the name of model to use
    class Meta:
        model = FormModel
        fields = ['title', 'description']