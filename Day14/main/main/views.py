from django.shortcuts import render
from django.http import HttpResponse

def service_index(request):
    return render(request, 'service.html')

def about_index(request):
    return render(request, 'about.html')

def home_index(request):
    return render(request, 'home.html')

def main_index(request):
    return render(request, 'main.html')