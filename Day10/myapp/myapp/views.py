from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'index.html')

def contact(request):
    # return HttpResponse("This is the contact page of the polls app.")
    return render(request, 'contact.html')
def about(request):
    # return HttpResponse("This is the about page of the polls app.")
    return render(request, 'about.html')

def projects(request):
    return render(request, 'project.html')

def content(request):
    return render(request, 'content.html')

# def portfolio(request):
    return HttpResponse("Welcome to the Portfolio Home Page.")