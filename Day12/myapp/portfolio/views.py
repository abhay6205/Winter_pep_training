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


from .forms import InputForm, FormModelForm

def home_view(request):
    context = {}
    context['form'] = InputForm()
    return render(request, "home.html", context)


def form_view(request):
    if request.method == 'POST':
        form = FormModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Data saved successfully")
    else:
        form = FormModelForm()
    return render(request, "form.html", {'form': form})

def form1_view(request):
    if request.method == 'POST':
        print(request.POST) #prints the posted data as a QueryDict
        name = request.POST.get('your_name')
        email = request.POST.get('your_email')
        address = request.POST.get('your_address')
    return render(request, "form1.html")