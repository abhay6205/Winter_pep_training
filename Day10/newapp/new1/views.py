from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def new1_index(request):
    return HttpResponse("Welcome to the new1 Home Page.")