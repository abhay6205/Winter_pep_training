from django.urls import path, include
from .views import home_view, form_view, form1_view
from . import views
urlpatterns = [
    path('', views.portfolio_index, name='portfolio_index'),
    path('home/', views.home_view, name='home'),
    path('form',form_view, name='form_view'),
    path('form1',form1_view, name='form1_view'),
]