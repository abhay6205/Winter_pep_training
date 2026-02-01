from django.urls import path, include

from . import views
urlpatterns = [
    path('', views.portfolio_index, name='portfolio_index'),
]