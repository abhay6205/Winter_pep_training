from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import TodoForm, TodoListForm
from .models import Todo, TodoList

def index(request):
    todo_lists = TodoList.objects.all()

    if request.method == "POST":
        if 'save_list' in request.POST:
            form = TodoListForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('todo')
        elif 'save_task' in request.POST:
            form = TodoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('todo')
    
    list_form = TodoListForm()
    task_form = TodoForm()

    page = {
        "list_form": list_form,
        "task_form": task_form,
        "todo_lists": todo_lists,
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html', page)

def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')

def remove_list(request, list_id):
    lista = TodoList.objects.get(id=list_id)
    lista.delete()
    messages.info(request, "List removed !!!")
    return redirect('todo')