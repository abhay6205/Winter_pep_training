from django.urls import path, include

from . import views
urlpatterns = [
    path('', views.new2_index, name='new2_index'),
]