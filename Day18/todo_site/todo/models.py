from django.db import models
from django.utils import timezone

class TodoList(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def __str__(self):
        return self.title