from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.jinja')


def django_page(request):
    return render(request, 'index.html', {'name': 'Django User'})

def jinja_page(request):
    return render(request, 'dashboard.jinja', {'name': 'Jinja User'})