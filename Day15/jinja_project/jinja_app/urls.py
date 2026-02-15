from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('django/', views.django_page, name='index_django'),
    path('jinja/', views.jinja_page, name='index_jinja'),
]
