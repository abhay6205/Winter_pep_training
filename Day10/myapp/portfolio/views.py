from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def portfolio_index(request):
    return HttpResponse("Welcome to the Portfolio Home Page.")