from django.urls import path, include

from . import views
urlpatterns = [
    path('', views.new1_index, name='neew1_index'),
]