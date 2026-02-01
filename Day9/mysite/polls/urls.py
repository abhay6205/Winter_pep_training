from django.urls import path, include

from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path("", views.index, name='index'),
    
]