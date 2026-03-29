from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('add-list/', views.add_task_list, name='add_task_list'),
    path('delete-list/<int:list_id>/', views.delete_task_list, name='delete_task_list'),
    path('add/<int:list_id>/', views.add_todo, name='add_todo'),
    path('update/<int:todo_id>/', views.update_todo, name='update_todo'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
]
