from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def new2_index(request):
    return HttpResponse("Welcome to the new2 Home Page.")