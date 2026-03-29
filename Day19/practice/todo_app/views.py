from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskList, Todo


def todo_list(request):
    """Display all task lists with their nested tasks."""
    task_lists = TaskList.objects.prefetch_related('todos').all()
    total_tasks = Todo.objects.count()
    completed_tasks = Todo.objects.filter(completed=True).count()
    pending_tasks = total_tasks - completed_tasks
    context = {
        'task_lists': task_lists,
        'total': total_tasks,
        'completed': completed_tasks,
        'pending': pending_tasks,
    }
    return render(request, 'todo_app/todo_list.html', context)


def add_task_list(request):
    """Create a new task list."""
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        if name:
            TaskList.objects.create(name=name)
    return redirect('todo_list')


def delete_task_list(request, list_id):
    """Delete an entire task list and all its tasks."""
    task_list = get_object_or_404(TaskList, id=list_id)
    if request.method == 'POST':
        task_list.delete()
    return redirect('todo_list')


def add_todo(request, list_id):
    """Add a new todo item inside a specific task list."""
    task_list = get_object_or_404(TaskList, id=list_id)
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        if title:
            Todo.objects.create(
                task_list=task_list, title=title, description=description
            )
    return redirect('todo_list')


def update_todo(request, todo_id):
    """Toggle the completed status of a todo."""
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        todo.completed = not todo.completed
        todo.save()
    return redirect('todo_list')


def delete_todo(request, todo_id):
    """Delete a todo item."""
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        todo.delete()
    return redirect('todo_list')
