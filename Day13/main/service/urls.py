from django.urls import path, include

from . import views
urlpatterns = [
    path('', views.service_index, name='service_index'),
]