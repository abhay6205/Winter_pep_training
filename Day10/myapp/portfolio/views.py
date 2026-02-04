# from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.
# def portfolio_index(request):
#     return HttpResponse("Welcome to the Portfolio Home Page.")


from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import details

def portfolio_index(request):
    all_details = details.objects.all()
    template = loader.get_template('detail.html')
    context = {
        'all_details': all_details,
    }
    return HttpResponse(template.render(context, request))