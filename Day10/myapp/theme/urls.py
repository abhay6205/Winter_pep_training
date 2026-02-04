from django.urls import path
from . import views
urlpatterns = [
    path('tailwind',views.index, name='index'),
]
